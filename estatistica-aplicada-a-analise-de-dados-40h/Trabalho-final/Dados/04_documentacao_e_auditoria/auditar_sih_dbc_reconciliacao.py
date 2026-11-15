"""Reextrai N18 dos DBCs locais e audita versões sem tocar nos arquivos atuais.

Execute na raiz do projeto com:
    .venv-sih-audit/bin/python Trabalho-final/Dados/04_documentacao_e_auditoria/auditar_sih_dbc_reconciliacao.py

Cada execução cria uma pasta exclusiva em Dados/02_derivados_preliminares/SIH.
N_AIH é mantido apenas em memória; não é exportado nos resultados.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
import csv
import hashlib
import re
import stat
import sys
import time

import dbc_reader
from dbc_reader import DbcReader

if sys.platform == "darwin":
    _blast = Path(dbc_reader.__file__).parent / "bin" / "blast-dbf-darwin"
    if _blast.is_file() and not (_blast.stat().st_mode & stat.S_IXUSR):
        _blast.chmod(_blast.stat().st_mode | stat.S_IXUSR)


HERE = Path(__file__).resolve()
TRABALHO = HERE.parents[2]
DADOS = TRABALHO / "Dados"
DBC_DIR = DADOS / "01_fontes_originais/SIH/SIH_RD_2024_2025_bruto"
DERIVADOS = DADOS / "02_derivados_preliminares/SIH"
CSV_N18 = DERIVADOS / "sih_n18_microdados_uf_ano_mes_2024_2025.csv"
CSV_TABNET = DERIVADOS / "sih_insuficiencia_renal_n17_n19_uf_mes_2024_2025_analitico.csv"
MANIFEST = DBC_DIR / "SHA256SUMS.txt"

PATTERN = re.compile(r"^RD(?P<uf>[A-Z]{2})(?P<yy>\d{2})(?P<mm>\d{2})$", re.I)
UF_NAMES = {
    "11": "Rondônia", "12": "Acre", "13": "Amazonas", "14": "Roraima",
    "15": "Pará", "16": "Amapá", "17": "Tocantins", "21": "Maranhão",
    "22": "Piauí", "23": "Ceará", "24": "Rio Grande do Norte", "25": "Paraíba",
    "26": "Pernambuco", "27": "Alagoas", "28": "Sergipe", "29": "Bahia",
    "31": "Minas Gerais", "32": "Espírito Santo", "33": "Rio de Janeiro",
    "35": "São Paulo", "41": "Paraná", "42": "Santa Catarina",
    "43": "Rio Grande do Sul", "50": "Mato Grosso do Sul", "51": "Mato Grosso",
    "52": "Goiás", "53": "Distrito Federal",
}
UF_CODES = {name: code for code, name in UF_NAMES.items()}
UF_ABBR_CODES = {
    "AC": "12", "AL": "27", "AM": "13", "AP": "16", "BA": "29", "CE": "23",
    "DF": "53", "ES": "32", "GO": "52", "MA": "21", "MG": "31", "MS": "50",
    "MT": "51", "PA": "15", "PB": "25", "PE": "26", "PI": "22", "PR": "41",
    "RJ": "33", "RN": "24", "RO": "11", "RR": "14", "RS": "43", "SC": "42",
    "SE": "28", "SP": "35", "TO": "17",
}


def uf_code_from_abbr(abbr):
    return UF_ABBR_CODES[abbr.upper()]
MONTHS = dict(zip("Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez".split(),
                  "01 02 03 04 05 06 07 08 09 10 11 12".split()))
COLS = [
    "UF", "COMPETENCIA_PROCESSAMENTO", "MUNICIPIO_RESIDENCIA", "MUNICIPIO_INTERNAÇÃO",
    "ANO_MES_INTERNACAO", "DATA_INTERNACAO", "DATA_SAIDA", "DIAG_PRINC",
    "PROCEDIMENTO_REALIZADO", "MORTE_HOSPITALAR", "DIAS_PERMANENCIA",
    "IDADE", "COD_IDADE", "SEXO", "RACA_COR", "VALOR_TOTAL",
]
VERSION_FIELDS = (
    "ident", "diag", "dt_inter", "dt_saida", "mun_res", "mun_mov", "morte",
    "proc", "dias", "idade", "cod_idade", "sexo", "raca", "valor",
)


def value(v):
    return "" if v is None else str(v).strip()


def code(v, width=None):
    s = value(v)
    if s.endswith(".0") and s[:-2].isdigit():
        s = s[:-2]
    return s.zfill(width) if width and s.isdigit() else s


def date8(v):
    s = re.sub(r"\D", "", value(v))
    if len(s) != 8:
        return ""
    try:
        datetime.strptime(s, "%Y%m%d")
    except ValueError:
        return ""
    return s


def money(v):
    s = value(v).replace(",", ".")
    if not s:
        return ""
    try:
        return f"{Decimal(s):.2f}"
    except InvalidOperation:
        return s


def metadata(path):
    m = PATTERN.match(path.stem)
    if not m:
        return None
    month = int(m["mm"])
    if month not in range(1, 13):
        raise ValueError(path.name)
    return {"path": path, "uf": m["uf"].upper(),
            "comp": f"20{m['yy']}{month:02d}"}


def files():
    result = [metadata(p) for p in DBC_DIR.glob("*.dbc")]
    result = sorted((x for x in result if x), key=lambda x: (x["comp"], x["uf"]))
    assert len(result) == 648, f"Esperados 648 DBCs; encontrados {len(result)}"
    assert len({(x["uf"], x["comp"]) for x in result}) == 648
    return result


def rows(path):
    # DbcReader 0.1.2 aceita caminho; usar file object falha nesta versão.
    yield from DbcReader(str(path))


def project(row, uf, comp):
    dt = date8(row.get("DT_INTER"))
    return dict(zip(COLS, [
        uf, comp, code(row.get("MUNIC_RES"), 6), code(row.get("MUNIC_MOV"), 6),
        dt[:6] if dt else "", dt, date8(row.get("DT_SAIDA")),
        code(row.get("DIAG_PRINC")).upper(), code(row.get("PROC_REA"), 10),
        code(row.get("MORTE")), code(row.get("DIAS_PERM")), code(row.get("IDADE")),
        code(row.get("COD_IDADE")), code(row.get("SEXO")), code(row.get("RACA_COR"), 2),
        money(row.get("VAL_TOT")),
    ]))


def signature(row):
    return tuple(row[c] for c in COLS)


def local_uf(mun):
    prefix = code(mun)[:2]
    return prefix if prefix in UF_NAMES else ""


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def write_csv(path, records, fields):
    with path.open("x", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(records)


def check_manifest():
    results = []
    for line in MANIFEST.read_text().splitlines():
        if not line.strip():
            continue
        expected, rel = line.split(maxsplit=1)
        path = MANIFEST.parent / rel.strip().lstrip("* ")
        h = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "ausente"
        results.append({"arquivo": rel.strip(), "sha256_esperado": expected,
                        "sha256_observado": h,
                        "status": "ok" if h == expected.lower() else "erro"})
    if not all(r["status"] == "ok" for r in results):
        raise RuntimeError("Falha no manifesto SHA-256; consulte manifest_check.csv")
    return results


def tabnet_cells(tabnet):
    cells, missing = {}, []
    for row in tabnet:
        uf = UF_CODES.get(row["UF"].strip())
        if not uf:
            raise ValueError(f"UF TabNet desconhecida: {row['UF']}")
        for label, text in row.items():
            if not re.fullmatch(r"20\d\d/(Jan|Fev|Mar|Abr|Mai|Jun|Jul|Ago|Set|Out|Nov|Dez)", label):
                continue
            year, month = label.split("/")
            cell = (uf, year + MONTHS[month])
            text = (text or "").strip()
            if text in ("", "-"):
                missing.append(cell)
            else:
                cells[cell] = int(text)
    return cells, missing


def main():
    dbc_files = files()
    prelim = read_csv(CSV_N18)
    tabnet = read_csv(CSV_TABNET)
    assert len(prelim) == 368_917
    manifest_results = check_manifest()
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = DERIVADOS / f"auditoria_sih_dbc_reconciliacao_{run_id}"
    out.mkdir(exist_ok=False)
    write_csv(out / "manifest_check.csv", manifest_results,
              ["arquivo", "sha256_esperado", "sha256_observado", "status"])

    counts = Counter()
    by_file = Counter()
    ident_n18 = Counter()
    raw_by_file = Counter()
    raw_by_local = Counter()
    ident1_local = Counter()
    candidate_ids = set()
    id_occurrences = Counter()
    id_comp = defaultdict(set)
    id_file_ufs = defaultdict(set)
    dbc_signatures = Counter()
    selected_rows = []
    t0 = time.time()

    for i, info in enumerate(dbc_files, 1):
        for row in rows(info["path"]):
            counts["linhas_dbc"] += 1
            diag = code(row.get("DIAG_PRINC")).upper()
            if not diag.startswith("N18"):
                continue
            counts["n18"] += 1
            dt = date8(row.get("DT_INTER"))
            if not dt:
                counts["n18_data_invalida"] += 1
                continue
            if not "20240101" <= dt <= "20251231":
                counts["n18_fora_periodo"] += 1
                continue
            counts["n18_periodo"] += 1
            ident = code(row.get("IDENT")) or "(vazio)"
            ident_n18[ident] += 1
            by_file[(info["comp"], info["uf"])] += 1
            proj = project(row, info["uf"], info["comp"])
            dbc_signatures[signature(proj)] += 1
            selected_rows.append({**proj, "IDENT": ident, "UF_ZI": code(row.get("UF_ZI")),
                                  "DBC_ORIGEM": info["path"].name})
            aih = code(row.get("N_AIH"))
            if aih:
                candidate_ids.add(aih)
                id_occurrences[aih] += 1
                id_comp[aih].add(info["comp"])
                id_file_ufs[aih].add(info["uf"])
            else:
                counts["n18_sem_n_aih"] += 1
            mes = dt[:6]
            raw_by_file[(uf_code_from_abbr(info["uf"]), mes)] += 1
            local = local_uf(row.get("MUNIC_MOV"))
            if local:
                raw_by_local[(local, mes)] += 1
                if ident == "1":
                    ident1_local[(local, mes)] += 1
                if local != uf_code_from_abbr(info["uf"]):
                    counts["uf_arquivo_diferente_uf_local"] += 1
            else:
                counts["uf_local_nao_derivavel_municip_mov"] += 1
        if i % 50 == 0 or i == len(dbc_files):
            print(f"Primeira passagem: {i}/648 DBCs; {counts['linhas_dbc']:,} registros; {time.time()-t0:.1f}s", flush=True)

    # Nova extração detalhada não sobrescreve o CSV atual; contém N_AIH/IDENT para auditoria.
    write_csv(out / "n18_reextraido_linhas.csv", selected_rows,
              COLS + ["IDENT", "UF_ZI", "DBC_ORIGEM"])
    del selected_rows

    csv_sig = Counter(signature({c: r.get(c, "").strip() for c in COLS}) for r in prelim)
    only_csv, only_dbc = csv_sig - dbc_signatures, dbc_signatures - csv_sig
    diff_rows = []
    for side, counter in (("somente_csv_preliminar", only_csv), ("somente_reextracao", only_dbc)):
        for sig, n in counter.items():
            diff_rows.append({**dict(zip(COLS, sig)), "lado": side, "contagem": n})
    write_csv(out / "divergencias_csv_vs_dbc.csv", diff_rows, COLS + ["lado", "contagem"])

    # Segunda passagem: snapshots de todos os N_AIH candidatos, inclusive versões fora de N18.
    versions = defaultdict(list)
    seen_candidate_rows = 0
    for i, info in enumerate(dbc_files, 1):
        for row in rows(info["path"]):
            aih = code(row.get("N_AIH"))
            if not aih or aih not in candidate_ids:
                continue
            seen_candidate_rows += 1
            # Fingerprint all analytical/version fields, including processing and territory.
            vals = (
                info["comp"], info["uf"], code(row.get("UF_ZI")), code(row.get("IDENT")),
                code(row.get("DIAG_PRINC")).upper(), date8(row.get("DT_INTER")),
                date8(row.get("DT_SAIDA")), code(row.get("MUNIC_RES"), 6),
                code(row.get("MUNIC_MOV"), 6), code(row.get("MORTE")),
                code(row.get("PROC_REA"), 10), code(row.get("DIAS_PERM")),
                code(row.get("IDADE")), code(row.get("COD_IDADE")), code(row.get("SEXO")),
                code(row.get("RACA_COR"), 2), money(row.get("VAL_TOT")),
            )
            versions[aih].append(vals)
        if i % 50 == 0 or i == len(dbc_files):
            print(f"Segunda passagem: {i}/648 DBCs; {seen_candidate_rows:,} linhas dos N_AIH candidatos; {time.time()-t0:.1f}s", flush=True)

    # Aggregate version patterns. Avoid exporting authorization numbers.
    version_stats = Counter()
    changes = Counter()
    version_counts_by_aihs = Counter()
    scenarios = {
        "linhas N18 por UF do arquivo/mês": raw_by_file,
        "linhas N18 por UF local de MUNIC_MOV/mês": raw_by_local,
        "linhas N18 IDENT=1 por UF local/mês": ident1_local,
    }
    for aih, snapshots in versions.items():
        ordered = sorted(snapshots, key=lambda x: x[0])
        first_comp, last_comp = ordered[0][0], ordered[-1][0]
        first = [x for x in ordered if x[0] == first_comp]
        last = [x for x in ordered if x[0] == last_comp]
        distinct_payloads = {x[1:] for x in snapshots}
        comps = {x[0] for x in snapshots}
        version_stats["aih_candidata"] += 1
        version_counts_by_aihs[len(comps)] += 1
        if len(comps) > 1:
            version_stats["aih_em_multiplas_competencias"] += 1
        if len(distinct_payloads) > 1:
            version_stats["aih_payload_alterado_entre_snapshots"] += 1
        if len(first) > 1:
            version_stats["aih_empate_primeira_competencia"] += 1
        if len(last) > 1:
            version_stats["aih_empate_ultima_competencia"] += 1
        if len(first) == 1 and len(last) == 1:
            a, b = first[0], last[0]
            labels = ("competencia", "uf_arquivo", "UF_ZI", "IDENT", "DIAG_PRINC", "DT_INTER",
                      "DT_SAIDA", "MUNIC_RES", "MUNIC_MOV", "MORTE", "PROC_REA", "DIAS_PERM",
                      "IDADE", "COD_IDADE", "SEXO", "RACA_COR", "VAL_TOT")
            for idx, label in enumerate(labels, start=0):
                if a[idx] != b[idx]:
                    changes[label] += 1
            if a[4].startswith("N18") != b[4].startswith("N18"):
                changes["status_diag_N18_mudou"] += 1
            in_a = bool(a[5] and "20240101" <= a[5] <= "20251231")
            in_b = bool(b[5] and "20240101" <= b[5] <= "20251231")
            if in_a != in_b:
                changes["status_data_periodo_mudou"] += 1

    tab_cells, missing_cells = tabnet_cells(tabnet)
    comparison_rows = []
    for name, counts_by_cell in scenarios.items():
        vals = [(counts_by_cell.get(k, 0), v) for k, v in tab_cells.items()]
        errors = [abs(a-b) for a, b in vals]
        comparison_rows.append({
            "cenario": name, "total_n18_nas_celulas_observadas": sum(a for a, _ in vals),
            "total_tabnet_n17_n19_observado": sum(b for _, b in vals),
            "celulas_comparadas": len(vals), "n18_maior_que_tabnet": sum(a>b for a, b in vals),
            "celulas_iguais": sum(a==b for a, b in vals),
            "desvio_absoluto_total": sum(errors),
            "desvio_absoluto_medio": round(sum(errors)/len(errors), 3) if errors else "",
        })
    write_csv(out / "comparacao_tabnet_por_uf_mes.csv", comparison_rows, list(comparison_rows[0]))

    cell_rows = []
    for uf_month, broad in tab_cells.items():
        uf, month = uf_month
        for name, counts_by_cell in scenarios.items():
            n = counts_by_cell.get(uf_month, 0)
            cell_rows.append({"cenario": name, "UF": UF_NAMES[uf], "codigo_UF": uf,
                              "ano_mes": month, "n18": n, "n17_n19_tabnet": broad,
                              "diferenca": n-broad, "n18_acima": int(n>broad)})
    write_csv(out / "celulas_tabnet_uf_mes.csv", cell_rows,
              ["cenario", "UF", "codigo_UF", "ano_mes", "n18", "n17_n19_tabnet", "diferenca", "n18_acima"])
    write_csv(out / "celulas_tabnet_ausentes.csv",
              [{"codigo_UF": uf, "UF": UF_NAMES[uf], "ano_mes": month} for uf, month in missing_cells],
              ["codigo_UF", "UF", "ano_mes"])
    write_csv(out / "contagens_por_dbc.csv",
              [{"competencia_processamento": comp, "uf_arquivo": uf,
                "linhas_n18_periodo": by_file[(comp, uf)]}
               for comp, uf in sorted((x["comp"], x["uf"]) for x in dbc_files)],
              ["competencia_processamento", "uf_arquivo", "linhas_n18_periodo"])
    write_csv(out / "distribuicao_ident.csv",
              [{"IDENT": k, "linhas_n18_periodo": v} for k, v in sorted(ident_n18.items())],
              ["IDENT", "linhas_n18_periodo"])
    write_csv(out / "distribuicao_repeticoes_n_aih.csv",
              [{"competencias_com_registro": n, "n_aih": c} for n, c in sorted(version_counts_by_aihs.items())],
              ["competencias_com_registro", "n_aih"])
    write_csv(out / "alteracoes_primeira_ultima_versao.csv",
              [{"campo": k, "n_aih_com_alteracao": v} for k, v in sorted(changes.items())],
              ["campo", "n_aih_com_alteracao"])

    summary = [
        {"indicador": k, "valor": v} for k, v in sorted(counts.items())
    ] + [
        {"indicador": "linhas_csv_preliminar", "valor": len(prelim)},
        {"indicador": "diferenca_nova_extracao_menos_csv", "valor": counts["n18_periodo"]-len(prelim)},
        {"indicador": "diferenca_nova_extracao_menos_rotina_historica_368905", "valor": counts["n18_periodo"]-368905},
        {"indicador": "assinaturas_somente_csv_com_multiplicidade", "valor": sum(only_csv.values())},
        {"indicador": "assinaturas_somente_reextracao_com_multiplicidade", "valor": sum(only_dbc.values())},
        {"indicador": "assinaturas_divergentes_csv_vs_reextracao", "valor": len(diff_rows)},
        {"indicador": "n_aih_distintos_n18_periodo", "valor": len(candidate_ids)},
        {"indicador": "n_aih_com_repeticao_no_recorte", "valor": sum(n > 1 for n in id_occurrences.values())},
        {"indicador": "ocorrencias_excedentes_n_aih_no_recorte", "valor": sum(n-1 for n in id_occurrences.values() if n > 1)},
        {"indicador": "n_aih_com_uf_arquivo_multipla", "valor": sum(len(v)>1 for v in id_file_ufs.values())},
        {"indicador": "n_aih_candidatos_lidos_segunda_passagem", "valor": seen_candidate_rows},
        {"indicador": "n_aih_candidatos", "valor": version_stats["aih_candidata"]},
        {"indicador": "hashes_manifesto_ok", "valor": len(manifest_results)},
        {"indicador": "celulas_tabnet_ausentes", "valor": len(missing_cells)},
    ] + [{"indicador": f"version_{k}", "valor": v} for k, v in sorted(version_stats.items())]
    write_csv(out / "resumo.csv", summary, ["indicador", "valor"])
    print("Saídas novas:", out)
    print("Resumo:", {r["indicador"]: r["valor"] for r in summary})
    print("IDENT:", dict(ident_n18))
    print("Versões first-last:", dict(changes))
    print("Comparação TabNet:", comparison_rows)


if __name__ == "__main__":
    main()
