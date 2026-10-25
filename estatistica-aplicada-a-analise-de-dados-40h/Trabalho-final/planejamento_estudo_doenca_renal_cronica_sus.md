# Planejamento do estudo: tratamento da doença renal crônica no SUS

## 1. Tema

**Tratamento da doença renal crônica no Sistema Único de Saúde (SUS), com foco no acesso à terapia renal substitutiva e nas diferenças regionais.**

## 2. Justificativa

A doença renal crônica pode exigir acompanhamento contínuo e terapias de alta complexidade, como hemodiálise. A distribuição dos serviços, a produção assistencial e os desfechos hospitalares podem variar entre estados e regiões. A análise de dados públicos pode ajudar a descrever essas diferenças e identificar questões relevantes para o planejamento da atenção à saúde.

## 3. Objetivo geral

Descrever e analisar o acesso e a evolução da assistência relacionada à doença renal crônica no SUS, comparando estados e regiões e examinando indicadores de oferta, produção, internações, óbitos hospitalares e gastos.

## 4. Objetivos específicos

1. **Acesso à hemodiálise:** comparar a oferta de serviços ou estabelecimentos de terapia renal substitutiva entre estados e regiões, considerando a população.
2. **Desigualdade no acesso:** verificar a distribuição geográfica da oferta, inclusive diferenças entre capitais e interior, quando os dados permitirem.
3. **Internações relacionadas à doença renal:** comparar internações e óbitos hospitalares registrados por região e ano.
4. **Evolução dos tratamentos:** examinar mudanças ao longo do tempo na oferta de serviços, nas internações e na produção de procedimentos relacionados à terapia renal substitutiva.
5. **Relação entre oferta e desfechos:** explorar se estados com maior oferta apresentam taxas diferentes de internação ou óbito hospitalar.
6. **Gastos com tratamento (objetivo complementar):** analisar os valores registrados pelo SUS para procedimentos de terapia renal substitutiva e comparar sua evolução entre regiões e anos.

## 5. Perguntas de pesquisa

- Como a oferta de serviços de terapia renal substitutiva se distribui entre estados e regiões, considerando o tamanho da população?
- Existem diferenças de oferta entre capitais e interior ou entre regiões do país?
- Como evoluíram a produção de procedimentos, as internações e os óbitos hospitalares relacionados à doença renal nos anos analisados?
- Há associação entre a oferta de serviços e as taxas de internação ou óbito hospitalar entre estados?
- Como variam os gastos públicos registrados com terapia renal substitutiva entre regiões e ao longo do tempo?

## 6. Delineamento e unidade de análise

Estudo observacional, ecológico e retrospectivo, baseado em dados secundários públicos agregados. A unidade de análise será definida conforme a disponibilidade de cada fonte: UF por mês ou ano; região por mês ou ano; e, quando possível, município ou estabelecimento.

A análise ecológica permite comparar grupos geográficos, mas não permite inferir diretamente resultados individuais. Associações observadas entre estados não demonstram que a oferta de serviços causou diferenças nos desfechos.

## 7. População, período e abrangência

- **Abrangência geográfica:** Brasil, com comparações entre as 27 unidades da federação e as cinco regiões.
- **Período inicial para a análise principal:** 2024–2025 para produção ambulatorial mensal de hemodiálise já mapeada.
- **Períodos para os demais indicadores:** a definir após verificar disponibilidade, consistência e atualização das fontes. Para tendências, poderá ser necessário usar uma série histórica mais longa.
- **População de referência:** população residente por UF/região e ano, para cálculo de indicadores por habitante.

## 8. Fontes verificadas e situação dos dados

Esta seção distingue páginas oficiais consultadas de arquivos de dados efetivamente obtidos. A existência de uma página ou sistema não significa que a extração, os campos ou a série temporal necessária já tenham sido confirmados.

