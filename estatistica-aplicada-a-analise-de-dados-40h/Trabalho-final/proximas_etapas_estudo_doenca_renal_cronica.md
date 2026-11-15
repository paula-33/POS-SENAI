# Próximas etapas do estudo sobre doença renal crônica no SUS

> **Decisão vigente — 15/11/2026:** os insumos externos não estão disponíveis. Concluir o estudo com SIA/SIH/IBGE locais, conforme as seções 12 e 13 do [plano estatístico](plano_analise_estatistica_e_previsao_drc.md). A janela comparativa é janeiro–outubro; APAC e N18 ficam excluídos; previsão SIA é avaliação retrospectiva com cenário ilustrativo. Os encaminhamentos DATASUS e clínicos descritos abaixo são histórico e possibilidades de pesquisa futura, sem bloquear a entrega. Restam revisão visual, consolidação do relatório e execução final documentada.


## Objetivo deste roteiro

Organizar o trabalho restante em ordem de execução, explicitar dependências e indicar frentes que podem avançar em paralelo. **Escopo decidido em 05/11/2026:** manter o estudo descritivo/associativo, explorando padrões, frequências, correlações e testes de hipóteses ecológicos com SIA, SIH N17–N19 e IBGE. Não estimar eficácia/efetividade nem atribuir causalidade ao tratamento.

O roteiro parte do estado registrado no [planejamento do estudo](planejamento_estudo_doenca_renal_cronica_sus.md) e nas notas de auditoria. A pergunta comparativa individual foi retirada do escopo vigente; o rascunho correspondente está suspenso.

As limitações de dados e de método, seus efeitos no painel e os encaminhamentos externos estão consolidados em [Limitações e próximos passos — auditoria DRC](Dados/04_documentacao_e_auditoria/PENDENCIAS_EXTERNAS_E_METODOLOGICAS_2026-11-15.md). A minuta ao DATASUS e o checklist clínico são anexos operacionais desse registro.

## Andamento da execução (atualizado em 05/11/2026)

- **Base descritiva territorial — construída, executada e interpretada:** notebook `Notebook/04_TRATAMENTO_E_ANALISE_base_final_DRC.ipynb`; síntese de resultados em `resultados_descritivos_territoriais_2024_2025.md`; arquivos novos em `Dados/03_bases_analiticas/descritiva_territorial_2024_2025/`. O painel contém 648 UF-mês; SIA, SIH e população também estão em tabelas auxiliares separadas. Há sumários por UF-ano, séries mensais e gráficos SVG. Detalhes em `Dados/04_documentacao_e_auditoria/LEIA-ME_BASE_DESCRITIVA_TERRITORIAL_2024_2025.md`.
- **Achados descritivos conferidos:** TabNet SIH soma 309.574 nas células observadas; RR/dezembro/2025 permanece ausente. Na janela principal janeiro–outubro (27 UFs), SIA variou +3,85% e SIH N17–N19 +4,04%. A janela janeiro–novembro anterior (+3,45% e +1,93%) é mantida apenas como referência descritiva, pois novembro SIH caiu em 25 UFs e dezembro caiu nas 26 UFs observadas. Não são resultados por paciente nem estimativas de efeito. IBGE é anual (1º de julho), sem taxa mensal.
- **Exploração estatística inicial:** na janela jan-out, teste de sinais encontrou aumento SIA em 25/27 UFs (p-Holm=0,0000282); SIH aumentou em 17/27, sem evidência de desequilíbrio direcional após Holm (p=0,6336). Correlações ecológicas não foram significativas após ajuste. Nos testes por mês, SIA teve aumento direcional em 9 meses; nenhum mês SIH jan-out foi significativo após Holm. SIH nov/dez foi excluído dos testes mensais por sinal de possível incompletude (nov −19,22%; dez −48,59%). Resultados e limites estão na síntese e nas tabelas exportadas pelo notebook.
- **SIH N18:** a definição TabNet “Internações” foi confirmada oficialmente como AIHs aprovadas sem prorrogações de longa permanência, incluindo transferências e reinternações. Na reextração DBC, 213.788 N18 `IDENT=1` e um `IDENT=5`; `IDENT=1` fica abaixo do N17–N19 TabNet nas 647 células preenchidas. O histórico de 368.917 é incompatível com a reextração. A diferença de 12 entre rotinas antigas permanece sem localização. N18 segue preliminar e fora da base descritiva; nova execução em `Dados/02_derivados_preliminares/SIH/auditoria_sih_dbc_reconciliacao_20261105_221707/` e detalhes na [nota SIH](Dados/04_documentacao_e_auditoria/LEIA-ME_SIH_N18_2024_2025.md).
- **APAC:** o Informe Técnico SIASUS 2019.07 define `ATD_DTPDR` como início da primeira diálise e `ATD_DTCLI` como início na clínica, ambos `AAAAMMDD`; isso não explica os anos futuros/distantes, que continuam fora de tempo zero/seguimento. Nova leitura dos 648 DBCs concluída, com 3.186.282 registros e inventário SHA-256 em `Dados/02_derivados_preliminares/APAC/auditoria_excecoes_20261105_v2/`. Reproduzidos os 12 registros `AP_TPAPAC=4`/procedimento vazio e datas futuras (146 `ATD_DTPDR`, 1.162 `ATD_DTCLI`). Semântica, continuidade, estabilidade de identificadores e completude do óbito não validadas; nenhuma coorte foi criada.
- **Escopo atual:** descritivo/associativo ecológico. O protocolo comparativo foi suspenso; não se planeja coorte individual nem estimativa de eficácia/efetividade.

