# Plano de análise estatística — produção de hemodiálise e internações por insuficiência renal no SUS

> **Escopo final adaptado em 15/11/2026:** os insumos externos não estão disponíveis. O estudo será concluído com o painel local SIA/SIH/IBGE de 2024–2025. Novas extrações, resposta do DATASUS, coorte APAC e validação N18 são possibilidades para trabalhos futuros, sem constituir pendências desta entrega. O nome dos arquivos mantém “DRC” para preservar os caminhos; o objeto medido é produção de hemodiálise e internações N17–N19, não a carga específica de DRC.

## 1. Apresentação do projeto e problema

O estudo descreve a produção aprovada de procedimentos de hemodiálise no SIA/SUS e as internações por insuficiência renal N17–N19 no SIH/TabNet. A base final reúne informações por Unidade da Federação (UF) e mês, entre janeiro de 2024 e dezembro de 2025.

O problema é identificar padrões temporais e territoriais desses registros sem confundir contagens administrativas com pessoas atendidas. A análise considera uma célula SIH ausente e a possível incompletude de novembro/dezembro de 2025. Como não há insumo para esclarecer esses meses, eles ficam definitivamente fora das comparações principais desta versão; permanecem apenas na descrição sinalizada da extração disponível.

## 2. Objetivo

Quantificar a magnitude e a distribuição territorial das mudanças nos registros SIA e SIH entre 2024 e 2025, descrever a produção SIA por população anual, explorar a concordância entre mudanças estaduais e comparar retrospectivamente modelos simples de previsão SIA. As respostas principais serão medidas observadas; testes e intervalos entram como apoio exploratório condicionado aos seus modelos de referência.

**Ampliação da proposta — aprofundamento analítico executado:** explorar os dados para identificar e caracterizar padrões territoriais e temporais, conectando as observações às metodologias estatísticas aplicadas. A proposta já foi incorporada à introdução e aos objetivos do notebook; sua exploração e síntese sistemáticas foram desenvolvidas conforme a seção 12.3.

### Objetivos específicos

1. Verificar qualidade, cobertura e ausência de dados do painel UF-mês.
2. Resumir as variáveis principais por UF, região, mês e ano.
3. Estimar a probabilidade empírica de aumento entre 2024 e 2025.
4. Testar mudanças direcionais e associações ecológicas entre SIA e SIH.
5. Avaliar diferenças regionais com ANOVA ou Kruskal–Wallis, conforme os pressupostos.
6. Comparar modelos de previsão SIA por desempenho retrospectivo de um mês à frente, sem prometer precisão futura ou uso operacional.

## 3. Base e unidade de análise

- **Base:** `Dados/03_bases_analiticas/descritiva_territorial_2024_2025/painel_descritivo_uf_mes_2024_2025.csv`.
- **Unidade de análise:** UF-mês.
- **Cobertura esperada:** 27 UFs × 24 meses = 648 observações.
- **Janela inferencial principal:** janeiro a outubro de cada ano. Novembro e dezembro de 2025 ficam fora dos testes SIH por indício de atualização incompleta.

## 4. Variáveis e decisões de uso

| Variável | Papel | Decisão |
|---|---|---|
| Quantidade aprovada SIA | Desfecho descritivo e série de previsão | Mantida; é completa no período. |
| Internações SIH N17–N19 | Indicador descritivo e associativo | Mantida observada; imputação apenas em sensibilidade. Não será prevista enquanto houver dúvida de completude no fim de 2025. |
| População IBGE anual | Denominador territorial | Mantida para taxa anual por 100 mil habitantes; não usada como denominador mensal. |
| UF, região, ano e mês | Estratificação e identificação | Mantidos; organizam tabelas, gráficos e comparações. |
| Código e sigla da UF | Chave e rótulo | Não usados como variável numérica ou preditor. |
| N18 | Fora da análise | O painel adota N17–N19 TabNet; a equivalência operacional com o recorte DBC N18 não foi demonstrada. |
| APAC | Fora da análise | Excluída por não haver vínculo individual e regras de continuidade validadas. |

## 5. Tratamento de dados ausentes

