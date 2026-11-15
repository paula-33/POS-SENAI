# Planejamento do estudo: tratamento da doença renal crônica no SUS

## 1. Tema

**Padrões territoriais e temporais da produção assistencial de hemodiálise registrada no SUS e das internações hospitalares por insuficiência renal, com exploração de associações ecológicas entre UFs.**

## 2. Justificativa

A doença renal crônica pode exigir acompanhamento contínuo e terapias de alta complexidade, como hemodiálise. A distribuição dos serviços, a produção assistencial e os desfechos hospitalares podem variar entre estados e regiões. A análise de dados públicos pode ajudar a descrever essas diferenças e identificar questões relevantes para o planejamento da atenção à saúde.

## 3. Objetivo geral

**Objetivo vigente (decisão de 05/11/2026):** descrever padrões temporais e territoriais da produção aprovada de hemodiálise no SIA/SUS e das internações N17–N19 no SIH/TabNet, e explorar associações ecológicas entre esses indicadores por UF e período usando frequências, correlações e testes de hipóteses compatíveis com dados agregados. O escopo não inclui estimar eficácia ou efetividade do tratamento.

Os resultados serão interpretados no nível das unidades territoriais e como padrões exploratórios; não permitem inferência individual nem atribuição causal ao tratamento.

**Nota de escopo:** trechos posteriores sobre efetividade comparativa e coorte individual registram o objetivo anterior e ficam como histórico metodológico; não são etapas ativas. O protocolo comparativo provisório está suspenso.

## 4. Objetivos específicos

1. **Produção registrada:** descrever a quantidade aprovada de procedimentos de hemodiálise por UF e mês; não interpretar esse volume como número de pessoas distintas.
2. **Variação territorial:** comparar níveis e mudanças da produção aprovada e das internações entre UFs/regiões, sem afirmar acesso ou capacidade operacional quando não medidos.
3. **Internações relacionadas à doença renal:** comparar internações e óbitos hospitalares registrados por região e ano.
4. **Evolução dos tratamentos:** examinar mudanças ao longo do tempo na oferta de serviços, nas internações e na produção de procedimentos relacionados à terapia renal substitutiva.
5. **Relação entre produção registrada e desfechos:** explorar, em nível agregado, se estados com maior volume registrado de atendimento apresentam taxas diferentes de internação ou óbito hospitalar.
6. **Desenvolvimento de hipóteses:** identificar padrões e diferenças que justifiquem análises posteriores ou coleta de dados contextuais; não atribuir explicações causais sem variáveis apropriadas.
7. **Inferência exploratória:** testar hipóteses sobre direção de mudanças entre UFs e associação ecológica entre produção SIA e internações SIH, com unidade, pressupostos, multiplicidade e limitações explicitados. Esses testes não estimam efeito terapêutico.

## 5. Perguntas de pesquisa

- Como os pacientes distintos e a produção aprovada de hemodiálise se distribuem entre estabelecimentos, municípios e UFs, considerando o tamanho da população?
- Existem diferenças de oferta entre capitais e interior ou entre regiões do país?
- Como evoluíram a produção de procedimentos, as internações e os óbitos hospitalares relacionados à doença renal nos anos analisados?
- Há associação ecológica entre o atendimento registrado e as taxas de internação ou óbito hospitalar entre estados?
- Como variam os gastos públicos registrados com terapia renal substitutiva entre regiões e ao longo do tempo?
- A direção das mudanças de produção e internações entre 2024 e 2025 é semelhante entre UFs?
- Há associação monotônica entre quantidade aprovada SIA e internações SIH por população entre UFs?
- As mudanças percentuais de SIA e SIH covariam entre UFs?

## 6. Delineamento e unidade de análise

O trabalho tem duas camadas metodológicas que não devem ser confundidas:

1. **Análise atualmente viável:** estudo observacional retrospectivo com dados administrativos agregados, cuja unidade será UF/mês ou, após validação do SUS 360º, estabelecimento/competência. Esta camada descreve produção, distribuição e desfechos hospitalares e estima associações ecológicas.
2. **Análises associativas ecológicas:** usar UF-mês e UF-ano para descrever distribuições, testar hipóteses de variação e estimar correlações exploratórias. Não interpretar essas associações como efeitos individuais ou causais.

A análise ecológica não permite inferir resultados individuais nem efeito causal. Para tratamento em condições usuais, o termo mais preciso é **efetividade**; eficácia, em sentido metodológico estrito, se refere ao efeito sob condições controladas. Um teste de hipótese em dados agregados não substitui um desenho capaz de comparar resultados atribuíveis ao tratamento.

### Reavaliação de viabilidade e status (atualizada em 05/11/2026)

As fontes atualmente reunidas não formam um grupo comparador de pessoas elegíveis com DRC que receberam cuidado conservador: a APAC observada é de tratamento dialítico, enquanto a tabela SIH N17–N19 conta registros hospitalares por diagnóstico e não identifica a população ambulatorial elegível sem diálise. O SIH também não contém identificador público de paciente que permita ligar internações à APAC. Portanto, a pergunta “diálise versus cuidado conservador” não é estimável com estes arquivos.

As bases podem sustentar, após os controles específicos, (a) descrição de produção aprovada de procedimentos por UF/mês no SIA, sem inferir pacientes tratados ou resultado clínico; (b) descrição de estabelecimentos cadastrados na competência CNES observada; e (c) descrição de internações/óbitos hospitalares por diagnóstico no SIH, uma vez que a unidade e a extração sejam reconciliadas. Uma análise APAC de modalidades só será considerada após validar identificador, continuidade, datas e desfecho; mesmo então, a comparação observacional entre modalidades exigiria controle de confundimento e não estimaria o benefício da diálise frente à ausência de diálise.

