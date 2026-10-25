# Mapeamento de dados: hemodiálise no SUS

## Objetivo da análise

Investigar a produção ambulatorial do SUS relacionada à hemodiálise por estado e mês, com foco em descrever o acesso e a evolução dos procedimentos no período recente. A análise estatística poderá comparar volumes entre estados e períodos e aplicar testes de hipótese adequados aos dados agregados.

**Limite de interpretação:** a produção aprovada de procedimentos não identifica pacientes, sobrevivência, cura ou sucesso individual do tratamento. Portanto, estes dados não permitem concluir se a hemodiálise prolonga a vida ou estimar eficácia clínica. Para isso seria necessário um conjunto longitudinal de pacientes com desfechos e variáveis clínicas, além de desenho analítico apropriado.

## Fonte e tabulação mapeada

- **Fonte:** Ministério da Saúde, Sistema de Informações Ambulatoriais do SUS (SIA/SUS), via TabNet DATASUS.
- **Tabulação:** Produção Ambulatorial do SUS – Brasil – por local de atendimento.
- **Link da tabulação:** <https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sia/cnv/qabr.def>
- **Unidade geográfica:** UF (estado de atendimento).
- **Período pretendido:** janeiro de 2024 a dezembro de 2025 (24 meses).
- **Medida selecionada:** quantidade aprovada (`Qtd.aprovada`).
- **Formato pretendido:** colunas separadas por ponto e vírgula (`;`).
- **Variáveis de consulta confirmadas na tela:** linha = UF; coluna = Ano/mês atendimento; conteúdo = Qtd.aprovada; meses de Jan/2024 a Dez/2025 selecionados.

## Procedimentos de hemodiálise mapeados

Os códigos abaixo foram identificados/selecionados na lista de procedimentos da tabulação:

| Código SIGTAP | Descrição apresentada |
|---|---|
| 0305010093 | Hemodiálise (máximo 1 sessão por semana – excepcionalidade) |
| 0305010107 | Hemodiálise (máximo 3 sessões por semana) |
| 0305010115 | Hemodiálise em portador de HIV/hepatite (máximo 3 sessões por semana) |
| 0305010123 | Hemodiálise em portador de HIV/hepatite (máximo 1 sessão por semana – excepcionalidade) |
| 0305010204 | Hemodiálise pediátrica (máximo 4 sessões por semana) |

**Conferência da consulta:** o resultado retornado pelo TabNet confirmou os cinco códigos acima no filtro “Procedimento”.

## Disponibilidade e status

- **Os períodos estão disponíveis na interface:** sim; a lista mostrava os meses de Jan/2024 a Dez/2025 e todos estavam selecionados.
- **A consulta foi executada com sucesso:** sim; a tabela foi gerada pelo TabNet.
- **Dados extraídos:** sim; 27 UFs e uma linha de total, com 24 meses de 2024–2025.
- **Arquivo salvo:** `Dados/hemodialise_sia_sus_uf_mes_2024_2025.csv`.
- **Formato:** CSV UTF-8, delimitado por ponto e vírgula. O arquivo contém as colunas mensais e `Total 2024-2025`, calculado a partir dos 24 meses selecionados.
- **Status geral:** extração concluída; recomenda-se validar os dados e suas limitações antes da análise.
- **Nota sobre a tabela retornada:** o TabNet acrescentou Oct/2023, Nov/2023 e Dez/2023 apesar do intervalo selecionado. Essas colunas foram excluídas do CSV, e o total foi recalculado apenas para 2024–2025.
- **Observação da própria tabulação:** os dados referentes aos últimos seis meses estão sujeitos a atualização. Isso afeta especialmente meses recentes e deve ser levado em conta em futuras atualizações da análise.

## Plano de análise possível com esta fonte

Com a tabela extraída e os procedimentos confirmados, será possível:

1. descrever a quantidade aprovada por UF e mês;
2. comparar distribuição e variação entre estados e regiões;
3. avaliar tendências mensais ou diferenças entre anos, com métodos compatíveis com contagens e com a estrutura temporal;
4. formular testes de hipótese sobre diferenças de produção entre períodos ou grupos de estados, deixando explícito que a unidade é produção administrativa agregada.

A quantidade aprovada mede produção registrada no SIA/SUS; não equivale necessariamente ao número de pessoas em tratamento, sessões efetivamente recebidas por paciente, cobertura populacional ou desfecho clínico.

## Referências e links

- DATASUS/TabNet – Produção Ambulatorial do SUS por local de atendimento: <https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sia/cnv/qabr.def>
- Ministério da Saúde/DATASUS – portal de transferência de arquivos (referenciado na própria tabulação): <https://datasus.saude.gov.br/transferencia-de-arquivos/>
- SIGTAP – Sistema de Gerenciamento da Tabela de Procedimentos, Medicamentos e OPM do SUS: <https://sigtap.datasus.gov.br/tabela-unificada/app/sec/inicio.jsp>
- Nota técnica da produção ambulatorial por local de atendimento, referenciada na tabulação: <https://tabnet.datasus.gov.br/cgi/sia/Prod_amb_loc_atend_2008.pdf>

## Próximas etapas

1. Validar os cabeçalhos, meses, estados, valores e totalizações do CSV.
2. Considerar as revisões dos meses mais recentes antes de consolidar os resultados.
3. Se necessário, obter denominadores populacionais para comparar taxas entre estados, em vez de apenas volumes absolutos.