Há uma ausência SIH: Roraima, dezembro de 2025. A base original não será alterada. Será criada uma cópia analítica com **imputação sazonal ajustada**:

`SIH_RR_dez_2025 = SIH_RR_dez_2024 × (total_RR_jan_out_2025 / total_RR_jan_out_2024)`.

O método preserva o padrão de dezembro da própria UF e usa a janela janeiro–outubro adotada para comparação, cuja maturidade não foi confirmada externamente. Ele evita usar médias de outras UFs, que poderiam mascarar diferenças territoriais. A imputação será usada **somente em análise de sensibilidade**; as tabelas, gráficos e testes principais manterão a célula como ausente. A célula imputada não participará dos testes principais, pois a janela principal encerra em outubro.

## 6. Etapas da análise

### 6.1 Qualidade e cobertura

1. Conferir número de linhas, chaves únicas e cobertura de UFs por competência.
2. Identificar valores ausentes e registrar a regra de imputação.
3. Confirmar que SIA e SIH possuem valores não negativos.
4. Exibir uma tabela de cobertura mensal SIH.

### 6.2 Análise descritiva

1. Calcular média, mediana, desvio-padrão, mínimo, máximo e quartis de SIA e SIH.
2. Somar SIA e SIH por mês para o Brasil.
3. Comparar totais janeiro–outubro de 2024 e 2025 por UF.
4. Calcular variação absoluta e percentual por UF.
5. Calcular taxa anual SIA por 100 mil habitantes para comparação territorial.

**Tabelas:** resumo numérico, cobertura, ranking de variações por UF, taxa anual por UF e taxa anual por região.

**Gráficos:** série mensal Brasil, barras de variação por UF, dispersão SIA × SIH, barras da taxa anual regional SIA e boxplot regional da variação percentual SIA.

### 6.3 Estudo de probabilidades

O experimento consiste em escolher uma das 27 UFs com probabilidades iguais e comparar janeiro–outubro de 2025 com o mesmo período de 2024. A seção 7 do notebook define o espaço amostral, os eventos A (aumento SIA) e B (aumento SIH) e apresenta cinco subseções, cada uma com pergunta, fórmula, cálculo executável, resultado exibido e interpretação em Markdown:

1. Aumento SIA: P(A) = 25/27 = 92,59%.
2. Aumento SIH: P(B) = 17/27 = 62,96%.
3. Aumento simultâneo: P(A ∩ B) = 15/27 = 55,56%.
4. Pelo menos um aumento: P(A ∪ B) = 27/27 = 100%; conferir pela inclusão–exclusão.
5. Dupla redução: 0/27 = 0%; redução exige variações estritamente negativas, não incluindo empates.

A interseção é contada diretamente, sem pressupor independência. Os eventos se sobrepõem e suas probabilidades não devem ser somadas como uma partição. O quadro-resumo é exportado em `probabilidades_basicas.csv`.

Os intervalos binomiais exatos de 95% para as duas probabilidades marginais são mantidos em uma subseção complementar. As proporções descrevem o conjunto observado de UFs; os intervalos dependem do modelo de referência e não representam erro amostral de um censo territorial. Probabilidades de 0% e 100% descrevem esta comparação e não são garantias sobre outros períodos ou sobre pessoas.

### 6.4 Inferência estatística

1. Aplicar teste binomial de sinais para verificar se aumentos e reduções entre UFs ocorrem em proporções diferentes de 50%.
2. Aplicar correlação de Spearman entre as variações percentuais de SIA e SIH por UF.
3. Ajustar pelo método de Holm a família de três testes do notebook 09: sinais SIA, sinais SIH e Spearman entre as duas variações. Resultados ajustados de outras famílias, como as do notebook 04, não são diretamente intercambiáveis.
4. Reportar estatística, p-valor bruto, p-valor ajustado e conclusão exploratória ao nível de 5%.

Os testes descrevem o conjunto completo das 27 UFs observadas, não uma amostra probabilística de pessoas ou serviços. P-valores e intervalos quantificam compatibilidade com os modelos de referência, sem sustentar generalização causal.

### 6.5 Avaliação de ANOVA