| Dimensão | Fonte oficial verificada | O que está confirmado | Situação para este estudo |
|---|---|---|---|
| Produção ambulatorial | [TabNet SIA/SUS — produção ambulatorial](https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sia/cnv/qabr.def) e [Notas técnicas do SIA](https://tabnet.datasus.gov.br/cgi/sia/padescr.htm) | As notas técnicas identificam a origem SIA/SUS e documentam variáveis como local de atendimento, ano/mês de processamento, procedimento e valores/quantidades da produção aprovada. | **Extração registrada:** arquivo CSV de hemodiálise por UF e mês para 2024–2025, com cinco códigos SIGTAP selecionados. Ver seção 12 e arquivo de mapeamento. A extração mede produção administrativa aprovada, não pessoas únicas nem sessões individuais confirmadas. |
| Estabelecimentos/serviços | [CNES — consulta de serviços especializados](https://cnes2.datasus.gov.br/mod_ind_especialidades.asp) | A página oficial oferece filtros de estado, município, competência, tipo de serviço, serviço especializado, classificação e atendimento SUS/não SUS, ambulatorial/hospitalar. | **Fonte consultada; extração pendente.** Ainda não foi executada uma consulta de diálise/TRS nem foram conferidos seus resultados, períodos e definição operacional. Não contar serviços ou estabelecimentos até essa validação. |
| Internações/óbitos hospitalares | [SIH/SUS — procedimentos hospitalares e notas técnicas](https://tabnet.datasus.gov.br/cgi/sih/Proced_hosp_loc_int_2008.pdf) | A documentação oficial informa que o SIH/SUS recebe informações de internações via AIH e descreve variáveis do sistema. | **Documentação consultada; tabulação específica pendente.** Não foi validada uma extração de internações por doença renal, nem códigos CID-10/procedimentos, campos, período ou filtros para óbito. Esses detalhes devem ser definidos e conferidos na tabulação antes de qualquer indicador. |
| População para denominadores | [IBGE — estimativa 2024](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2024/estimativa_dou_2024.pdf), [IBGE — estimativa 2025](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20251031.pdf) e [página do produto](https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html) | Os arquivos oficiais consultados apresentam estimativas para Brasil e UFs com referência em 1º de julho de 2024 e 1º de julho de 2025, respectivamente. | **Fonte e anos 2024/2025 confirmados; arquivo de população ainda não incorporado ao conjunto analítico.** Para indicadores municipais ou capitais/interior, será necessário usar os valores municipais correspondentes e harmonizar a geografia. |

### Arquivos de dados efetivamente disponíveis

- **SIA/SUS:** `Dados/hemodialise_sia_sus_uf_mes_2024_2025.csv` — extração registrada para os cinco códigos SIGTAP descritos no mapeamento. Consultar o próprio CSV e o registro para conferir filtros e valores antes de qualquer cálculo.
- **CNES:** nenhum arquivo analítico extraído nesta etapa.
- **SIH/SUS:** nenhum arquivo analítico extraído nesta etapa.
- **IBGE população:** fontes oficiais de 2024 e 2025 verificadas, mas ainda não copiadas/transformadas em arquivo analítico do estudo.

Os objetivos abaixo são perguntas de pesquisa. A existência de um campo em uma fonte ou sua adequação à pergunta só será afirmada depois da consulta correspondente.

## 9. Indicadores propostos

### Acesso à hemodiálise

- Número de estabelecimentos/serviços de terapia renal substitutiva por UF e região.
- Número de estabelecimentos/serviços por milhão de habitantes.
- Produção aprovada de procedimentos de hemodiálise por UF, região e mês.
- Produção aprovada por mil ou milhão de habitantes, se a comparação exigir padronização populacional.

### Desigualdade geográfica

- Distribuição dos serviços e da produção entre regiões e estados.
- Diferença entre capitais e interior, caso seja possível identificar a localização do serviço e definir adequadamente os grupos.
- Medidas descritivas de dispersão e concentração entre UFs.

### Internações e óbitos hospitalares

- Número e taxa de internações relacionadas à doença renal por UF/região.
- Óbitos hospitalares registrados e proporção de óbitos entre internações, interpretada como indicador hospitalar.
- Duração média da internação e valores registrados, quando disponíveis e pertinentes.

### Evolução temporal

- Variação mensal ou anual da oferta, da produção e das internações.
- Comparação entre anos completos e períodos equivalentes.
- Identificação de sazonalidade ou mudanças de tendência apenas se a extensão e qualidade da série permitirem.

### Gastos

- Valor aprovado para procedimentos de terapia renal substitutiva por UF, região e ano.
- Evolução nominal dos valores; se houver comparação ao longo de vários anos, considerar atualização monetária e explicitar o índice utilizado.
- Gasto por habitante como medida complementar, sem confundi-lo com custo individual do tratamento.

## 10. Plano de análise estatística

1. **Preparação:** verificar códigos e rótulos, períodos, unidades, valores ausentes, supressões, duplicidades e consistência das totalizações.
2. **Descrição:** calcular frequências, totais, proporções, taxas populacionais e medidas de dispersão; apresentar tabelas, gráficos de série temporal e mapas quando houver geografia adequada.
3. **Comparações:** comparar regiões/estados e períodos usando testes compatíveis com a estrutura dos dados e com as premissas verificadas. Para contagens, avaliar métodos apropriados à distribuição e considerar exposição populacional.
4. **Associações:** explorar associação entre oferta e desfechos hospitalares por UF/ano, usando taxas ou modelos que considerem o tamanho populacional e potenciais fatores de confusão disponíveis.
5. **Gastos:** descrever evolução e distribuição dos valores; ajustar por inflação se a análise cobrir diferentes anos.
6. **Incerteza e robustez:** apresentar intervalos de confiança quando cabível, verificar sensibilidade a definições alternativas e evitar conclusões causais a partir de dados ecológicos observacionais.

Os testes de hipótese e modelos finais serão escolhidos depois da inspeção dos dados e da definição das variáveis. A unidade de observação, a dependência temporal e a comparabilidade entre estados devem ser consideradas para evitar tratar cada mês ou UF como observação independente quando não for apropriado.

## 11. Limitações e cuidados de interpretação

- Quantidade aprovada no SIA/SUS é produção administrativa; não equivale necessariamente a número de pacientes, sessões efetivamente recebidas por indivíduo, cobertura assistencial ou adesão.
- A consulta de serviços especializados do CNES foi verificada, mas a extração de diálise/TRS não foi feita; por isso, ainda não há contagem validada de oferta nem medida de capacidade ou disponibilidade de vagas.
- O SIH/SUS é documentado como sistema de informações hospitalares baseado em AIH; a definição operacional de internação renal e a disponibilidade/uso de campo de óbito ainda dependem da tabulação específica. Mesmo quando calculado, óbito hospitalar não deve ser interpretado como mortalidade de toda a população com doença renal nem como sobrevida de pessoas em hemodiálise.
- Dados agregados por estado ou município não permitem vincular oferta, tratamento e desfecho no nível individual.
- Diferenças regionais podem refletir idade, prevalência, comorbidades, condições socioeconômicas, organização da rede, fluxos entre municípios/estados, qualidade do registro e outros fatores não observados.
- Meses recentes podem estar sujeitos a atualização, conforme nota do TabNet; a data de extração deve ser registrada.
- Valores financeiros nominais de anos diferentes não são diretamente comparáveis sem considerar inflação.

## 12. Situação atual e próximos passos

**Registro de andamento — 24/10/2026**

### Já realizado

- Mapeada a tabulação SIA/SUS de produção ambulatorial de hemodiálise por UF e mês, para 2024–2025.
- Extraídos cinco códigos SIGTAP relacionados à hemodiálise.
- Salvo o CSV em `Dados/hemodialise_sia_sus_uf_mes_2024_2025.csv`.
- Salvo o registro do mapeamento em `mapeamento_hemodialise_sia_sus.md`.
- Consultadas páginas oficiais do SIA/SUS, CNES, SIH/SUS e IBGE; o arquivo de referências bibliográficas está salvo em `referencias_bibliograficas_doenca_renal_cronica_sus.md`.
- Confirmadas nas páginas do IBGE as estimativas para UFs referentes a 1º de julho de 2024 e 1º de julho de 2025; os arquivos ainda não foram integrados ao conjunto analítico.
- Confirmada a existência de filtros geográficos e de competência na consulta de serviços especializados do CNES; nenhuma extração de diálise/TRS foi feita.
- Consultada a documentação geral do SIH/SUS; nenhuma tabulação específica de doença renal foi validada ou extraída.

### Etapa A — Extração e preparação dos dados

Esta etapa termina quando os arquivos necessários estiverem obtidos, documentados e validados estruturalmente. Ainda não é a etapa de testar hipóteses ou interpretar resultados.

1. **SIA/SUS — validar a extração já existente:** conferir o CSV em relação à consulta registrada; verificar os cinco códigos SIGTAP, filtros, meses de janeiro de 2024 a dezembro de 2025, UFs, totais e valores. Registrar correções, se necessárias.
2. **CNES — mapear antes de extrair:** localizar e confirmar a classificação oficial aplicável à diálise/terapia renal substitutiva; verificar competências, variáveis e geografia na consulta; então extrair os registros necessários para contar serviços/estabelecimentos segundo uma definição explícita.
3. **SIH/SUS — mapear antes de extrair:** definir e justificar códigos CID-10 e/ou procedimentos que identifiquem internações relacionadas à doença renal; verificar na tabulação os campos disponíveis para período, geografia, internações e óbito; então extrair apenas os indicadores sustentados pelos campos observados.
4. **IBGE — obter denominadores:** baixar e organizar as estimativas oficiais de população para UFs em 2024 e 2025. Se a análise incluir capitais/interior ou município, obter os dados municipais correspondentes e documentar a classificação territorial.
5. **Documentar os arquivos:** para cada extração, guardar arquivo bruto, data, link da consulta, filtros, códigos, competência/período, unidade geográfica e limitações. Registrar separadamente fontes consultadas e dados efetivamente baixados.
6. **Preparar e validar a estrutura:** harmonizar códigos de UF/município, datas/competências, definições e unidades; conferir ausências, duplicidades, totalizações, revisões e compatibilidade temporal e geográfica entre bases.
7. **Confirmar o escopo viável:** com as bases mapeadas, escolher quais dimensões entram na análise principal. A produção de hemodiálise é a dimensão com extração registrada; oferta CNES e internações SIH só entram se suas definições e dados forem confirmados.

**Situação para iniciar esta etapa:** SIA/SUS extraído, aguardando validação; CNES e SIH/SUS com páginas/documentação consultadas, mas sem extração específica; IBGE 2024/2025 confirmado como fonte, sem arquivo integrado ao conjunto analítico.

### Etapa B — Análise depois de obter e validar os dados

Esta etapa começa somente após a conclusão da Etapa A e a definição do conjunto analítico.

1. **Explorar os dados:** examinar distribuições, períodos, valores ausentes, extremos, mudanças de registro e comparabilidade entre UFs/anos.
2. **Definir indicadores:** especificar numeradores, denominadores, escala (por exemplo, por 100 mil habitantes), unidade de análise e regras de agregação. Não interpretar produção aprovada como número de pacientes.
3. **Formular perguntas e hipóteses:** definir hipótese nula e alternativa para comparações que façam sentido diante dos dados, período e desenho observacional.
4. **Escolher métodos estatísticos:** selecionar testes/modelos após avaliar premissas, distribuição, tamanho amostral, dependência temporal, exposição populacional e possíveis fatores de confusão.
5. **Realizar análises descritivas e comparativas:** estimar frequências, taxas, diferenças e tendências; calcular intervalos de confiança quando apropriado; executar análises de associação apenas se as variáveis e unidades forem compatíveis.
6. **Avaliar robustez e limitações:** testar definições alternativas justificadas e discutir sub-registro, revisão, cobertura dos sistemas e falácia ecológica. Tratar óbito hospitalar como desfecho hospitalar, não como medida de sobrevida individual.
7. **Apresentar resultados:** elaborar tabelas, gráficos e texto que diferenciem descrição, associação e causalidade, sem afirmar relações causais que o desenho não permite.

**Próxima ação recomendada na Etapa A:** validar o arquivo CSV do SIA/SUS e registrar o resultado dessa validação.

## 13. Referências oficiais consultadas

- Ministério da Saúde/DATASUS. [Produção Ambulatorial do SUS — notas técnicas do SIA/SUS](https://tabnet.datasus.gov.br/cgi/sia/padescr.htm). Documenta origem dos dados e variáveis de tabulação.
- Ministério da Saúde/DATASUS. [TabNet — produção ambulatorial por local de atendimento](https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sia/cnv/qabr.def). Tabulação usada para mapear a extração de hemodiálise. A consulta efetiva e os filtros estão documentados no arquivo de mapeamento.
- Ministério da Saúde/DATASUS. [CNES — consulta de serviços especializados](https://cnes2.datasus.gov.br/mod_ind_especialidades.asp). Página oficial consultada para verificar filtros disponíveis; não representa, por si só, uma extração sobre diálise.
- Ministério da Saúde/DATASUS. [Procedimentos hospitalares do SUS — notas técnicas do SIH/SUS](https://tabnet.datasus.gov.br/cgi/sih/Proced_hosp_loc_int_2008.pdf). Documentação do sistema; a tabulação renal específica continua pendente.
- IBGE. [Estimativas da população residente — referência de 1º de julho de 2024](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2024/estimativa_dou_2024.pdf).
- IBGE. [Estimativas da população residente — referência de 1º de julho de 2025](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20251031.pdf).
- IBGE. [Produto Estimativas da População — conceitos e edições](https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html).
- Ministério da Saúde. [SIGTAP — Sistema de Gerenciamento da Tabela de Procedimentos, Medicamentos e OPM do SUS](https://sigtap.datasus.gov.br/tabela-unificada/app/sec/inicio.jsp). Referência para conferência dos códigos e descrições dos procedimentos selecionados.

**Acesso às fontes conferido em 24/10/2026.** A data de acesso não substitui a data de extração dos dados; esta deverá ser registrada para cada arquivo baixado.
