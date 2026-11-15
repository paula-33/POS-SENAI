# Organização da pasta Dados

A cópia de segurança anterior à reorganização está ao lado desta pasta, em `../Dados_backup_antes_reorganizacao_2026-10-25/`. Nenhum arquivo de dados foi apagado. O inventário com caminho, tamanho e SHA-256 de cada arquivo está em `00_inventario/inventario_arquivos.csv`.

## Pastas

- `01_fontes_originais/`: arquivos obtidos das fontes oficiais, preservados sem tratamento.
- `02_derivados_preliminares/`: tabelas exportadas, transformadas ou agregadas que ainda precisam das validações descritas na documentação.
- `03_bases_analiticas/`: produtos derivados e validados para escopo analítico específico. A base descritiva territorial SIA/SIH/IBGE está em `03_bases_analiticas/descritiva_territorial_2024_2025/`; ela não é uma coorte individual nem base de efetividade.
- `04_documentacao_e_auditoria/`: notas de leitura, decisões, pendências e script de auditoria.
- `00_inventario/`: inventário de arquivos.

## Conteúdo por fonte

- SIH, APAC, CNES, IBGE, SIGTAP e captura TabNet originais estão separados em suas subpastas de `01_fontes_originais/`.
- Os CSVs derivados estão separados por fonte em `02_derivados_preliminares/`.
- A tabela TabNet de N17–N19 permanece preliminar; sua exportação precisa ser validada. Os CSVs N18 do SIH também permanecem preliminares até reconciliação e definição da regra de duplicidade.
- Os arquivos CNES descrevem cadastro de uma competência e não são medida confirmada de capacidade operacional.
- O arquivo SIA de hemodiálise é produção agregada e não contagem validada de pacientes únicos.

Consulte as notas `LEIA-ME_*.md` em `04_documentacao_e_auditoria/` antes de usar qualquer tabela. Para o painel descritivo, leia também `04_documentacao_e_auditoria/LEIA-ME_BASE_DESCRITIVA_TERRITORIAL_2024_2025.md`.