Comparar, de forma exploratória, a **variação percentual SIA de janeiro–outubro entre 2024 e 2025** nas cinco regiões. Cada UF entra uma vez; isso evita tratar a mesma UF nos dois anos como observações independentes.

1. Testar normalidade em cada região com Shapiro–Wilk.
2. Testar homogeneidade das variâncias com Levene.
3. Se os pressupostos forem atendidos, interpretar a ANOVA de uma via.
4. Se algum pressuposto falhar, interpretar o teste não paramétrico de Kruskal–Wallis.

Kruskal–Wallis compara distribuições por postos; com dispersões diferentes, não deve ser interpretado como teste isolado de medianas. A ausência de significância não demonstra igualdade regional. Os grupos regionais têm poucos estados, especialmente o Sul (3 UFs) e o Centro-Oeste (4 UFs). Portanto, o resultado é complementar e descritivo; não substitui um modelo longitudinal com efeito de UF caso haja mais anos disponíveis.

### 6.6 Previsão exploratória

Prever somente a série nacional SIA, pois a série está completa. Há somente 24 competências, portanto a previsão terá finalidade didática/exploratória, sem uso operacional. Comparar três modelos com validação de origem móvel: cada competência de 2025 é prevista apenas com meses anteriores.

| Modelo | Regra |
|---|---|
| Média móvel | Média dos três meses anteriores. |
| Tendência linear | Regressão linear do total mensal contra o tempo. |
| Ingênuo sazonal | Repete o valor do mesmo mês do ano anterior. |

A validação contém 12 previsões de **um mês à frente**, com histórico crescente. Esse desempenho não valida os 12 meses projetados de uma única origem ao fim de 2025. Como o modelo é selecionado e avaliado na mesma janela, não há avaliação final independente do modelo escolhido. A presença das 24 competências SIA indica cobertura estrutural, sem comprovar encerramento administrativo ou ausência de revisões.

**Critérios de seleção:** menor MAPE calculado sobre os valores observados da validação; em caso de empate, menor MAE. RMSE será apresentado como medida complementar. O modelo escolhido gera somente um cenário ilustrativo para 2026, condicionado à estabilidade do registro administrativo e sem intervalo preditivo confiável com a série curta.

## 7. Ordem de apresentação

1. Contexto, problema, objetivo e limites.
2. Base, unidade de análise e variáveis.
3. Qualidade, cobertura e imputação.
4. Tabelas e gráficos descritivos.
5. Probabilidade e intervalos de confiança.
6. Testes de hipóteses, correlação e avaliação regional.
7. Comparação dos modelos e projeção SIA.
8. Conclusão, limites e próximos passos.

## 8. Comunicação e limites

Os gráficos usam azul para SIA, laranja para SIH, verde para resultados de apoio e vermelho para alertas de qualidade. Cada tabela e gráfico deve conter título, unidade de medida e período analisado. O relatório final apresenta os períodos, unidades e fontes nas seções e legendas; as figuras indicam a cobertura SIH e o alcance do cenário SIA.

Os resultados não estimam número de pacientes, acesso, efetividade ou causalidade. SIA e SIH não podem ser vinculados por pessoa. N18 permanece fora dos totais, e a previsão não deve ser usada para decisão operacional sem atualização e nova validação dos dados.

## 9. Entrega

O plano é implementado no notebook `Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb`, com comentários curtos, células em ordem de execução e resultados reprodutíveis.

## 10. Status do que já foi desenvolvido

### 10.1 Etapas concluídas e documentadas

