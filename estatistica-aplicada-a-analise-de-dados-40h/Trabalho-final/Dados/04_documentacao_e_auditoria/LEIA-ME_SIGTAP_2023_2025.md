# SIGTAP — arquivos oficiais por competência (2023–2025)

## Origem e extração

- Fonte: Ministério da Saúde/DATASUS, FTP oficial: [ftp://ftp2.datasus.gov.br/pub/sistemas/tup/downloads/](ftp://ftp2.datasus.gov.br/pub/sistemas/tup/downloads/).
- Data do download: 25/10/2026.
- Conteúdo: 36 ZIPs mensais, janeiro/2023 a dezembro/2025; total de 73,6 MB em tamanho de arquivo.
- Os arquivos ZIP foram testados com `unzip -t`; os 36 passaram sem erro.
- Cada ZIP preserva a versão integral da Tabela Unificada SIGTAP da competência indicada no nome do arquivo.

## Arquivo compacto para a análise

`../02_derivados_preliminares/SIGTAP/procedimentos_renal_sigtap_por_competencia_2023_2025.csv` contém seis procedimentos observados na APAC, em 36 competências (216 linhas), extraídos da tabela `tb_procedimento.txt` de cada ZIP. Delimitador `;`; codificação UTF-8 com BOM. O campo `competencia` corresponde à competência indicada no nome do ZIP. `dt_competencia` reproduz o campo da linha SIGTAP e pode indicar atualização cadastral do procedimento, por isso não deve substituir a competência da versão usada.

Campos incluídos: código e descrição oficial, complexidade, sexo, quantidade máxima de execução, idade mínima/máxima, valores SH/SA/SP, financiamento, rubrica e `dt_competencia`.

### Códigos confirmados

| Código | Descrição encontrada no SIGTAP | Presença no período |
|---|---|---|
| 0305010026 | Diálise peritoneal intermitente (DPI), máximo 2 sessões por semana | 36/36 competências |
| 0305010107 | Hemodiálise, máximo 3 sessões por semana | 36/36 competências |
| 0305010115 | Hemodiálise em paciente com sorologia positiva para HIV e/ou hepatite B e/ou hepatite C, máximo 3 sessões por semana | 36/36 competências |
| 0305010166 | Manutenção e acompanhamento domiciliar de paciente submetido a DPA/DPAC | 36/36 competências |
| 0305010182 | Treinamento de paciente submetido a diálise peritoneal DPAC/DPA, 9 dias | 36/36 competências |
| 0305010204 | Hemodiálise pediátrica, máximo 4 sessões por semana | 36/36 competências |

Os códigos foram confirmados na estrutura oficial de cada competência; portanto, as descrições preliminares podem ser substituídas pelas descrições SIGTAP. A presença do código em toda a série não resolve, por si só, qual modalidade clínica cada registro representa; agrupamentos analíticos devem considerar os atributos e o objetivo do estudo.

## Integridade

`SHA256SUMS.txt` registra o SHA-256 de cada ZIP e do CSV compacto para detectar alterações acidentais. A listagem e o download foram feitos do FTP oficial DATASUS; a extração do CSV foi derivada exclusivamente desses ZIPs.