### Próximos passos — ordem de execução e trabalho paralelo (estado em 05/11/2026)

**Etapa 1 — Concluída nesta rodada.** Resultados SIA/IBGE e SIH N17–N19 revisados; síntese interpretativa registrada em `resultados_descritivos_territoriais_2024_2025.md` e incorporada à seção de resultados do notebook. As unidades permanecem separadas e N18 preliminar não foi incorporado.

**Etapa 2 — Aguardando insumo externo para SIH/N18.** A exploração mensal já detectou quedas em novembro (−19,22%; 25 de 27 UFs) e dezembro (−48,59%; 26 UFs, RR ausente). A verificação de 15/11/2026 não encontrou no repositório resposta do DATASUS nem nova extração TabNet datada; logo, não há versão nova a comparar. Esses meses seguem fora dos testes mensais SIH, RR/dezembro não é tratado como zero e N18 não entra nos totais.

**Etapa 3 — Viabilidade APAC encerrada negativamente com as fontes atuais.** Datas sem semântica confirmada, continuidade não reconstruível, identificador sem estabilidade demonstrada e desfecho sem completude validada impedem coorte e seguimento individual. A APAC fica restrita à auditoria. Uma especificação oficial futura poderá reabrir essa avaliação.

**Etapa 4 — Decisão clínica não acionada.** O checklist não será levado a nefrologista e epidemiologista enquanto a etapa 3 estiver encerrada negativamente. Se a APAC se tornar tecnicamente viável, definir população, comparador, tempo zero, seguimento, desfecho, confundimento, vínculo e governança antes de formar coorte.

**Etapa 5 — Atualizar resultados e previsão.** Após nova extração SIH, decidir se novembro/dezembro retornam à inferência. Reavaliar a previsão SIA somente com série mais longa e dados atualizados; até então, tratá-la como cenário exploratório. Não afirmar causa nem efeito terapêutico.

**Frentes que podem avançar em paralelo:** exploração mensal e correlações adicionais; auditoria da consistência/maturidade do SIH; esclarecimento APAC e busca da rotina histórica de N18. A análise principal usa SIA e SIH N17–N19 tratados, com N18 e APAC excluídos.

**Registro da rodada:** a auditoria local APAC de continuidade foi adicionada à nota e ao notebook; seis células de código do notebook de execução foram executadas com os artefatos existentes. Foi corrigida a leitura de CSVs com separadores diferentes. DBCs brutos e extrações anteriores foram preservados. O notebook resume verificações locais, mas não substitui o esclarecimento técnico nem a validação clínica.

## Princípios de execução