| Entrega | Evidência | Status |
|---|---|---|
| Validação da extração SIA | `Notebook/01_VALIDACAO_SIA_hemodialise.ipynb` | Concluída: cobertura temporal, UFs, totais e filtros SIGTAP conferidos. |
| Tratamento SIH N17–N19 | `Notebook/02_TRATAMENTO_SIH_TabNet_N17_N19.ipynb` | Concluído para o painel: células tratadas e cópia analítica produzida. |
| Validação de população IBGE por UF | `Notebook/03_VALIDACAO_IBGE_populacao_UF.ipynb` | Concluída: população anual e totais territoriais conferidos. |
| Painel integrado UF-mês | `Notebook/04_TRATAMENTO_E_ANALISE_base_final_DRC.ipynb` | Concluído: 648 chaves UF-mês, 54 chaves UF-ano e arquivos analíticos gerados. |
| Descrição, gráficos e testes exploratórios | `Notebook/04...` e arquivos em `Dados/03_bases_analiticas/...` | Concluídos: séries Brasil/região, comparações janeiro–outubro, teste de sinais, Spearman e Holm. |
| Auditoria N18/DBC | `Notebook/05_AUDITORIA_SIH_DBC_N18.ipynb` | Executada como auditoria; N18 permanece excluído do painel e dos totais finais. |
| Estrutura CNES de diálise | `Notebook/06_ANALISE_CNES_dialise_202412.ipynb` | Concluída como análise complementar de uma competência. |
| Validação municipal IBGE | `Notebook/07_ANALISE_IBGE_populacao_municipio.ipynb` | Concluída como apoio territorial. |
| Auditoria APAC e decisão de uso SIH | `Notebook/08_AUDITORIA_APAC_e_proximas_etapas_SIH.ipynb` | Executada; não fornece coorte individual apta para efetividade. |

### 10.2 Entregas executadas

| Entrega | Situação atual | Próxima ação |
|---|---|---|
| Notebook de análise final | Executado em ordem; saídas gravadas no notebook. | Reexecutar somente após atualização das fontes ou do código. |
| Imputação sazonal ajustada | Sensibilidade executada: RR/dez-2025 = 27; fator jan–out = 0,704; total SIH 2025 passa de 153.083 para 153.110. | Manter tabelas, gráficos e testes principais sem imputação. |
| Comparação regional | Levene p=0,037; Kruskal–Wallis é o método indicado (p=0,248). | Manter interpretação exploratória; não há evidência de diferença regional nesta análise. |
| Seleção de modelo SIA | Tendência linear venceu a validação móvel: MAPE 3,01%, MAE 46.849 e RMSE 62.453. | Tratar a projeção de 2026 apenas como cenário exploratório. |

### 10.3 Decisão de encerramento com as fontes disponíveis

As limitações SIH, APAC e N18 permanecem documentadas, mas não serão tratadas como tarefas bloqueadoras. Para esta entrega, a comparação principal fica fixada em janeiro–outubro de ambos os anos. Novembro/dezembro SIH permanecem apenas na descrição da extração, com alerta; RR/dezembro continua ausente, e a imputação é apenas demonstração de sensibilidade. Não se atribui causa à queda no fim de 2025.

APAC e N18 ficam excluídos do conjunto analítico final. Não haverá coorte, comparador clínico ou estimativa de mortalidade, sobrevida ou efetividade. A auditoria já realizada justifica essas exclusões; não é necessário aguardar nova especificação para encerrar o estudo.

A avaliação retrospectiva SIA é uma entrega estatística válida com os 24 meses disponíveis. O cenário de 2026 é apenas ilustração de extrapolação a partir do corte de dezembro de 2025, mesmo que parte desse ano já tenha transcorrido na data de redação. Sem observações de 2026 nesta base, não será chamado de previsão atualizada ou validada para esse ano.

O [registro de limitações](Dados/04_documentacao_e_auditoria/PENDENCIAS_EXTERNAS_E_METODOLOGICAS_2026-11-15.md) preserva a auditoria histórica. Seus encaminhamentos externos passam a ser sugestões para outro ciclo de pesquisa.

## 11. Revisão metodológica e interpretação consolidada — 15/11/2026

As células de código do notebook 09 foram executadas em ordem com a base local, sem alterar os dados originais. A conferência reproduziu 648 chaves UF-mês, 27 UFs, 24 competências e uma ausência SIH (RR/dezembro de 2025). A conferência inicial usou modo não interativo. O fechamento posterior executou o notebook em kernel Jupyter, salvou as saídas e inspecionou visualmente os seis PNGs; as evidências estão no [registro de fechamento](Dados/04_documentacao_e_auditoria/REGISTRO_FECHAMENTO_ESTATISTICO_2026-11-15.md).

### 11.1 Respostas às perguntas do estudo

