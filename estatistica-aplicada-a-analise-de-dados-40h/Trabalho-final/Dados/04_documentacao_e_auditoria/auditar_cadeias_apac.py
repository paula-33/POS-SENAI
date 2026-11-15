"""Auditoria agregada de referências APAC anteriores, sem exportar chaves pessoais.

Lê os 648 ATDAC DBCs locais. Valores APAC/CNS são usados apenas em memória;
nenhuma chave, hash ou linha individual é exportada.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import csv, hashlib, hmac, os, re, stat, sys
import dbc_reader
from dbc_reader import DbcReader

ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/'Dados/01_fontes_originais/APAC/APAC_ATD_2024_2025_bruto'
OUT=ROOT/'Dados/02_derivados_preliminares/APAC/auditoria_continuidade_20261105_v1'
if sys.platform=='darwin':
    blast=Path(dbc_reader.__file__).parent/'bin'/'blast-dbf-darwin'
    if blast.is_file() and not (blast.stat().st_mode & stat.S_IXUSR):
        blast.chmod(blast.stat().st_mode|stat.S_IXUSR)

def val(x): return '' if x is None else str(x).strip()
def date8(x):
    s=re.sub(r'\D','',val(x))
    if len(s)!=8 or s=='00000000': return None
    try: return datetime.strptime(s,'%Y%m%d').date()
    except ValueError: return None
def ref_value(x):
    s=val(x)
    return '' if not s or not s.strip('0') else s
def write(path, rows):
    rows=list(rows)
    with path.open('x',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows)

def main():
    OUT.mkdir(parents=True,exist_ok=False)
    files=sorted(RAW.glob('ATD*.dbc'))
    assert len(files)==648, f'Esperados 648 DBCs, encontrados {len(files)}'
    # Salt aleatório efêmero: tokens só permitem comparar CNS dentro desta execução.
    salt=os.urandom(32)
    patient_token={}
    auth_patients=defaultdict(set)
    auth_start={};auth_end={};auth_types=defaultdict(set)
    edges={}
    counts=Counter(); by_tp=Counter()
    for i,path in enumerate(files,1):
        for row in DbcReader(str(path)):
            counts['linhas_lidas']+=1
            auth=val(row.get('AP_AUTORIZ'))
            if not auth or not auth.strip('0'):
                counts['linhas_sem_autorizacao']+=1; continue
            pid=val(row.get('AP_CNSPCN'))
            token=None
            if pid:
                if pid not in patient_token:
                    patient_token[pid]=hmac.new(salt,pid.encode(),hashlib.sha256).digest()
                token=patient_token[pid]
                auth_patients[auth].add(token)
            tp=val(row.get('AP_TPAPAC')) or '(vazio)'
            auth_types[auth].add(tp); by_tp[(tp,'linhas')]+=1
            st,en=date8(row.get('AP_DTINIC')),date8(row.get('AP_DTFIM'))
            if st and (auth not in auth_start or st<auth_start[auth]): auth_start[auth]=st
            if en and (auth not in auth_end or en>auth_end[auth]): auth_end[auth]=en
            prev=ref_value(row.get('AP_APACANT'))
            if prev:
                counts['linhas_com_apac_anterior']+=1
                key=(auth,prev)
                e=edges.setdefault(key,{'tokens':set(),'starts':[],'types':set()})
                if token: e['tokens'].add(token)
                if st: e['starts'].append(st)
                e['types'].add(tp)
            elif tp=='2':
                counts['linhas_tp2_sem_referencia_anterior']+=1
        if i%108==0: print(f'Lidos {i}/648 DBCs; {counts["linhas_lidas"]:,} registros',flush=True)
    counts['autorizacoes_unicas']=len(auth_patients.keys()|auth_types.keys())
    counts['autorizacoes_com_multiplos_ids_no_conjunto']=sum(len(v)>1 for v in auth_patients.values())
    counts['referencias_unicas_filha_pai']=len(edges)
    summary_by_tp=Counter()
    for (child,parent),e in edges.items():
        summary_by_tp['referencias_unicas']+=1
        if child==parent: summary_by_tp['referencia_propria']+=1
        target_pids=auth_patients.get(parent,set())
        if not target_pids:
            summary_by_tp['alvo_nao_encontrado_no_recorte']+=1
        else:
            summary_by_tp['alvo_encontrado_no_recorte']+=1
            if e['tokens'] and e['tokens'] & target_pids:
                summary_by_tp['ids_com_alguma_intersecao']+=1
            elif e['tokens']:
                summary_by_tp['ids_sem_intersecao_observada']+=1
            if len(target_pids)>1 or len(e['tokens'])>1:
                summary_by_tp['ligacao_ambigua_por_multiplos_ids']+=1
            if len(e['tokens'])==1 and len(target_pids)==1:
                summary_by_tp['par_com_id_unico_em_ambos']+=1
        starts=e['starts']
        prev_end=auth_end.get(parent)
        if starts and prev_end:
            gap=(min(starts)-prev_end).days
            summary_by_tp['refs_com_datas_validas_em_ambos']+=1
            if gap>0: summary_by_tp['inicio_filha_apos_fim_pai']+=1
            elif gap==0: summary_by_tp['inicio_filha_no_fim_pai']+=1
            else: summary_by_tp['inicio_filha_antes_fim_pai']+=1
        for tp in e['types']:
            summary_by_tp[f'referencia_em_linha_tp{tp}']+=1
    write(OUT/'resumo.csv',[{'indicador':k,'valor':v} for k,v in sorted(counts.items())])
    write(OUT/'referencias_apac_agregadas.csv',[{'indicador':k,'valor':v} for k,v in sorted(summary_by_tp.items())])
    write(OUT/'distribuicao_linhas_por_tipo_apac.csv',[{'AP_TPAPAC':tp,'linhas':n} for (tp,_),n in sorted(by_tp.items())])
    print('Concluído:',OUT)
    print('Resumo:',dict(counts))
    print('Referências:',dict(summary_by_tp))
if __name__=='__main__': main()