- Preservar os arquivos brutos e as extrações existentes; gerar novos artefatos de auditoria em diretórios versionados.
- Manter SIH N18 identificado como preliminar de auditoria. Não usar o CSV de 368.917 linhas como total final, nem interpretar linhas ou AIHs como pacientes únicos.
- Não deduplicar `N_AIH` nem recodificar `IDENT` sem regra documentada e evidência.
- Não interpretar produção aprovada do SIA como pacientes tratados ou sessões individuais confirmadas.
- Não concluir eficácia ou efetividade a partir de comparações agregadas.
- Registrar para cada decisão a fonte, unidade, período, geografia, filtros, limitações e artefatos usados.

## Ordem de execução e dependências

### 1. Delimitar a divergência histórica do SIH — definição TabNet conferida; 12 linhas antigas pendentes

**Status (05/11/2026):** definição da medida TabNet verificada e cenário N18 `IDENT=1` reextraído/comparado nas 647 células observadas; a diferença de 12 entre rotinas antigas permanece sem os artefatos que a geraram.  
**Pode avançar em paralelo com:** etapas 2 e 3.

1. A busca local já não encontrou código ou saída da rotina de 368.905; se os artefatos forem recuperados futuramente, reproduzir as rotinas linha a linha.
2. A definição oficial TabNet foi verificada: “Internações” exclui AIHs de prorrogação de longa permanência e inclui transferências/reinternações; competência de atendimento corresponde à data de internação.
3. A nova auditoria encontrou 213.788 linhas N18 `IDENT=1` e uma `IDENT=5`; nas 647 células observadas, `IDENT=1` permanece abaixo de N17–N19 em todas. Isso verifica coerência de subconjunto, não igualdade entre categorias.
4. Manter N18 e os cenários por UF/mês em diretório de auditoria; considerar ainda não demonstrada a maturidade/cobertura do processamento SIH em relação ao corte TabNet. Não deduplicar para forçar igualdade.

**Saída:** concluída para a definição e os cenários observáveis; a diferença exata de 12 linhas continua delimitada como não localizável sem a rotina histórica. N18 segue excluído dos totais finais.

### 2. Validar exceções e datas da APAC

**Depende de:** nada; trabalhar em paralelo à etapa 1.  
**Pode avançar em paralelo com:** etapas 1 e 3.

1. Consultar o layout e os domínios oficiais vigentes para explicar os 12 registros sem tipo APAC/procedimento principal classificado.
2. Investigar os valores de `ATD_DTPDR` e `ATD_DTCLI` posteriores ao fim de 2025: representação/codificação, competências afetadas e semântica dos campos. Não corrigir nem excluir antes de documentar a regra.
3. Documentar as regras de reapresentação, continuidade, transferência e uso de `AP_APACANT`, incluindo a janela temporal necessária para observar início e continuidade do tratamento.
4. Avaliar a estabilidade do identificador pseudonimizado entre competências. Investigar as 12.065 autorizações ligadas a mais de um identificador sem assumir que `AP_AUTORIZ` identifica uma pessoa.
5. Avaliar o que os campos de saída e óbito permitem afirmar sobre desfecho e seguimento; coerência entre flags e motivo de saída não prova completude da mortalidade.

**Saída:** nota APAC atualizada com regras confirmadas, exceções, decisões de tratamento dos registros e conclusão sobre se há identificador e seguimento utilizáveis. Não criar coorte de pacientes antes dessa conclusão.

### 3. Explorar padrões e formular hipóteses descritivas/associativas

**Status:** primeira rodada executada no notebook principal. Foram produzidas frequências direcionais, correlações ecológicas por UF e testes exploratórios com ajuste de Holm.  
**Pode avançar em paralelo com:** etapas 2 e 4.

1. Revisar os testes e correlações registrados no notebook e nos CSVs; relatar estimativas, p-valores brutos e ajustados, unidades e pressupostos.
2. Descrever frequência e magnitude de aumentos/reduções por UF e região; investigar extremos sem atribuir causa com base apenas em agregados.
3. Explorar padrões mensais/sazonais com cautela, dada a série curta de 24 meses; separar cobertura incompleta SIH e ausência/supressão.
4. Explorar associações temporais por UF considerando tendência, autocorrelação e dependência espacial; não usar correlação simples como relação causal.
5. Definir hipóteses antes de novos testes e controlar multiplicidade quando houver várias comparações.