| Pergunta | Resultado conferido | Interpretação |
|---|---|---|
| Como os volumes nacionais mudaram? | Janeiro–outubro: SIA +3,85%; SIH +4,04%, em 2025 frente a 2024. | Crescimento de registros agregados; não mede crescimento do número de pacientes ou efeito do tratamento. |
| Qual a frequência territorial de aumento? | SIA: 25/27 UFs, 92,6% (IC exato 95%: 75,7%–99,1%); SIH: 17/27, 63,0% (42,4%–80,6%). | As proporções são observadas no conjunto das UFs. Os intervalos dependem do modelo binomial de referência; não são erro amostral de um censo territorial. |
| Há predomínio direcional de aumento? | SIA: p-Holm ≈ 0,000017; SIH: p-Holm ≈ 0,427. | Evidência exploratória de predomínio de aumento SIA. Para SIH, não se rejeita a referência de 50%; isso não demonstra estabilidade. |
| As variações estaduais SIA e SIH se associam? | Spearman ρ = −0,247; p bruto ≈ 0,214; p-Holm ≈ 0,427. | Não há evidência suficiente de associação monotônica nesta comparação de 27 UFs. Não se conclui independência nem relação protetora. |
| As regiões diferem na variação SIA? | Levene p = 0,037; Kruskal–Wallis p = 0,248. | Não há evidência suficiente de diferença entre distribuições regionais nesta análise. Grupos pequenos e dispersões distintas limitam a interpretação. |
| Qual modelo teve melhor desempenho? | Tendência linear: MAPE 3,01%, MAE 46.849 e RMSE 62.453 unidades de quantidade aprovada. | Melhor desempenho entre os três candidatos nas 12 previsões de um mês à frente de 2025; não garante desempenho em 2026. |

Os p-valores de Holm desta tabela pertencem exclusivamente à família de três testes do notebook 09. A dependência espacial entre UFs e o caráter censitário territorial limitam a interpretação inferencial; os testes não estabelecem causalidade.

### 11.2 Conclusão do escopo atual

Entre janeiro e outubro de 2025, a produção aprovada de hemodiálise e as internações N17–N19 aumentaram nacionalmente em relação ao mesmo período de 2024. O aumento SIA ocorreu em 25 UFs, enquanto o SIH apresentou direções mais heterogêneas. Não foi identificada evidência suficiente de associação entre as variações estaduais dos dois indicadores ou de diferença regional da variação SIA. Esses achados descrevem registros administrativos e não permitem atribuir mudanças a acesso, prevalência, qualidade assistencial ou efetividade terapêutica. O indicador hospitalar N17–N19 abrange insuficiência renal aguda, crônica e não especificada; portanto, não é uma medida específica de DRC.

A tendência linear é a referência selecionada para o cenário ilustrativo SIA de 2026. A série curta, a seleção na própria janela de avaliação e a diferença entre o horizonte validado e o projetado impedem interpretar MAPE de 3,01% como precisão garantida do cenário anual. A imputação de RR/dezembro acrescenta 27 registros apenas à sensibilidade e não resolve a possível incompletude SIH de novembro/dezembro.

## 12. O que deve ser concluído

### 12.1 Fechamento da entrega com as fontes atuais

- [x] Conferir cálculos e execução sequencial do notebook 09 contra o plano.
- [x] Consolidar respostas às perguntas, conclusão e limites metodológicos no plano e na síntese do notebook.
- [x] Revisar visualmente os gráficos e conferir conteúdo/estrutura das tabelas do notebook: legibilidade, período, unidade, legendas e alerta de cobertura SIH. O alcance da inspeção está descrito no registro de fechamento.
- [x] Consolidar a versão final do relatório acadêmico, incorporando os resultados do notebook 09, métodos, referências e limitações; conferir coerência com a síntese territorial existente, inclusive as famílias de testes distintas.
- [x] Conferir a entrega final após a revisão editorial: executar o notebook no kernel Jupyter, salvar as saídas e registrar versões das dependências e identificação da base usada.

