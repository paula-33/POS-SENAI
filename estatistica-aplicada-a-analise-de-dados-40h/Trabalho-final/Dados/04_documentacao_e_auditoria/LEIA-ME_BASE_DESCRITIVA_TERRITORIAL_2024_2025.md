# Base descritiva territorial — SIA, SIH TabNet e IBGE (2024–2025)

## Objetivo e unidade

Produto para descrição temporal e territorial da produção aprovada de hemodiálise e de internações por insuficiência renal. O painel tem 648 linhas (27 UFs × 24 meses); cada linha é uma UF-mês, não uma pessoa. Foi produzido pelo notebook [`analise_descritiva_final_drc_sus.ipynb`](../../Notebook/analise_descritiva_final_drc_sus.ipynb), a partir de fontes locais já existentes. Nenhum dado bruto ou CSV de origem foi sobrescrito ou baixado novamente.

## Arquivos gerados

Diretório: `../03_bases_analiticas/descritiva_territorial_2024_2025/`.

- `painel_descritivo_uf_mes_2024_2025.csv`: painel integrado UF-mês; SIA, SIH TabNet, status de ausência e população anual de referência.
- `base_descritiva_sia_hemodialise_uf_mes.csv`: quantidade aprovada SIA para os cinco códigos SIGTAP mapeados.
- `base_descritiva_sih_n17_n19_uf_mes.csv`: internações TabNet N17–N19; campo `status` diferencia célula observada de ausente/suprimida.
- `dimensao_populacao_ibge_uf_ano.csv`: estimativa IBGE por UF-ano, referência em 1º de julho.
- `resumo_descritivo_uf_ano.csv`: totais SIA e soma SIH observada por UF-ano, com cobertura mensal explicitada.
- `serie_mensal_brasil.csv` e `serie_mensal_regiao.csv`: totais observados e cobertura de UFs por competência.
- `comparacao_periodos_equivalentes_uf.csv` e `comparacao_periodos_equivalentes_brasil.csv`: tabela descritiva anterior de janeiro–novembro.
- `comparacao_periodos_jan_outubro_uf.csv`: janela principal dos testes de hipóteses (janeiro–outubro), após sinal de possível incompletude em novembro/dezembro SIH.
- `frequencias_direcao_variacao_uf.csv`, `associacoes_ecologicas_uf_ano.csv`, `testes_hipoteses_exploratorios.csv` e `testes_mensais_direcao.csv`: frequências por UF, taxas ecológicas brutas, correlações e testes exploratórios com ajuste de Holm.
- `graficos/`: três gráficos SVG de série mensal Brasil e por região.

## Validações e resultados reproduzidos

- 648 chaves UF-mês únicas no painel e em cada tabela mensal; 54 chaves UF-ano de população únicas.
- Soma SIH TabNet observada: 309.574; 647 células preenchidas e uma ausente/suprimida: Roraima, dezembro de 2025. Ausência não foi imputada como zero.
- Totais janeiro–outubro (janela principal): SIA 15.187.201 (2024) e 15.772.215 (2025), +3,85%; SIH N17–N19 130.752 e 136.036, +4,04%. A comparação usa os mesmos 10 meses e 27 UFs. Os números janeiro–novembro permanecem como saída descritiva anterior, mas novembro SIH teve queda de 19,22% em 27 UFs; não usar essa janela como principal até verificar maturidade.
- O SIH anual 2025 não tem cobertura completa de UFs em dezembro; totais anuais SIH estão rotulados como observados.
- Dezembro/2025 SIH N17–N19 soma 6.502 nas 26 UFs observadas, contra 12.647 nas mesmas UFs em dezembro/2024 (−48,59%); todas as 26 células observadas são menores. Novembro também caiu em 25 das 27 UFs. Esses padrões sinalizam possível incompletude/defasagem de atualização. Novembro e dezembro foram excluídos dos testes mensais inferenciais de SIH e requerem verificação de maturidade das competências.

## Interpretação e limites

SIA mede quantidade aprovada de procedimentos, não pessoas únicas, cobertura ou sessões recebidas por paciente. SIH N17–N19 mede internações em categoria diagnóstica ampla; não identifica tratamento dialítico ambulatorial nem uma coorte de pacientes. As séries são agregadas e não podem ser vinculadas indivíduo a indivíduo. A população IBGE é anual, com referência em julho; não foi usada como denominador mensal nem foram calculadas taxas neste produto. Comparação percentual é descritiva e não causal.

**N18 foi excluído do painel e de todas as totalizações** por divergência não resolvida com TabNet e inconsistências entre rotinas históricas. Os arquivos N18, inclusive a reextração de 213.789 linhas, continuam restritos à auditoria descrita na [nota SIH](LEIA-ME_SIH_N18_2024_2025.md). Este dataset não responde à efetividade do tratamento.

## Síntese interpretativa

A comparação de períodos equivalentes e os limites de interpretação estão documentados em [`resultados_descritivos_territoriais_2024_2025.md`](../../resultados_descritivos_territoriais_2024_2025.md). A síntese confirma que a camada descritiva/associativa inicial foi concluída; testes e correlações são exploratórios, não alteram o status preliminar de N18 e não respondem a perguntas sobre efeito terapêutico.

## Pendências para avançar além da descrição

1. Decisão clínica sobre população, comparador, tempo zero, desfecho e horizonte.
2. Validação da semântica das datas, continuidade, estabilidade dos identificadores e completude dos desfechos APAC.
3. Fonte que identifique elegíveis comparáveis e permita seguimento individual; cuidado conservador não está representado nas fontes locais identificadas.
4. Manter a reconciliação SIH N18/TabNet como não resolvida; procurar, se disponíveis, artefatos antigos para explicar a diferença de 12 linhas.
5. Se não houver dados para comparador e seguimento, formalizar o escopo final como descritivo/associativo, sem alegação de efetividade.
