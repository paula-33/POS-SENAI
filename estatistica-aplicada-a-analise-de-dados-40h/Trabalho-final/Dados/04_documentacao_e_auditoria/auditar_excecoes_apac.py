"""Resume excecoes APAC sem exportar identificadores pessoais ou de autorizacao."""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path
import csv
import hashlib
import re
import stat

import dbc_reader
from dbc_reader import DbcReader

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "Dados/01_fontes_originais/APAC/APAC_ATD_2024_2025_bruto"
OUT = ROOT / "Dados/02_derivados_preliminares/APAC/auditoria_excecoes_20261105_v2"
if __import__("sys").platform == "darwin":
    blast = Path(dbc_reader.__file__).parent / "bin" / "blast-dbf-darwin"
    if blast.is_file() and not (blast.stat().st_mode & stat.S_IXUSR):
        blast.chmod(blast.stat().st_mode | stat.S_IXUSR)


def norm(v):
    return "" if v is None else str(v).strip()


def date_value(v):
    s = re.sub(r"\D", "", norm(v))
    if len(s) != 8 or s == "00000000":
        return None
    try:
        return date(int(s[:4]), int(s[4:6]), int(s[6:8]))
    except ValueError:
        return None


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=False)
    files = sorted(RAW.glob("ATD*.dbc"))
    assert len(files) == 648, f"Esperados 648 DBCs, encontrados {len(files)}"
    per_file, totals, types, procs, date_years, date_by_comp, future_values = [], Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
    manifest = []
    for i, path in enumerate(files, 1):
        c = Counter()
        for row in DbcReader(str(path)):
            c["registros"] += 1
            tp, proc = norm(row.get("AP_TPAPAC")), norm(row.get("AP_PRIPAL"))
            types[tp or "(vazio)"] += 1
            procs[proc or "(vazio)"] += 1
            if tp == "4" or proc == "":
                c["tp4_ou_procedimento_vazio"] += 1
            for field in ("ATD_DTPDR", "ATD_DTCLI"):
                raw = norm(row.get(field))
                d = date_value(raw)
                if raw and d is None:
                    c[f"{field}_data_invalida"] += 1
                elif d and d > date(2025, 12, 31):
                    c[f"{field}_apos_2025"] += 1
                    date_years[(field, str(d.year))] += 1
                    date_by_comp[(field, norm(row.get("AP_CMP"))[:6])] += 1
                    future_values[(field, raw)] += 1
        comp = path.stem[-4:]
        uf = path.stem[3:5]
        per_file.append({"arquivo": path.name, "uf": uf, "competencia_arquivo": comp,
                         **{k: c[k] for k in ("registros", "tp4_ou_procedimento_vazio",
                             "ATD_DTPDR_apos_2025", "ATD_DTCLI_apos_2025",
                             "ATD_DTPDR_data_invalida", "ATD_DTCLI_data_invalida")}})
        totals.update(c)
        manifest.append({"arquivo": path.name, "sha256": sha(path), "bytes": path.stat().st_size})
        if i % 54 == 0:
            print(f"Lidos {i}/648 DBCs", flush=True)
    write(OUT / "resumo_por_arquivo.csv", per_file)
    write(OUT / "dominios_tp_apac.csv", [{"valor": k, "registros": v} for k, v in sorted(types.items())])
    write(OUT / "dominios_procedimento_principal.csv", [{"valor": k, "registros": v} for k, v in sorted(procs.items())])
    write(OUT / "datas_futuras_por_ano.csv", [{"campo": k[0], "ano": k[1], "registros": v} for k, v in sorted(date_years.items())])
    write(OUT / "datas_futuras_por_competencia_apac.csv", [{"campo": k[0], "AP_CMP": k[1], "registros": v} for k, v in sorted(date_by_comp.items())])
    write(OUT / "valores_datas_futuras.csv", [{"campo": k[0], "valor_data": k[1], "registros": v} for k, v in sorted(future_values.items())])
    write(OUT / "hashes_apac.csv", manifest)
    write(OUT / "resumo.csv", [{"indicador": k, "valor": v} for k, v in sorted(totals.items())])
    print(f"Concluído: {len(files)} arquivos, {totals['registros']} registros; saída: {OUT}")


def write(path, rows):
    rows = list(rows)
    fields = list(rows[0]) if rows else []
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