Fechamento realizado sem reabrir a auditoria APAC/N18. O [relatório final](relatorio_final_analise_estatistica_drc_2024_2025.md) consolida métodos, resultados, seis figuras, conclusão e referências. O notebook foi executado em kernel Jupyter com 19 células de código sequenciais, sem erros; 17 CSVs, seis PNGs, HTML e identificação SHA-256/ambiente estão nos [artefatos finais](Dados/03_bases_analiticas/analise_estatistica_final_2024_2025/LEIA-ME.md). Consulte o registro para o alcance da revisão das tabelas e figuras.

### 12.2 Pesquisas futuras — fora dos critérios de conclusão

Uma futura atualização SIH poderá investigar as revisões de novembro/dezembro; uma série SIA mais longa poderá permitir nova avaliação preditiva; documentação técnica adicional poderá reabrir APAC e N18. Nenhuma dessas possibilidades integra o trabalho necessário à conclusão desta versão. A solicitação ao DATASUS permanece como minuta histórica, sem envio nesta adaptação.

### 12.3 Concluído — aprofundamento da exploração e identificação de padrões

**Proposta:** além de transformar registros administrativos em respostas estatísticas, explorar o painel disponível para identificar tendências, oscilações mensais, contrastes territoriais e possíveis associações, aplicando metodologias estatísticas e interpretando suas evidências.

**Situação:** seção 6.4 do notebook 09 implementada com novas tabelas descritivas e síntese interpretativa na discussão. Perguntas, unidade, método e limites foram explicitados antes dos cálculos. A seção 4.6 do relatório incorpora a síntese. Sete CSVs adicionais permitem conferir as evidências; nenhuma fonte original ou família de testes foi alterada.

- [x] Revisar as perguntas exploratórias e relacionar cada uma aos dados, à unidade de análise e ao método já aplicado ou necessário; justificar previamente qualquer análise adicional.
- [x] Explorar tendências e oscilações mensais da série SIA e da janela SIH utilizável, distinguindo padrões observados de possíveis efeitos de cobertura e atualização administrativa.
- [x] Examinar contrastes entre UFs e regiões, concentrações de volume e valores extremos, considerando conjuntamente magnitudes absolutas, relativas e produção SIA por população anual.
- [x] Aprofundar a interpretação das mudanças conjuntas e divergentes entre SIA e SIH, articulando probabilidades, dispersão e correlação, sem pressupor independência ou causalidade.
- [x] Consolidar uma síntese dos padrões: pergunta, evidência numérica/gráfica, metodologia, interpretação e limitação; registrar também perguntas para as quais a evidência foi insuficiente.
- [x] Incorporar essa síntese à discussão e à conclusão do notebook e do relatório; se houver novos cálculos, executar as células afetadas, atualizar os artefatos e documentar a validação.

**Critério de conclusão:** cada padrão relatado deve estar apoiado em tabela, gráfico ou cálculo reproduzível, com unidade/período explícitos e interpretação proporcional à evidência. As observações exploratórias podem gerar hipóteses; não constituem confirmação independente. A série de 24 meses não permite presumir sazonalidade estável. Não ampliar a família de testes apenas para procurar significância.

A etapa utiliza os dados locais e não depende de novas fontes, de APAC ou da equivalência operacional N18/TabNet.

## 13. O que a estatística entrega com os dados disponíveis

### 13.1 Pergunta central e respostas observáveis

**Pergunta central:** como a produção aprovada de hemodiálise e as internações por insuficiência renal N17–N19 se distribuíram e variaram entre UFs, regiões e períodos comparáveis de 2024–2025 na extração disponível?