**Atualização de 05/11/2026:** a reextração dos DBCs SIH já foi executada e está descrita mais adiante neste planejamento e na nota SIH; os números 368.917 e 33.492 são apenas o resultado do CSV preliminar antigo e não devem ser reportados como resultado corrente. A busca de scripts e saídas antigas não localizou a rotina linha a linha de 368.905; a diferença de 12 permanece sem localização. A comparação TabNet continua limitada por diagnóstico agregado N17–N19, atendimento versus processamento e regra de contagem. Não assumir que deduplicação por `N_AIH` reproduza TabNet.

**Decisão de análise (05/11/2026):** manter o estudo no escopo descritivo/associativo solicitado. Não produzir estimativa causal de eficácia/efetividade nem denominador de pacientes tratados a partir da produção agregada. A camada descritiva SIA/IBGE e SIH N17–N19 foi construída; testes exploratórios estão registrados no notebook. N18 permanece preliminar e excluído; APAC não sustenta seguimento individual validado.

**Registro de execução (05/11/2026):** a leitura independente das referências `AP_APACANT` foi documentada e incorporada ao notebook de acompanhamento; foram conferidos 81.416 pares distintos atual→anterior, 40.170 autorreferências e 10.756 alvos não encontrados no recorte. A evidência não valida continuidade individual. O notebook também foi ajustado para ler os CSVs de auditoria com separadores distintos e suas células de conferência foram executadas. Permanecem pendentes para a auditoria: localizar a rotina/saída histórica SIH para a diferença de 12 linhas e obter especificação técnica das anomalias APAC. Essas pendências não impedem a análise descritiva/associativa SIA e SIH N17–N19; apenas mantêm N18 fora dos totais e APAC fora da análise longitudinal.

### Nota metodológica: efetividade não faz parte do escopo vigente

> O texto abaixo registra a justificativa metodológica do objetivo anterior. Ele é mantido para histórico, mas não define tarefas ativas após a decisão de seguir com análise descritiva/associativa.

A documentação metodológica do Ministério da Saúde diferencia eficácia (condições controladas) de efetividade (prática usual). Para estimar efetividade, não basta observar que pessoas tratadas tiveram internações ou óbitos: é preciso comparar resultados sob o tratamento e sob uma alternativa adequada, entre pacientes comparáveis, com acompanhamento temporal definido e ajuste para fatores prognósticos relevantes. O estimando deve ser definido antes dos testes. Se a comparação for hemodiálise versus diálise peritoneal, o resultado será efetividade comparativa entre modalidades; isso não demonstra o efeito da diálise frente a não tratar.

O SIA disponibiliza arquivos APAC e documentação para tratamento dialítico. Os arquivos ATDAC públicos de 2024–2025 foram obtidos; a auditoria inicial confirmou campos de paciente, competência, procedimento, datas de validade e de início do tratamento e indicador de óbito. A documentação técnica consultada distingue o layout do DBC dialítico do layout geral de remessa APAC. As ressalvas e discrepâncias observadas estão descritas em `Dados/04_documentacao_e_auditoria/LEIA-ME_APAC_ATD_2024_2025.md`. O serviço oficial distribui microdados anonimizados, mas a estabilidade do identificador entre competências ainda não está formalmente confirmada. Para vincular APAC a SIM ou obter dados identificáveis, aplicam-se procedimentos legais, éticos e institucionais próprios.

**Porta de viabilidade:** verificar se a APAC dialítica pública contém (a) identificador pseudonimizado estável entre competências; (b) início e modalidade do tratamento; (c) desfecho de óbito confiável e data/tempo de seguimento; (d) grupo comparador apropriado; e (e) variáveis prognósticas para controle de confundimento. A auditoria inicial encontrou coerência interna entre motivo de saída e flags, mas também 12 registros com tipo APAC/procedimento não classificado e datas clínicas após a competência máxima. Esses pontos precisam ser resolvidos antes da coorte. Se comparar diálise com cuidado conservador, verificar uma fonte que identifique também pacientes elegíveis não dialíticos. Sem comparador adequado, os dados podem descrever a sobrevida/prognóstico da coorte tratada, mas não concluir que a diálise causou benefício. Se faltar requisito central, limitar as conclusões a descrição/associação.

## 7. População, período e abrangência

- **Abrangência geográfica:** Brasil, com comparações entre as 27 unidades da federação e as cinco regiões.
- **Período inicial para a análise principal:** 2024–2025 para produção ambulatorial mensal de hemodiálise já mapeada.
- **Períodos para os demais indicadores:** a definir após verificar disponibilidade, consistência e atualização das fontes. Para tendências, poderá ser necessário usar uma série histórica mais longa.
- **População de referência:** população residente por UF/região e ano, para cálculo de indicadores por habitante.

## 8. Fontes verificadas e situação dos dados

Esta seção distingue páginas oficiais consultadas de arquivos de dados efetivamente obtidos. A existência de uma página ou sistema não significa que a extração, os campos ou a série temporal necessária já tenham sido confirmados.