**Saída:** tabelas de frequências, medidas de associação e testes exploratórios reproduzíveis, com interpretação limitada ao nível ecológico.

### 4. Decidir fontes complementares e usos descritivos

**Depende de:** as perguntas descritivas/associativas da etapa 3 orientam prioridades; a coleta exploratória pode começar em paralelo.  
**Pode avançar em paralelo com:** etapas 1 e 2.

1. Avaliar o CSV agregado SUS 360º como fonte contextual ou validação de produção por CNES, sem misturar sua unidade com SIA ou SIH.
2. Buscar variáveis territoriais anuais comparáveis para contextualizar diferenças entre UFs, documentando limitações e cobertura.
3. Usar população IBGE como denominador apenas em indicadores cuja temporalidade e unidade sejam explicitadas; manter taxas mensais fora do produto atual.
4. Manter CNES fora de indicadores de capacidade operacional sem medida validada para esse uso.

**Saída:** matriz fonte–variável–unidade–período–limitação e decisão sobre incluir cada fonte.

### 5. Congelar definições e montar o conjunto analítico

**Depende de:** conclusão das etapas 1 a 4.  
**Pode avançar em paralelo:** preparar documentação e estrutura de diretórios, sem consolidar observações analíticas antes das decisões.

1. Harmonizar códigos territoriais e períodos, definir unidade de análise e regras de agregação.
2. Especificar numeradores, denominadores, dados ausentes, supressões e tratamento de valores extremos.
3. Criar tabelas analíticas derivadas sem alterar os originais; registrar versão, código de geração e proveniência.
4. Validar reconciliações internas, totais, chaves, duplicidades e consistência temporal contra as regras aprovadas.
5. Separar explicitamente bases prontas para análise, preliminares de auditoria e fontes excluídas, documentando a razão.

**Saída:** base analítica agregada versionada e dicionário de dados, mantendo fontes preliminares separadas.

### 6. Consolidar análises descritivas/associativas e redigir conclusões

**Depende de:** etapa 5 concluída e pergunta analítica definida.

1. Descrever distribuição, cobertura, ausências e características das unidades observadas.
2. Calcular indicadores e intervalos de incerteza adequados ao desenho e à unidade de análise.
3. Usar modelos somente após avaliar distribuição, dependência temporal, tamanho amostral e confundimento mensurável.
4. Apresentar análises territoriais como descritivas/ecológicas e evitar inferência individual.
5. Interpretar p-valores junto com tamanhos de associação, cobertura e limitações; não chamar associação agregada de eficácia, efetividade ou efeito causal.

**Saída:** relatório de resultados, limitações e respostas explícitas às perguntas de pesquisa.

## Frentes paralelas imediatas

| Frente | Tarefas | Bloqueia o quê? |
|---|---|---|
| SIH | Procurar rotina/saídas antigas; documentar regra TabNet e comparar UF/mês | Uso de N18 em totais finais |
| APAC | Consultar layout, datas futuras, 12 registros sem classificação, continuidade e identificadores | Coorte longitudinal e desfechos |
| Hipóteses | Registrar perguntas, unidade, medidas, pressupostos e multiplicidade antes de novos testes | Interpretação válida dos testes ecológicos |
| Fontes | Avaliar SUS 360º e indicadores territoriais contextuais | Contextualizar variações sem extrapolar unidade |
| Descritivo | Preparar definições de indicadores SIA/IBGE, sem misturar unidades | Análise descritiva territorial |

## Critérios para considerar a preparação encerrada

- As divergências do SIH foram reproduzidas e explicadas, ou formalmente delimitadas como não resolvidas, com decisão de uso documentada.
- A APAC tem regra justificada para identificador, continuidade, datas e desfecho, ou foi excluída de análises longitudinais.
- As hipóteses ecológicas, unidade, período, medidas e correções de multiplicidade estão documentadas.
- Fontes, filtros, limitações, ausências e transformações estão documentados e os dados derivados podem ser reproduzidos sem sobrescrever os brutos.
- O plano distingue descrição e associação ecológica e não atribui causalidade ao tratamento.

O escopo vigente já é descritivo/associativo. Não há etapa pendente de aprovação de comparador individual; a prioridade é aprofundar padrões e associações ecológicas e comunicar seus limites.
