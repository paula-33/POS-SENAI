"""Valida e transforma a coleta TabNet versionada de 15/11/2026.

Leia docs/Trabalho-final/Dados/04_documentacao_e_auditoria/ATUALIZACAO_SIH_SIA_2026-11-15.md antes de executar. Não baixa dados,
não altera fontes nem saídas antigas. Requer pandas e beautifulsoup4.
Uso: python atualizar_bases_tabnet.py --saida /tmp/atualizacao-validada
"""
import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup

MESES = {m: f'{i:02d}' for i, m in enumerate(
    ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], 1)}
PROJETO = Path(__file__).resolve().parents[2]
RAW = PROJETO / 'Dados/01_fontes_originais/TabNet/atualizacao_sih_sia_20261115'


def ler_lote(csv_path, html_path, ano_processamento):
    """Lê um lote disjunto; valida totais e a legenda oficial do hífen."""
    texto = BeautifulSoup(Path(html_path).read_text(encoding='latin1'), 'html.parser').get_text(' ', strip=True)
    hifen_zero = 'Dado numérico igual a 0 não resultante de arredondamento.' in texto

    def numero(token):
        token = token.strip()
        if token == '-' and hifen_zero:
            return 0
        if not re.fullmatch(r'\d+(?:\.\d{3})*', token):
            raise ValueError(f'Valor não reconhecido ou ausência sem semântica confirmada: {token!r}')
        return int(token.replace('.', ''))

    linhas = list(csv.reader(io.StringIO(Path(csv_path).read_text(encoding='latin1')), delimiter=';'))
    inicio = next(i for i, r in enumerate(linhas) if r and r[0] in ['UF', 'Unidade da Federação'])
    cabecalho = linhas[inicio]
    if cabecalho[-1] != 'Total':
        raise ValueError('Cabeçalho sem total oficial')
    meses = []
    for coluna in cabecalho[1:-1]:
        ano, mes = coluna.split('/')
        meses.append(f'{ano}-{MESES[mes]}')
    registros, soma, totais = [], [0] * len(meses), []
    ufs = set()
    for linha in linhas[inicio + 1:]:
        if not linha:
            continue
        rotulo = linha[0].strip()
        if not re.match(r'^\d{2} ', rotulo) and rotulo.upper() != 'TOTAL':
            continue
        if len(linha) != len(cabecalho):
            raise ValueError('Número de colunas divergente')
        valores = [numero(v) for v in linha[1:-1]]
        if sum(valores) != numero(linha[-1]):
            raise ValueError(f'Total da linha divergente: {rotulo}')
        if rotulo.upper() == 'TOTAL':
            totais.append(valores)
            continue
        codigo = rotulo[:2]
        if codigo in ufs:
            raise ValueError(f'UF repetida: {codigo}')
        ufs.add(codigo)
        soma = [a + b for a, b in zip(soma, valores)]
        if codigo == '00':
            if any(valores):
                raise ValueError('Ignorado/exterior não nulo exige tratamento explícito')
            continue
        for mes, valor, token in zip(meses, valores, linha[1:-1]):
            registros.append({'codigo_uf': codigo, 'uf': rotulo[3:], 'ano_mes': mes,
                              'valor': valor, 'lote_processamento': ano_processamento,
                              'zero_por_hifen': int(token.strip() == '-')})
    if len(totais) != 1 or totais[0] != soma:
        raise ValueError('Total mensal oficial diverge da soma das UFs')
    return pd.DataFrame(registros)


def agregar_lotes(lotes, inicio, fim):
    """Soma apresentações em anos distintos, mantendo o mês de atendimento."""
    dados = pd.concat(lotes, ignore_index=True)
    if dados.duplicated(['lote_processamento', 'codigo_uf', 'ano_mes']).any():
        raise ValueError('Sobreposição de lotes de processamento')
    dados = dados[dados.ano_mes.between(inicio, fim)]
    resultado = dados.groupby(['codigo_uf', 'uf', 'ano_mes'], as_index=False).agg(
        valor=('valor', 'sum'), lotes_com_coluna=('lote_processamento', 'nunique'),
        parcelas_zero_por_hifen=('zero_por_hifen', 'sum'))
    resultado['status'] = 'observado'
    return resultado.sort_values(['codigo_uf', 'ano_mes']).reset_index(drop=True)