| Dimensão | Fonte oficial verificada | O que está confirmado | Situação para este estudo |
|---|---|---|---|
| Produção ambulatorial | [TabNet SIA/SUS — produção ambulatorial](https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sia/cnv/qabr.def) e [Notas técnicas do SIA](https://tabnet.datasus.gov.br/cgi/sia/padescr.htm) | As notas técnicas identificam a origem SIA/SUS e documentam variáveis como local de atendimento, ano/mês de processamento, procedimento e valores/quantidades da produção aprovada. | **Extração validada:** CSV por UF e mês para 2024–2025; 27 UFs, 24 competências, valores inteiros não negativos e totais mensais/estaduais conciliados. Os cinco códigos SIGTAP foram conferidos no mapeamento e no HTML salvo da consulta. Total nacional: 37.296.852. A medida é produção administrativa aprovada, não pessoas únicas nem sessões individuais confirmadas. |
| Cadastro de estabelecimentos/equipamentos | [CNES — documentação e tabelas de domínio](https://cnes.datasus.gov.br/pages/downloads/documentacao.jsp) e [consulta de serviços especializados](https://cnes2.datasus.gov.br/mod_ind_especialidades.asp) | O arquivo CNES 2024/12 foi relacionado entre perfil de diálise, estabelecimentos e serviço/classificação. A consulta pública também registra equipamentos em campos como existentes, em uso e SUS, sujeitos a atualização cadastral. | **Extraído, mas excluído do conjunto analítico principal por decisão metodológica:** é um retrato cadastral e não mede vagas ou capacidade operacional máxima. Arquivos ficam guardados para referência, não entram nos indicadores centrais. Ver `Dados/04_documentacao_e_auditoria/LEIA-ME_CNES_dialise_2024_12.md`. |
| Produção por estabelecimento e pacientes | [SUS 360º — Monitor de Hemodiálise](https://sus360.saude.gov.br/painel/hemodialise/) | A página oficial descreve bases públicas de hemodiálise agregadas por CNES, procedimento e competência, com campos de pacientes distintos, quantidade apresentada/aprovada e valores; lista arquivos CSV de 2023, 2024 e 2025. O painel informa que está em atualização. | **Extração específica ainda pendente.** O conjunto APAC individual abaixo foi obtido e auditado estruturalmente; o CSV agregado SUS 360º pode servir para contextualização/validação depois do download e conferência dos campos. |
| Internações/óbitos hospitalares | [TabNet — morbidade hospitalar por local de internação](https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/niuf.def), [notas técnicas do SIH/SUS](https://tabnet.datasus.gov.br/cgi/sih/Proced_hosp_loc_int_2008.pdf) e [FTP oficial de microdados SIH/SUS](ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/) | TabNet disponibiliza a categoria “Insuficiência renal” (N17–N19); microdados incluem diagnóstico principal, tipo de AIH e flag de óbito hospitalar. | **N17–N19 TabNet obtido; reextração N18 dos 648 DBCs concluída em 05/11/2026:** 213.789 linhas por diagnóstico principal N18 e `DT_INTER` em 2024–2025. A reextração corrigida fica em nova pasta de auditoria; o CSV anterior de 368.917 continua preservado como derivado preliminar incompatível: 155.128 linhas excedentes não têm a mesma UF/competência que a extração DBC, embora seus campos analíticos encontrem correspondência de payload. Nas 647 células TabNet preenchidas, N18 fica abaixo de N17–N19 em todas; RR/dez-2025 está ausente no TabNet e tem zero N18. A definição TabNet está documentada e o cenário `IDENT=1` foi comparado por UF/mês; a categoria TabNet ainda é N17–N19, portanto não se espera igualdade com N18. A cobertura/revisão do processamento dos DBCs não foi demonstrada como idêntica ao corte atual TabNet, e as 12 linhas entre rotinas históricas seguem não localizadas. Não usar o CSV antigo como total nem interpretar registros como pacientes/efeito terapêutico. Detalhes e artefatos em `Dados/04_documentacao_e_auditoria/LEIA-ME_SIH_N18_2024_2025.md` e `Dados/02_derivados_preliminares/SIH/auditoria_sih_dbc_reconciliacao_20261105_221707/`.
| População para denominadores | [IBGE — estimativa 2024 (planilha ODS)](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2024/POP2024_20241230.ods), [IBGE — estimativa 2025 (planilha ODS, revisão mais recente)](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20260828.ods) e [página do produto](https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html) | As planilhas oficiais têm abas para Brasil/UFs e municípios, com data de referência em 1º de julho de cada ano. Em 2025, o IBGE observa diferença de 67 pessoas entre Paraná e Santa Catarina em relação à Projeção da População (Revisão 2024), devido à alteração de limites municipais. | **Extração concluída em 24/10/2026:** ODS originais preservados e dados organizados em CSV por UF e município. Foram conferidos os 27 totais estaduais e os totais Brasil; a soma municipal coincide com cada UF nos dois anos. As estimativas são anuais, com referência em 1º de julho; harmonizar limites e geografia antes de cruzar com outras bases. |

### Arquivos de dados efetivamente disponíveis

- **SIA/SUS:** `Dados/02_derivados_preliminares/SIA/hemodialise_sia_sus_uf_mes_2024_2025.csv` — extração registrada para os cinco códigos SIGTAP descritos no mapeamento. Consultar o próprio CSV e o registro para conferir filtros e valores antes de qualquer cálculo.
- **CNES (fora do núcleo analítico):** arquivo bruto e derivados da competência 2024/12 estão preservados na pasta `Dados`. Foram retirados dos indicadores centrais porque medem registros cadastrais, não capacidade operacional ou atendimento realizado. O registro da extração permanece em `Dados/04_documentacao_e_auditoria/LEIA-ME_CNES_dialise_2024_12.md`.
- **SUS 360º — Monitor de Hemodiálise:** a página lista CSVs oficiais de 2023, 2024 e 2025 agregados por CNES, procedimento e competência. A extração/validação para o estudo ainda está pendente; não presumir que a página ou o link listado confirmem que o arquivo foi baixado.
- **SIH/SUS:** a exportação TabNet N17–N19 e sua cópia analítica estão em `Dados/sih_cnv_niuf231237179_0_58_181.csv` e `Dados/sih_insuficiencia_renal_n17_n19_uf_mes_2024_2025_analitico.csv`. Foram baixados os 648 DBCs de microdados de 2024–2025 e geradas `Dados/02_derivados_preliminares/SIH/sih_n18_microdados_uf_ano_mes_2024_2025.csv` e `Dados/02_derivados_preliminares/SIH/sih_n18_uf_mes_admissao_2024_2025.csv`. O CSV N18 antigo é incompatível e permanece preservado apenas como histórico preliminar (368.917 linhas; 33.492 `MORTE=1`). A reextração de auditoria atualizou a contagem para 213.789 linhas (213.788 `IDENT=1`, uma `IDENT=5`); ainda não é total final; N18 e N17–N19 têm abrangências diagnósticas distintas e a compatibilidade do corte de processamento não foi demonstrada. Ver `Dados/04_documentacao_e_auditoria/LEIA-ME_SIH_N18_2024_2025.md`.
- **IBGE população:** fontes originais preservadas em `Dados/POP2024_20241230.ods` e `Dados/POP2025_20260828.ods`; tabelas organizadas em `Dados/02_derivados_preliminares/IBGE/populacao_ibge_uf_2024_2025.csv` e `Dados/02_derivados_preliminares/IBGE/populacao_ibge_municipio_2024_2025.csv`.
- **SIA/APAC dialítica:** 648 arquivos DBC ATDAC de 2024–2025, para 27 UFs e 24 meses, somam 3.186.282 registros e 65 campos uniformes. A reextração de exceções de 05/11/2026 confirmou os 12 registros sem tipo/procedimento classificado e as datas futuras; as datas ainda não têm semântica validada. A auditoria prévia reporta repetições de autorizações e associações com múltiplos identificadores, mas a regra de continuidade e a estabilidade longitudinal seguem sem confirmação. Nenhum CSV analítico de pacientes foi derivado. Ver a nota APAC e a pasta `Dados/02_derivados_preliminares/APAC/auditoria_excecoes_20261105_v2/`.

### Necessidade das bases atuais para o objetivo final

| Base/arquivo atual ou candidato | Necessidade para estimar efetividade | Decisão de uso |
|---|---|---|
| SIA/SUS agregado por UF/mês (`hemodialise_sia_sus_uf_mes_2024_2025.csv`) | Não é suficiente para comparar desfechos individuais; não contém coorte nem seguimento por pessoa. | Manter como contexto e validação de totais; não é base principal de efetividade. |
| CNES bruto e derivados 2024/12 | Não medem pacientes acompanhados nem resultado do tratamento; o retrato cadastral não é necessário para a estimativa individual. | Fora do núcleo analítico; manter arquivado, sem apagar. |
| SIH agregado N17–N19 e cópia analítica | Contam internações por categoria ampla, sem identificar tratamento dialítico ou resultado individual. | Opcional para contexto epidemiológico; não necessário para efetividade. |
| SIH microdados com N18 e desfecho de internação | A extração preliminar contém diagnóstico principal, `MORTE`, datas e dados territoriais. A reextração N18 fica abaixo do agregado N17–N19 nas células observadas, coerente com a diferença de abrangência diagnóstica; a equivalência do corte de processamento não foi demonstrada, e a diferença de 12 entre rotinas antigas continua sem localização. AIH tipo 5 pode refletir prorrogação e não uma internação elegível para a medida TabNet. Não forma sozinha uma coorte de diálise nem estima sobrevida após início do tratamento. | Secundário e condicional: manter para investigação de consistência; só usar após reconciliar tipo de AIH, competência e regra TabNet. |
| IBGE população municipal/UF 2024–2025 | Necessária para taxas territoriais populacionais; não é denominador de uma coorte individual de pacientes. | Manter apenas se a análise secundária de acesso/desigualdade territorial for preservada. |
| SUS 360º agregado por CNES/mês | Mais informativo que o SIA agregado atual para pacientes distintos e produção por unidade, mas continua agregado e não acompanha trajetória individual. | Não priorizar para eficácia; usar para validação/contexto se necessário. |
| SIA/APAC de tratamento dialítico (ATD) por paciente e competência — obtida, validação em andamento | 648 arquivos DBC e campos-chave confirmados. Motivos de saída e flags são coerentes; 12 registros têm tipo APAC=4 sem procedimento principal; há datas clínicas posteriores ao período observado. Os seis códigos `AP_PRIPAL` foram confirmados nas 36 competências SIGTAP de 2023–2025. Foram encontrados 1.199.885 números distintos de autorização, com até três competências por autorização e sem duplicação na mesma autorização/competência/movimento; 12.065 autorizações associam-se a mais de um identificador de paciente. Persistem regra de reuso, investigação das chaves e completude do óbito/seguimento. Não garante comparador nem efeito causal. | Resolver exceções e definir uma unidade de análise sem contar repetições como pessoas distintas. |
| Comparador de cuidado conservador ou modalidade alternativa | Indispensável para estimar efeito relativo. APAC dialítica pode permitir comparar modalidades de diálise, mas não está confirmada uma fonte comparável de pacientes elegíveis em cuidado conservador. | Requisito em aberto; escolher comparador clínico e verificar fonte antes da análise de efetividade. |

**Síntese:** os dados já reunidos são úteis para contexto, validação e análise territorial, mas não são todos necessários para o objetivo final. A APAC dialítica foi extraída e passou por auditoria estrutural, checagem de domínios e rechecagem agregada de referências: 12 registros têm tipo/procedimento sem classificação; datas de início incluem valores posteriores ao período; relações entre autorizações/identificadores e referências anteriores não validam continuidade individual. Os seis procedimentos foram conferidos por competência nos arquivos oficiais SIGTAP de 2023–2025. Ainda é preciso tratar as exceções temporais e avaliar continuidade/identidade por APAC e paciente. Se a APAC permitir seguimento e registro de óbito, mas não houver comparador adequado, o estudo poderá estimar desfechos/prognóstico entre pessoas tratadas ou comparar modalidades com cautela; não poderá concluir o efeito da diálise versus não tratamento.

Os objetivos abaixo são perguntas de pesquisa. A existência de um campo em uma fonte ou sua adequação à pergunta só será afirmada depois da consulta correspondente.

## 9. Indicadores propostos

### Acesso à hemodiálise

- Pacientes distintos com hemodiálise por estabelecimento, município, UF e mês, caso a extração por CNES seja validada.
- Quantidade aprovada dos procedimentos selecionados por estabelecimento, UF e competência; interpretar como produção administrativa registrada.
- Indicadores por população somente quando numerador e denominador forem temporal e geograficamente compatíveis.
- Taxa populacional de pacientes distintos ou de produção, conforme a unidade validada; não apresentar quantidade de procedimentos como cobertura de pacientes.

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
4. **Associações:** explorar associação entre produção assistencial registrada e desfechos hospitalares por UF/ano, usando taxas ou modelos que considerem o tamanho populacional e potenciais fatores de confusão disponíveis.
5. **Gastos:** descrever evolução e distribuição dos valores; ajustar por inflação se a análise cobrir diferentes anos.
6. **Incerteza e robustez:** apresentar intervalos de confiança quando cabível, verificar sensibilidade a definições alternativas e evitar conclusões causais a partir de dados ecológicos observacionais.
7. **Eficácia/efetividade (somente após a porta de viabilidade):** especificar o efeito-alvo, tratamento e comparador, critérios de elegibilidade, tempo zero, seguimento, desfecho e covariáveis prognósticas; verificar comparabilidade, perdas, confundimento e vieses. Se esses requisitos não puderem ser atendidos, não interpretar associação como efeito do tratamento.

Os testes de hipótese e modelos finais serão escolhidos depois da inspeção dos dados e da definição das variáveis. A unidade de observação, a dependência temporal e a comparabilidade entre estados devem ser consideradas para evitar tratar cada mês ou UF como observação independente quando não for apropriado.

## 11. Limitações e cuidados de interpretação

- Quantidade aprovada no SIA/SUS é produção administrativa; não equivale necessariamente a número de pacientes, sessões efetivamente recebidas por indivíduo, cobertura assistencial ou adesão.
- Os arquivos CNES de 2024/12 descrevem serviço/equipamento cadastrado e foram excluídos do conjunto analítico principal; não serão usados como medida de capacidade real, vagas ou atendimento.
- O SUS 360º lista dados de hemodiálise por CNES com pacientes distintos e quantidade aprovada; esses dados ainda precisam ser baixados e validados. O painel informa que está em atualização.
- O SIH/SUS é documentado como sistema de informações hospitalares baseado em AIH; a definição operacional de internação renal e a disponibilidade/uso de campo de óbito ainda dependem da tabulação específica. Mesmo quando calculado, óbito hospitalar não deve ser interpretado como mortalidade de toda a população com doença renal nem como sobrevida de pessoas em hemodiálise.
- Dados agregados por estado, município ou estabelecimento não permitem vincular uma pessoa ao tratamento, ao acompanhamento e ao desfecho; não sustentam conclusão de eficácia/efetividade.
- Microdados anonimizados do SUS podem não conter identificador longitudinal utilizável ou variáveis suficientes para formar grupos comparáveis. A disponibilidade pública de microdados, por si só, não resolve esse requisito.
- Mortalidade hospitalar do SIH, se disponível, é óbito durante internação e não substitui seguimento de sobrevida após início da diálise. Uma taxa observada entre internados não estima o efeito do tratamento.
- Diferenças regionais podem refletir idade, prevalência, comorbidades, condições socioeconômicas, organização da rede, fluxos entre municípios/estados, qualidade do registro e outros fatores não observados.
- Meses recentes podem estar sujeitos a atualização, conforme nota do TabNet; a data de extração deve ser registrada.
- Valores financeiros nominais de anos diferentes não são diretamente comparáveis sem considerar inflação.

## 12. Situação atual e próximos passos

**Atualização de 05/11/2026 — base descritiva territorial construída:** foi criado e executado `Notebook/analise_descritiva_final_drc_sus.ipynb`. O notebook gerou arquivos novos em `Dados/03_bases_analiticas/descritiva_territorial_2024_2025/`: painel UF-mês (648 linhas), tabelas SIA e TabNet SIH separadas (648 células cada), dimensão IBGE UF-ano (54 linhas), resumo UF-ano (54 linhas), séries mensais Brasil (24) e região (120), comparação comum janeiro–novembro por UF (27) e Brasil, e três gráficos SVG. As fontes/CSVs originais não foram sobrescritos.

A validação encontrou uma célula SIH ausente/suprimida (RR, dezembro/2025); a soma observada TabNet é 309.574. A nota técnica oficial define “Internações” como AIHs aprovadas excluindo prorrogações de longa permanência, mas incluindo transferências e reinternações. Rechecagem DBC de 05/11 encontrou 213.788 linhas N18 `IDENT=1` e uma `IDENT=5`; `IDENT=1` ficou abaixo do TabNet N17–N19 em todas as 647 células preenchidas. Na janela principal janeiro–outubro, SIA variou +3,85% e SIH N17–N19 +4,04% entre as 27 UFs. Novembro e dezembro SIH tiveram quedas amplas (−19,22% e −48,59%) e foram marcados como possível problema de maturidade/atualização; excluí-los dos testes mensais não determina a causa. Testes exploratórios e correlações por UF estão implementados no notebook principal; a população IBGE é referência anual em 1º de julho e as taxas usadas são ecológicas, não mensais ou individuais. N18 continua preliminar e excluído do painel/totalizações.

A auditoria adicional de referências APAC leu os 648 arquivos sem exportar chaves: 81.416 pares distintos `AP_AUTORIZ`→`AP_APACANT`, dos quais 40.170 são autorreferências; 10.756 alvos não aparecem no recorte. Entre 149.406 linhas `AP_TPAPAC=2` sem referência anterior, o campo não permite reconstruir toda continuidade. A identidade e a continuidade seguem não validadas; detalhes em `Dados/04_documentacao_e_auditoria/LEIA-ME_APAC_ATD_2024_2025.md`.

**Situação do objetivo:** a preparação para análise descritiva territorial está concluída e reproduzível. A avaliação de efetividade permanece não realizada e não é sustentada pelas bases atuais: faltam comparador clínico validado, elegibilidade, tempo zero, seguimento, desfechos adequados e controle de confundimento. Para detalhes do dataset e campos, consultar `Dados/04_documentacao_e_auditoria/LEIA-ME_BASE_DESCRITIVA_TERRITORIAL_2024_2025.md`.

### Pendências prioritárias atuais

1. Revisar e incorporar ao relatório as tabelas/gráficos descritivos, preservando a distinção entre produção aprovada SIA e internações N17–N19 SIH.
2. Manter a reconciliação N18/TabNet delimitada como não resolvida: diferença de 12 linhas entre rotinas antigas não localizada; não promover 368.917 nem a reextração de auditoria a total final.
3. Obter esclarecimento técnico das datas `ATD_DTPDR`/`ATD_DTCLI`, continuidade e estabilidade do identificador APAC; não criar coorte antes da decisão.
4. Discutir com nefrologista e epidemiologista clínico população, tratamento, comparador, tempo zero, desfecho e horizonte de seguimento.
5. Identificar fonte válida para elegíveis comparáveis e desfechos. Se inexistente, restringir formalmente o estudo ao escopo descritivo/associativo.


**Registro de andamento — 25/10/2026**

### Já realizado

- Mapeada a tabulação SIA/SUS de produção ambulatorial de hemodiálise por UF e mês para 2024–2025, com cinco códigos SIGTAP.
- Mantido o CSV organizado `Dados/02_derivados_preliminares/SIA/hemodialise_sia_sus_uf_mes_2024_2025.csv` para análise. A extração bruta redundante do SIA foi removida; os valores dos 24 meses de 2024–2025 haviam sido conferidos contra ela e coincidiram para todas as UFs.
- Salvo o registro do mapeamento em `mapeamento_hemodialise_sia_sus.md` e as referências em `referencias_bibliograficas_doenca_renal_cronica_sus.md`.
- Baixado e relacionado o CNES 2024/12 (`tbDialise`, `tbEstabelecimento` e `rlEstabServClass`); depois de avaliar seus limites, os dados foram excluídos do conjunto analítico principal e mantidos arquivados para referência.
- Localizado no SUS 360º o download de arquivos de hemodiálise por CNES, procedimento e competência (página lista 2023–2025, com pacientes distintos e quantidades aprovadas); a extração e validação ainda não foram feitas.
- Obtida e estruturada a exportação TabNet SIH/SUS N17–N19 e baixados do FTP oficial 648 DBCs SIH de 2024–2025 (27 UFs × 24 competências de processamento, 2.181.489.356 bytes). A extração N18 por `DIAG_PRINC` e data de internação gerou 368.917 registros; `MORTE` vale 1 em 33.492 e 0 em 335.425. O CSV analítico soma com a agregação UF/mês, e os 649 hashes (648 DBCs e nota técnica) foram verificados. A contagem ainda é preliminar: excede o total N17–N19 do TabNet (309.574), incluindo 120 células UF/mês acima do agrupamento amplo; precisa ser reconciliada antes do uso analítico. Documentação em `Dados/04_documentacao_e_auditoria/LEIA-ME_SIH_N18_2024_2025.md`.
- Baixadas as planilhas oficiais IBGE para 2024 e 2025, extraídos CSVs por UF e município e conferidas as somas municipais contra cada UF e as somas estaduais contra os totais Brasil.

### Etapa A — Extração e preparação dos dados

Esta etapa termina quando os arquivos necessários estiverem obtidos, documentados e validados estruturalmente. Ainda não é a etapa de testar hipóteses ou interpretar resultados.

1. **SIA/SUS — concluído:** notebook `Notebook/validacao_dados_hemodialise_sia_sus.ipynb` confere 27 UFs, 24 competências, cinco códigos SIGTAP no mapeamento e no HTML salvo, valores e totais por UF/mês/Brasil. Não interpretar produção aprovada como pacientes únicos.
2. **CNES cadastral — excluído do núcleo analítico:** manter arquivos arquivados para rastreabilidade; não usar contagem de serviços ou máquinas do perfil como capacidade real ou atendimento efetivo.
3. **SIA/APAC dialítica — extraída; auditoria estrutural, domínios e repetições feitas:** 648 arquivos ATDAC de 2024–2025 estão em `Dados/01_fontes_originais/APAC/APAC_ATD_2024_2025_bruto/`. Os seis códigos `AP_PRIPAL` observados foram encontrados em todas as 36 competências SIGTAP de 2023–2025. Na reextração de 05/11/2026, os 648 arquivos foram lidos (3.186.282 registros); foram gerados hashes SHA-256 novos, sem manifesto anterior para comparação. Os 12 registros `AP_TPAPAC=4` coincidem com procedimento principal vazio. Foram reproduzidas 146 datas `ATD_DTPDR` e 1.162 `ATD_DTCLI` posteriores a 2025; algumas têm anos muito distantes, apesar de serem datas válidas no calendário, e a semântica continua sem explicação. Repetições de autorizações, associação múltipla com identificadores, continuidade e completude do óbito seguem sem regra validada. Nenhuma coorte foi criada. Detalhes em `Dados/04_documentacao_e_auditoria/LEIA-ME_APAC_ATD_2024_2025.md`.
4. **Definir o comparador:** testar se as variáveis permitem comparar modalidades dialíticas; para comparar diálise com cuidado conservador, identificar fonte de pacientes elegíveis não dialíticos e seus desfechos. Sem grupo comparador apropriado, não estimar efeito causal.
5. **SIH/SUS N17–N19 — concluído:** notebook `Notebook/analise_sih_insuficiencia_renal.ipynb` documenta os nove meses extras de 2023, valida as 27 UFs e 24 competências-alvo e gera a cópia analítica, preservando o bruto. Uma célula de Roraima está ausente/suprimida; a soma observada de 309.574 não a substitui por zero.
6. **SIH/SUS N18 — reextraído; reconciliação histórica parcialmente esclarecida:** manter DBCs e CSVs originais. Os 648 DBCs e 649 hashes foram conferidos; o leitor local extraiu 213.789 linhas N18 no período, com 213.788 `IDENT=1` e um `IDENT=5`. O CSV preliminar de 368.917 tem 155.128 linhas a mais. As 213.688 assinaturas de campos analíticos distintas coincidem entre CSV e DBC ao ignorar UF e competência; as linhas excedentes no CSV têm payload já visto no DBC, mas incompatibilidade de UF/competência. Como o CSV não preserva `N_AIH`, não é possível afirmar que cada linha excedente seja repetição da mesma autorização. Na reextração, 213.788 `N_AIH` distintos aparecem em 213.789 registros; uma autorização repete-se em duas competências e teve mudanças em `IDENT`, data de saída, permanência e valor. Isso contradiz a exploração histórica de 140.113 repetições e 228.792 IDs distintos, que não foi reproduzida. Comparando UF local de `MUNIC_MOV`/`UF_ZI` com TabNet, N18 fica abaixo do agregado N17–N19 nas 647 células preenchidas (213.789 contra 309.574); RR/dez-2025 permanece ausente no TabNet, com zero N18 na reextração. A diferença histórica de 12 linhas continua sem localização porque o código/saída linha a linha da rotina antiga não está arquivado. Não deduplicar por `N_AIH` nem tratar N18 como pacientes únicos ou total final; ver a nota e os novos arquivos em `Dados/02_derivados_preliminares/SIH/auditoria_sih_dbc_reconciliacao_20261105_221707/`.
7. **Documentar cada arquivo:** guardar fonte, data de extração, filtros, códigos, competência/período, geografia, unidade de medida e limitações; distinguir arquivos brutos de versões analíticas.
8. **Harmonizar e validar:** alinhar códigos de UF/município, períodos, conceitos e unidades; conferir ausências, duplicidades, totalizações e compatibilidade geográfica e temporal. A população IBGE está disponível para UF e município, com referência em 1º de julho; justificar o denominador usado nas taxas mensais ou anuais.
9. **Fechar o escopo viável:** avaliar separadamente o que SIA por CNES e os dois recortes SIH permitem responder. Relacionar bases somente quando definições, geografia e períodos forem compatíveis; registrar dados que não entrarem na análise e o motivo.

**Status para a Etapa A (atualizado em 05/11/2026):** SIA agregado, IBGE e SIH N17–N19 estão disponíveis. SIH N18 foi reextraído para auditoria e permanece preliminar; N18 fica abaixo de N17–N19 nas 647 células preenchidas, mas a diferença histórica de 12 linhas não foi localizada e a a cobertura temporal/revisão dos arquivos por processamento não foi demonstrada como idêntica ao corte TabNet; a diferença histórica de 12 linhas permanece não localizada. A busca local não encontrou a rotina antiga. O script corrigido foi reexecutado nos 648 DBCs, com 649 hashes conferidos e cenário `IDENT=1` por UF/mês; N18 permanece preliminar. O Informe Técnico SIASUS 2019.07 descreve `ATD_DTPDR` e `ATD_DTCLI` como datas de início em formato AAAAMMDD, mas não explica valores posteriores ao período; APAC foi reextraída em auditoria de exceções: 12 registros não classificados e datas futuras foram reproduzidos; semântica das datas, identificador longitudinal, continuidade e completude do óbito continuam pendentes. CNES permanece fora do núcleo. Comparador e viabilidade de efetividade continuam em aberto. Os registros históricos deste planejamento que descrevem os totais antigos do SIH são contexto de auditoria, não resultados correntes.

**Ação em andamento (05/11/2026):** foi preparado um [rascunho de viabilidade comparativa](protocolo_viabilidade_comparativa_provisorio.md), com hemodiálise versus diálise peritoneal como pergunta a discutir clinicamente; não é protocolo aprovado nem estimativa viável. O Informe Técnico SIASUS 2019.07 documenta os nomes e formatos de `ATD_DTPDR`/`ATD_DTCLI`; a causa dos anos futuros/distantes continua sem explicação, e a auditoria de referências APAC encontrou autorreferências e lacunas que não permitem validar continuidade. A conclusão sobre comparador, tempo zero e desfecho requer especialista clínico; buscar cuidado conservador exige fonte adicional de elegíveis não dialíticos.

### Etapa B — Análise descritiva concluída; análises adicionais condicionadas

A preparação e a análise descritiva territorial SIA/SIH TabNet/IBGE foram executadas no notebook `Notebook/analise_descritiva_final_drc_sus.ipynb` e documentadas na nota do dataset. Análises inferenciais ou de efetividade permanecem condicionadas à definição de pergunta, unidade, comparador e disponibilidade de dados longitudinais adequados.

1. Explorar distribuições, períodos, ausências, extremos e mudanças de registro.
2. Definir indicadores, numeradores, denominadores, unidades e regras de agregação.
3. Formular perguntas e hipóteses nulas/alternativas compatíveis com o desenho observacional e as variáveis efetivamente disponíveis.
4. Escolher testes/modelos após avaliar distribuição, tamanho amostral, dependência temporal, exposição populacional e fatores de confusão disponíveis.
5. Fazer análise descritiva e comparativa; calcular intervalos de confiança quando apropriado.
6. Explorar associação entre produção assistencial registrada e desfechos hospitalares apenas se período, geografia e definições forem compatíveis. Não inferir causalidade nem sobrevida individual a partir desses dados agregados.
7. Avaliar robustez, limitações e sensibilidade a definições justificadas; apresentar tabelas, gráficos e conclusões com limites claros.

**Próximo passo recomendado:** manter documentada como não localizável a diferença histórica de 12 linhas enquanto a rotina/saída de 368.905 não for recuperada; não promover N18 ao total final. Na APAC, solicitar esclarecimento técnico das autorreferências/lacunas e dos valores futuros, e validar a estabilidade do identificador e completude do desfecho antes de qualquer seguimento. Definir comparador clínico (HD versus DP ou diálise versus cuidado conservador) e confirmar sua fonte antes de montar a tabela analítica. Os dados administrativos, por si sós, não demonstram benefício causal.

**Atualização do próximo passo — 25/10/2026:** a associação entre `AP_AUTORIZ` e `AP_CNSPCN` foi reavaliada nos 648 arquivos: as 12.065 autorizações associadas a mais de um identificador aparecem em duas competências (730) ou três (11.335), sempre atravessando competências. Portanto, a autorização não pode ser tomada como chave de pessoa; ainda é preciso confirmar as regras de continuidade e a estabilidade do identificador pseudonimizado. Seguem sinalizados 146 valores de `ATD_DTPDR` e 1.162 de `ATD_DTCLI` posteriores ao fim de 2025; esses campos ficam fora de qualquer análise até validação. O acesso FTP foi restabelecido e os 36 arquivos SIGTAP oficiais de 2023–2025 foram baixados e testados; os seis códigos `AP_PRIPAL` constam em todas as 36 competências. A extração compacta, os arquivos integrais e os hashes estão em `Dados/01_fontes_originais/SIGTAP/SIGTAP_2023_2025/`. Não foi criada coorte nem estimativa de sobrevida. **Ação imediata:** tratar os registros sem classificação e auditar as datas futuras com o layout oficial; depois definir unidade de análise e comparador antes de derivar a base analítica.

## 13. Referências oficiais consultadas

- Ministério da Saúde/DATASUS. [Produção Ambulatorial do SUS — notas técnicas do SIA/SUS](https://tabnet.datasus.gov.br/cgi/sia/padescr.htm). Documenta origem dos dados e variáveis de tabulação.
- Ministério da Saúde/DATASUS. [TabNet — produção ambulatorial por local de atendimento](https://tabnet.datasus.gov.br/cgi/deftohtm.exe?sia/cnv/qabr.def). Tabulação usada para mapear a extração de hemodiálise. A consulta efetiva e os filtros estão documentados no arquivo de mapeamento.
- Ministério da Saúde/DATASUS. [CNES — documentação do SCNES](https://cnes.datasus.gov.br/pages/downloads/documentacao.jsp) e [consulta de serviços especializados](https://cnes2.datasus.gov.br/mod_ind_especialidades.asp). A extração CNES 2024/12 foi excluída do núcleo analítico e está documentada em `Dados/04_documentacao_e_auditoria/LEIA-ME_CNES_dialise_2024_12.md`.
- Ministério da Saúde/DATASUS. [Documentação e arquivos APAC do SIA/SUS](https://sia.datasus.gov.br/documentos/listar_ftp_apac.php) e [diretório público de arquivos SIASUS](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/). Os arquivos ATDAC de 2024–2025 foram baixados; cobertura e campos estão auditados em `Dados/04_documentacao_e_auditoria/LEIA-ME_APAC_ATD_2024_2025.md`. A validação semântica e analítica continua pendente.
- Ministério da Saúde. [Portaria de Consolidação SAES/MS nº 1/2022 — controle de frequência individual de tratamento dialítico](https://bvsms.saude.gov.br/bvs/saudelegis/saes/2022/prc0001_31_03_2022.html). Estabelece o CFID para comprovar mensalmente a realização dos procedimentos dialíticos e condiciona o faturamento APAC à conferência e validação do CFID.
- Ministério da Saúde/SAES. [SUS 360º — Monitor de Hemodiálise](https://sus360.saude.gov.br/painel/hemodialise/). Fonte agregada por CNES para contexto/validação, não trajetória individual; download não prioritário para o objetivo de efetividade.
- Ministério da Saúde. [Obter microdados anonimizados oriundos do SUS](https://www.gov.br/pt-br/servicos/obter-aplicativos-documentos-e-microdados-anonimizados-oriundos-do-sus). Fonte oficial sobre o serviço de disseminação; não garante identificador longitudinal nos arquivos de cada sistema.
- Ministério da Saúde/REBRATS. [Diretrizes metodológicas: estudos de avaliação econômica de tecnologias em saúde](https://rebrats.saude.gov.br/diretrizes-metodologicas?download=62%3Aestudos-de-avaliacao-economica-de-tecnologias-em-saude). Referência consultada para distinguir eficácia em condições controladas e efetividade em condições usuais.
- Ministério da Saúde/DATASUS. [Procedimentos hospitalares do SUS — notas técnicas do SIH/SUS](https://tabnet.datasus.gov.br/cgi/sih/Proced_hosp_loc_int_2008.pdf). Documentação do sistema; a tabulação renal específica continua pendente.
- IBGE. [Estimativas da população residente — referência de 1º de julho de 2024, edição atualizada em 30/12/2024 (PDF)](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2024/POP2024_20241230.pdf) e [planilha ODS](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2024/POP2024_20241230.ods).
- IBGE. [Estimativas da população residente — referência de 1º de julho de 2025, edição atualizada em 28/08/2026 (PDF)](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20260828.pdf) e [planilha ODS](https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20260828.ods).
- IBGE. [Produto Estimativas da População — conceitos e edições](https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html).
- Ministério da Saúde. [SIGTAP — Sistema de Gerenciamento da Tabela de Procedimentos, Medicamentos e OPM do SUS](https://sigtap.datasus.gov.br/tabela-unificada/app/sec/inicio.jsp). Referência para conferência dos códigos e descrições dos procedimentos selecionados.
- Ministério da Saúde/DATASUS. [Diretório FTP oficial das tabelas SIGTAP](ftp://ftp2.datasus.gov.br/pub/sistemas/tup/downloads/). Foram baixadas as 36 competências de 2023–2025 e conferidos os seis códigos observados na APAC; detalhes e hashes em `Dados/01_fontes_originais/SIGTAP/SIGTAP_2023_2025/`.

**Acesso às fontes conferido em 24/10/2026.** A data de acesso não substitui a data de extração dos dados; esta deverá ser registrada para cada arquivo baixado.
