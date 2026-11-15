"""Reproduz verificações dos CSVs SIH/TabNet sem alterar arquivos de origem.

Uso: python3 Trabalho-final/Dados/auditar_contagens_sih_csv.py

Este script confere CSVs derivados e os hashes listados no manifesto SIH.
Ele não lê DBC e, portanto, não reproduz a extração a partir dos microdados brutos.
"""
from collections import Counter
import csv
import hashlib
from pathlib import Path


AUDITORIA = Path(__file__).resolve().parent
DADOS = AUDITORIA.parent
SIH_DERIVADOS = DADOS / "02_derivados_preliminares" / "SIH"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream, delimiter=";"))


micro = read_csv(SIH_DERIVADOS / "sih_n18_microdados_uf_ano_mes_2024_2025.csv")
aggregate = read_csv(SIH_DERIVADOS / "sih_n18_uf_mes_admissao_2024_2025.csv")
tabnet = read_csv(SIH_DERIVADOS / "sih_insuficiencia_renal_n17_n19_uf_mes_2024_2025_analitico.csv")

assert all(row["DIAG_PRINC"].startswith("N18") for row in micro)
assert all("20240101" <= row["DATA_INTERNACAO"] <= "20251231" for row in micro)
deaths = sum(row["MORTE_HOSPITALAR"] == "1" for row in micro)
assert sum(int(row["AIH_N18_DIAGNOSTICO_PRINCIPAL"]) for row in aggregate) == len(micro)
assert sum(int(row["OBITOS_HOSPITALARES"]) for row in aggregate) == deaths

abbr = {
    "AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas",
    "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo",
    "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná",
    "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul", "RO": "Rondônia",
    "RR": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo",
    "SE": "Sergipe", "TO": "Tocantins",
}
month_number = dict(zip(
    ("Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez").split(),
    ("01 02 03 04 05 06 07 08 09 10 11 12").split(),
))
monthly = Counter((abbr[row["UF"]], row["ANO_MES_INTERNACAO"]) for row in micro)
month_columns = [key for key in tabnet[0] if key[:4] in ("2024", "2025")]
comparisons, missing = [], []
for row in tabnet:
    for key in month_columns:
        value = row[key].strip()
        if not value:
            missing.append((row["UF"], key))
            continue
        year, month = key.split("/")
        n18 = monthly[(row["UF"], year + month_number[month])]
        comparisons.append((n18, int(value)))

manifest = DADOS / "01_fontes_originais" / "SIH" / "SIH_RD_2024_2025_bruto" / "SHA256SUMS.txt"
verified = failed = absent = 0
for line in manifest.read_text().splitlines():
    expected, relative = line.split(None, 1)
    path = manifest.parent / relative.strip().lstrip("* ")
    if not path.is_file():
        absent += 1
    elif hashlib.sha256(path.read_bytes()).hexdigest() == expected:
        verified += 1
    else:
        failed += 1

print(f"CSV microdados: {len(micro)} linhas; MORTE=1: {deaths}")
print(f"CSV agregado: {len(aggregate)} células UF/mês; contagem e óbitos conferem")
print(f"TabNet: total informado por UF: {sum(int(r['Total observado 2024-2025']) for r in tabnet)}")
print(f"Células comparáveis: {len(comparisons)}; N18 maior que N17–N19: {sum(a > b for a, b in comparisons)}")
print(f"Células TabNet vazias: {missing}")
print(f"Manifesto: {verified} hashes corretos; {failed} divergentes; {absent} arquivos ausentes")
print("Nota: conferência dos CSVs e integridade dos arquivos; não extrai nem reconcilia DBC.")