def historico(sistema):
    if sistema == 'sih':
        p = PROJETO / 'Dados/02_derivados_preliminares/SIH/sih_insuficiencia_renal_n17_n19_uf_mes_2024_2025_analitico.csv'
        d = pd.read_csv(p, sep=';', encoding='utf-8-sig', dtype={'Código UF': str})
        d['codigo_uf'] = d['Código UF']
    else:
        p = PROJETO / 'Dados/02_derivados_preliminares/SIA/hemodialise_sia_sus_uf_mes_2024_2025.csv'
        d = pd.read_csv(p, sep=';', encoding='utf-8-sig')
        d['codigo_uf'] = d.UF.str[:2]
    d = d[d.codigo_uf.str.fullmatch(r'\d{2}', na=False)]
    colunas = [c for c in d if re.fullmatch(r'202[45]/[A-Za-z]{3}', c)]
    longo = d.melt(id_vars='codigo_uf', value_vars=colunas, var_name='mes', value_name='anterior')
    longo['ano_mes'] = longo.mes.map(lambda c: c[:4] + '-' + MESES[c[5:]])
    return longo[['codigo_uf', 'ano_mes', 'anterior']]


def executar(saida):
    manifesto = json.loads((RAW / 'manifesto_coleta.json').read_text())
    for nome, esperado in manifesto['sha256'].items():
        if hashlib.sha256((RAW / nome).read_bytes()).hexdigest() != esperado:
            raise ValueError(f'Hash divergente: {nome}')
    saida.mkdir(parents=True, exist_ok=False)
    validacoes, series, comparacoes = [], [], []
    for sistema, inicio, esperado in [('sih', '2024-01', 648), ('sia', '2023-01', 972)]:
        lotes = [ler_lote(RAW / c['arquivo_csv'], RAW / c['arquivo_html'], c['ano_processamento'])
                 for c in manifesto['consultas'] if c['sistema'] == sistema]
        base = agregar_lotes(lotes, inicio, '2025-12')
        meses = pd.period_range(inicio, '2025-12', freq='M').astype(str)
        ufs = set(historico('sih').codigo_uf)
        grade = {(u, m) for u in ufs for m in meses}
        if set(zip(base.codigo_uf, base.ano_mes)) != grade or len(base) != esperado:
            raise ValueError(f'Grade UF-mês incompleta ou inesperada: {sistema}')
        base.to_csv(saida / f'{sistema}_uf_mes.csv', index=False)
        parcelas = pd.concat(lotes, ignore_index=True)
        parcelas = parcelas[parcelas.ano_mes.between(inicio, '2025-12')]
        parcelas.to_csv(saida / f'{sistema}_contribuicoes_processamento.csv', index=False)
        # Comparação com o recorte de processamento usado na extração histórica.
        corte = agregar_lotes([p for p in lotes if p.lote_processamento.iloc[0] <= 2025], inicio, '2025-12')
        antigo = historico(sistema)
        comp = base.merge(antigo, on=['codigo_uf', 'ano_mes'], how='inner', validate='one_to_one')
        comp = comp.merge(corte[['codigo_uf', 'ano_mes', 'valor']].rename(columns={'valor': 'corte_processamento_2025'}), on=['codigo_uf', 'ano_mes'], validate='one_to_one')
        comp = comp.rename(columns={'valor': 'atualizado'})
        comp['diferenca'] = comp.atualizado - comp.anterior
        comp['acrescimo_processado_2026'] = comp.atualizado - comp.corte_processamento_2025
        comp['historico_ausente'] = comp.anterior.isna()
        comp['coincide_corte_2025'] = comp.anterior.eq(comp.corte_processamento_2025)
        comp.to_csv(saida / f'{sistema}_comparacao_2024_2025.csv', index=False)
        comp['sistema'] = sistema
        comparacoes.append(comp)
        serie = base.groupby('ano_mes', as_index=False).agg(total=('valor', 'sum'), ufs=('codigo_uf', 'nunique'))
        serie['sistema'] = sistema
        series.append(serie)
        validacoes.append({'sistema': sistema, 'linhas': len(base), 'ufs': len(ufs), 'meses': len(meses),
                           'ausencias': int(base.valor.isna().sum()), 'duplicidades': int(base.duplicated(['codigo_uf', 'ano_mes']).sum()),
                           'soma': int(base.valor.sum()), 'celulas_comparadas_historico': len(comp),
                           'historico_ausente': int(comp.anterior.isna().sum()),
                           'coincidencias_corte_2025': int(comp.coincide_corte_2025.sum()),
                           'celulas_revisadas_observadas': int((comp.diferenca.ne(0) & comp.anterior.notna()).sum())})
    pd.concat(series).to_csv(saida / 'series_mensais_brasil.csv', index=False)
    pd.concat(comparacoes).to_csv(saida / 'comparacoes_2024_2025.csv', index=False)
    pd.DataFrame(validacoes).to_csv(saida / 'validacoes.csv', index=False)
    (saida / 'manifesto_coleta.json').write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + '\n')
    arquivos = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(saida.iterdir()) if p.is_file()}
    (saida / 'manifesto_sha256.json').write_text(json.dumps(arquivos, ensure_ascii=False, indent=2) + '\n')
    print(pd.DataFrame(validacoes).to_string(index=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saida', type=Path, required=True, help='Diretório novo; recusa sobrescrita')
    executar(parser.parse_args().saida)