| Resposta possível | Entrega estatística | Leitura substantiva permitida |
|---|---|---|
| Quanto mudou no Brasil? | Totais, diferenças absolutas e percentuais em janeiro–outubro. SIA: +585.014 (+3,85%); SIH: +5.284 (+4,04%). | Dimensiona a mudança do volume registrado em períodos equivalentes. |
| O aumento foi disseminado ou concentrado em poucas UFs? | Frequência de direções, mediana e extremos das variações. SIA: 25 aumentos e 2 reduções; SIH: 17 aumentos e 10 reduções. | Distingue crescimento nacional e disseminação territorial. Cada UF pesa uma vez na frequência; o total nacional é ponderado pelos volumes. |
| Onde as mudanças foram maiores? | Ranking de diferenças absolutas e percentuais; comparação regional e gráficos por UF. | Identifica contrastes observados, sem transformar posição no ranking em qualidade assistencial. Bases pequenas podem produzir percentuais extremos. |
| Como comparar produção em territórios de tamanhos distintos? | Quantidade anual SIA por 100 mil habitantes, usando população do mesmo ano; taxa regional calculada pela razão das somas. | Compara intensidade bruta de produção por população. Não equivale a prevalência, cobertura ou necessidade atendida; não há padronização etária. |
| As duas mudanças territoriais acompanharam-se? | Dispersão e Spearman das variações: ρ = −0,247, sem evidência suficiente após Holm. | Descreve concordância monotônica entre mudanças agregadas; não mede o efeito da hemodiálise sobre internações. |
| Qual regra simples antecipou melhor um mês da série SIA? | Validação móvel em 2025: tendência linear, MAPE 3,01%; média móvel, 3,53%; ingênuo sazonal, 3,59%. | Responde sobre desempenho retrospectivo entre os três candidatos e o horizonte de um mês, condicionado à extração usada. |

### 13.2 Hierarquia de evidência e interpretação

1. **Resultado principal:** magnitude, direção, distribuição e cobertura dos registros observados. O painel tem 648 linhas, mas as comparações anuais e regionais usam 27 UFs e a previsão usa 24 totais nacionais mensais; não se apresenta 648 como tamanho amostral dos testes.
2. **Apoio exploratório:** testes de sinais, Spearman e comparação regional. P-valores e intervalos são condicionados aos modelos de referência, com limitações por dependência entre UFs, grupos pequenos e multiplicidade. Não significância significa evidência insuficiente, não equivalência.
3. **Exercício preditivo:** comparação retrospectiva de três regras, seguida de cenário ilustrativo. Não há avaliação final independente após seleção nem validação dos 12 meses futuros em uma única origem.
4. **Limites definitivos desta versão:** não estimar pacientes, incidência/prevalência de DRC, necessidade não atendida, causa das mudanças, efeito terapêutico, sobrevida ou demanda operacional futura.

Não serão acrescentados testes apenas para procurar significância. Nenhuma imputação substituirá observações principais, e nenhuma nova modelagem será necessária para sustentar as respostas descritivas já disponíveis.

### 13.3 Critério de estudo concluído

O estudo estará concluído quando o relatório responder às perguntas da seção 13.1 com as tabelas e figuras existentes, explicar as limitações da seção 13.2 e permitir reproduzir os resultados com o painel local identificado. A revisão visual/editorial, o relatório e a execução final documentada da seção 12.1 foram concluídos; a base e os resultados permanecem limitados ao corte disponível. O aprofundamento exploratório e sua síntese da seção 12.3 também foram executados e incorporados à discussão e à conclusão. A obtenção de insumos externos deixa de integrar o checklist de conclusão.


## 14. Entrega final e evidências

- [Relatório acadêmico consolidado](relatorio_final_analise_estatistica_drc_2024_2025.md).
- [Notebook 09](Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb), com saídas de execução Jupyter salvas.
- [Artefatos e reprodução](Dados/03_bases_analiticas/analise_estatistica_final_2024_2025/LEIA-ME.md).
- [Registro de fechamento, ambiente e revisão](Dados/04_documentacao_e_auditoria/REGISTRO_FECHAMENTO_ESTATISTICO_2026-11-15.md).

A entrega anterior foi concluída para o escopo descritivo/ecológico então definido. A ampliação da proposta foi desenvolvida na seção 12.3, com evidências reproduzíveis e síntese dos padrões, sem exigir novas fontes externas. O conjunto de resultados não sustenta ampliação clínica ou operacional das conclusões.

### Evidências do aprofundamento da seção 12.3

- [Síntese dos padrões, métodos e limites](Dados/03_bases_analiticas/analise_estatistica_final_2024_2025/sintese_padroes_exploratorios.md).
- Cálculos: seção 6.4 do notebook; discussão: seção 10 e seção 4.6 do relatório.
- Validação: registro de fechamento, adendo do aprofundamento; as limitações externas continuam como pesquisas futuras.
