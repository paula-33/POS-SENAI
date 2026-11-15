# Plano de análise estatística e previsão — DRC no SUS

## 1. Apresentação do projeto e problema

O estudo descreve a produção aprovada de procedimentos de hemodiálise no SIA/SUS e as internações por insuficiência renal N17–N19 no SIH/TabNet. A base final reúne informações por Unidade da Federação (UF) e mês, entre janeiro de 2024 e dezembro de 2025.

O problema é identificar padrões temporais e territoriais desses registros sem confundir contagens administrativas com pessoas atendidas. A análise deve ainda lidar de forma transparente com uma célula SIH ausente e com a possível incompletude de novembro/dezembro de 2025.

## 2. Objetivo

Descrever a variação de registros SIA e SIH entre UFs e competências, quantificar incertezas estatísticas, comparar padrões regionais e selecionar um modelo simples e reproduzível para previsão exploratória da produção SIA.

### Objetivos específicos

1. Verificar qualidade, cobertura e ausência de dados do painel UF-mês.
2. Resumir as variáveis principais por UF, região, mês e ano.
3. Estimar a probabilidade empírica de aumento entre 2024 e 2025.
4. Testar mudanças direcionais e associações ecológicas entre SIA e SIH.
5. Avaliar diferenças regionais com ANOVA ou Kruskal–Wallis, conforme os pressupostos.
6. Comparar modelos de previsão para a série mensal SIA e selecionar o melhor por desempenho fora da amostra.

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
| N18 | Fora da análise | Excluída por divergência de auditoria ainda não resolvida. |
| APAC | Fora da análise | Excluída por não haver vínculo individual e regras de continuidade validadas. |

## 5. Tratamento de dados ausentes

Há uma ausência SIH: Roraima, dezembro de 2025. A base original não será alterada. Será criada uma cópia analítica com **imputação sazonal ajustada**:

`SIH_RR_dez_2025 = SIH_RR_dez_2024 × (total_RR_jan_out_2025 / total_RR_jan_out_2024)`.

O método preserva o padrão de dezembro da própria UF e usa apenas a janela com maturidade documentada. Ele evita usar médias de outras UFs, que poderiam mascarar diferenças territoriais. A imputação será usada **somente em análise de sensibilidade**; as tabelas, gráficos e testes principais manterão a célula como ausente. A célula imputada não participará dos testes principais, pois a janela principal encerra em outubro.

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

**Tabelas:** resumo numérico, cobertura, ranking de variações por UF e taxa por região.

**Gráficos:** série mensal Brasil, barras de variação por UF, dispersão SIA × SIH e boxplot regional da taxa SIA.

### 6.3 Aplicação de probabilidade

Estimar a probabilidade empírica de uma UF apresentar aumento de janeiro–outubro de 2025 em relação ao mesmo período de 2024:

`P(aumento) = número de UFs com variação positiva / 27`.

Apresentar intervalo de confiança exato de 95% para essa proporção, separadamente para SIA e SIH. A interpretação é territorial e descritiva; as 27 UFs não representam uma amostra aleatória de indivíduos.

### 6.4 Inferência estatística

1. Aplicar teste binomial de sinais para verificar se aumentos e reduções entre UFs ocorrem em proporções diferentes de 50%.
2. Aplicar correlação de Spearman entre as variações percentuais de SIA e SIH por UF.
3. Ajustar os p-valores da família de testes pelo método de Holm.
4. Reportar estatística, p-valor bruto, p-valor ajustado e conclusão exploratória ao nível de 5%.

Os testes descrevem o conjunto completo das 27 UFs observadas, não uma amostra probabilística de pessoas ou serviços. P-valores e intervalos quantificam compatibilidade com os modelos de referência, sem sustentar generalização causal.

### 6.5 Avaliação de ANOVA

Comparar, de forma exploratória, a **variação percentual SIA de janeiro–outubro entre 2024 e 2025** nas cinco regiões. Cada UF entra uma vez; isso evita tratar a mesma UF nos dois anos como observações independentes.

1. Testar normalidade em cada região com Shapiro–Wilk.
2. Testar homogeneidade das variâncias com Levene.
3. Se os pressupostos forem atendidos, interpretar a ANOVA de uma via.
4. Se algum pressuposto falhar, interpretar o teste não paramétrico de Kruskal–Wallis.

Os grupos regionais têm poucos estados, especialmente o Centro-Oeste. Portanto, o resultado é complementar e descritivo; não substitui um modelo longitudinal com efeito de UF caso haja mais anos disponíveis.

### 6.6 Previsão exploratória

Prever somente a série nacional SIA, pois a série está completa. Há somente 24 competências, portanto a previsão terá finalidade didática/exploratória, sem uso operacional. Comparar três modelos com validação de origem móvel: cada competência de 2025 é prevista apenas com meses anteriores.

| Modelo | Regra |
|---|---|
| Média móvel | Média dos três meses anteriores. |
| Tendência linear | Regressão linear do total mensal contra o tempo. |
| Ingênuo sazonal | Repete o valor do mesmo mês do ano anterior. |

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

Os gráficos usam azul para SIA, laranja para SIH, verde para resultados de apoio e vermelho para alertas de qualidade. Cada tabela e gráfico deve conter título, unidade de medida e período analisado.

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

### 10.2 Entregas estruturadas, pendentes de execução

| Entrega | Situação atual | Próxima ação |
|---|---|---|
| Notebook de análise final | `Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb` está organizado, mas não possui saídas executadas. | Executar todas as células em ordem no ambiente do projeto e salvar as saídas reprodutíveis. |
| Imputação sazonal ajustada | Implementada apenas como sensibilidade no notebook 09, com fator janeiro–outubro. | Conferir o valor imputado, comparar totais observados e imputados e manter os resultados principais sem imputação. |
| Comparação regional | Código ANOVA/Kruskal–Wallis inserido no notebook 09. | Executar pressupostos e reportar somente o teste indicado pelos dados, como resultado exploratório. |
| Seleção de modelo SIA | Código de validação de origem móvel e critérios MAPE/MAE/RMSE inserido no notebook 09. | Executar, registrar métricas e apresentar 2026 apenas como cenário exploratório. |

### 10.3 Pendências metodológicas e de dados

1. Restaurar um ambiente funcional para executar o notebook 09 e salvar as saídas reprodutíveis.
2. Manter novembro/dezembro de 2025 fora da inferência SIH até confirmar a maturidade das competências.
3. Manter N18 fora dos totais: a compatibilidade operacional com TabNet e a divergência histórica não foram resolvidas.
4. Não usar APAC, SIA ou SIH para inferir efetividade sem população elegível, comparador, tempo zero, seguimento e desfecho individual validados.
5. Reavaliar previsão quando houver série temporal mais longa; 24 meses não sustentam projeção operacional.
