# Resultados descritivos territoriais — SIA, SIH TabNet e IBGE (2024–2025)

## Escopo e fontes

Esta síntese descreve a produção aprovada de procedimentos de hemodiálise no SIA/SUS, as internações registradas no TabNet SIH/SUS para N17–N19 e as estimativas anuais de população do IBGE. A unidade integrada é UF-mês (27 UFs × 24 meses; 648 combinações). Os dados foram tratados e validados no notebook [`analise_descritiva_final_drc_sus.ipynb`](Notebook/analise_descritiva_final_drc_sus.ipynb); esta síntese interpreta os arquivos gerados, sem reler nem alterar dados brutos.

Os artefatos e critérios de transformação estão descritos na [nota da base descritiva](Dados/04_documentacao_e_auditoria/LEIA-ME_BASE_DESCRITIVA_TERRITORIAL_2024_2025.md). As tabelas utilizadas estão em [`Dados/03_bases_analiticas/descritiva_territorial_2024_2025/`](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/).

## Perguntas que estas bases permitem explorar

| Pergunta | Fonte e unidade disponível | Limite da resposta |
|---|---|---|
| Em quais UFs a quantidade aprovada SIA aumentou ou diminuiu entre períodos equivalentes? | SIA, UF-mês; comparação pareada das 27 UFs | Mede produção aprovada, não pessoas atendidas nem acesso individual. |
| Como variaram as internações N17–N19 por UF e mês? | TabNet SIH, UF-mês, com status de cobertura | A categoria é ampla, e competência incompleta pode distorcer comparação. |
| A produção SIA e as internações SIH covariam entre UFs? | Correlações ecológicas com denominador populacional anual | Não liga os sistemas por pessoa e não estima efeito do tratamento. |
| A direção das mudanças SIA e SIH entre 2024 e 2025 acompanha-se entre UFs? | Variações percentuais pareadas e Spearman | Pode haver tendências comuns, dependência espacial e confundidores não observados. |
| A queda observada do SIH no fim de 2025 é uma mudança epidemiológica? | Os arquivos permitem detectar o padrão, não explicar sua causa | Dezembro/2025 é sinalizado para verificar maturidade/atualização antes de inferir. |

## Resultados

A janela principal foi janeiro–outubro em ambos os anos, cobrindo as mesmas 27 UFs. A quantidade aprovada de procedimentos SIA passou de **15.187.201** em 2024 para **15.772.215** em 2025, diferença de **585.014 (+3,85%)**. As internações TabNet N17–N19 passaram de **130.752** para **136.036**, diferença de **5.284 (+4,04%)**. Janeiro–novembro também foi tabulado anteriormente (+3,45% SIA; +1,93% SIH), mas deixou de ser a janela principal após os sinais de queda ampla do SIH em novembro e dezembro de 2025, que podem indicar incompletude ou diferença de atualização.

A direção não foi uniforme entre UFs. Na comparação janeiro–outubro, a produção SIA aumentou em 25 UFs e diminuiu em 2; as variações foram de −2,52% no Distrito Federal a +22,49% no Tocantins. As internações N17–N19 aumentaram em 17 UFs e diminuíram em 10; as variações foram de −29,60% em Roraima a +36,39% no Amapá. Essas diferenças estaduais são descritivas; não foram ajustadas por estrutura etária, gravidade, acesso, mudanças de registro ou outros fatores.

O painel contém **309.574 registros TabNet SIH N17–N19** nas 647 células observadas. A célula de Roraima em dezembro de 2025 está ausente/suprimida; não foi preenchida como zero. Além disso, os totais SIH caem amplamente em novembro (−19,22%) e dezembro (−48,59%) de 2025 frente aos mesmos meses de 2024. A causa não foi identificada; esses meses foram excluídos das hipóteses mensais SIH e a janela principal foi limitada a janeiro–outubro. A soma observada de 2025 e as séries regionais do SIH não devem ser interpretadas como cobertura completa de todas as UFs.

A população IBGE foi organizada por UF-ano, com referência em 1º de julho. Ela não foi convertida em denominador mensal e não foram calculadas taxas neste produto.

## Exploração associativa e testes exploratórios

Foram exploradas cinco hipóteses principais no nível agregado das 27 UFs, com correção de Holm para múltiplos testes. Para a mudança entre 2024 e 2025, o teste binomial exato de sinais avalia se as UFs se distribuem igualmente entre aumento e redução; para associações monotônicas, foi usada correlação de Spearman com p-valor por 9.999 permutações Monte Carlo e semente fixa.

| Pergunta | Resultado | p bruto | p ajustado (Holm) |
|---|---:|---:|---:|
| A produção SIA aumentou em mais UFs do que diminuiu (jan-out)? | Aumentou em 25, diminuiu em 2; mediana da variação: +3,30% | 0,00000565 | 0,0000282 |
| As internações N17–N19 aumentaram em mais UFs do que diminuíram (jan-out)? | Aumentaram em 17, diminuíram em 10; mediana: +2,38% | 0,2478 | 0,6336 |
| Associação entre SIA por 100 mil habitantes e SIH por 100 mil em 2024 | Spearman ρ = −0,090 | 0,6553 | 0,6553 |
| Mesma associação em 2025 | Spearman ρ = −0,288 | 0,1451 | 0,5804 |
| Associação entre as mudanças percentuais SIA e SIH por UF | Spearman ρ = −0,247 | 0,2112 | 0,6336 |

A frequência de aumento da produção SIA é incompatível com uma divisão 50/50 das direções sob o teste de sinais. Para SIH, a maioria direcional no período janeiro–outubro não foi estatisticamente distinguível de equilíbrio. As correlações estimadas foram negativas e de magnitude fraca a moderada nesta amostra, mas nenhuma passou o limiar de significância após correção de Holm. Isso **não prova ausência de associação**: são apenas 27 UFs, pode haver dependência espacial e há confundidores não medidos. As estimativas por 100 mil são indicadores ecológicos brutos e não representam pacientes ou risco individual.

Tabelas reprodutíveis: [`comparacao_periodos_jan_outubro_uf.csv`](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/comparacao_periodos_jan_outubro_uf.csv), [`testes_hipoteses_exploratorios.csv`](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/testes_hipoteses_exploratorios.csv), [`frequencias_direcao_variacao_uf.csv`](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/frequencias_direcao_variacao_uf.csv) e [`associacoes_ecologicas_uf_ano.csv`](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/associacoes_ecologicas_uf_ano.csv). O tratamento e os testes estão implementados no notebook de análise; nenhuma dependência adicional foi instalada.

Também foram comparados, para cada mês, os valores de 2025 com o mesmo mês de 2024 em cada UF. Após correção de Holm dentro de cada série mensal, SIA mostrou aumento direcional em 9 meses (janeiro, março–julho, setembro, outubro e dezembro). Nenhum mês de SIH entre janeiro e outubro foi significativo após o ajuste. Novembro e dezembro/2025 foram excluídos dos testes mensais de SIH por possível incompletude: novembro soma 10.545 em 27 UFs (−19,22%; 25 UFs caíram) e dezembro soma 6.502 em 26 UFs (−48,59%; RR ausente), comparados aos mesmos meses de 2024. A queda no fim do período precisa ser esclarecida antes de interpretação substantiva. Resultados mensais completos em [`testes_mensais_direcao.csv`](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/testes_mensais_direcao.csv).

## Interpretação e limites

A produção SIA representa quantidade aprovada dos procedimentos selecionados, não pessoas únicas, cobertura de tratamento nem sessões confirmadas por paciente. SIH N17–N19 é uma categoria diagnóstica hospitalar agregada; não identifica pessoas em hemodiálise e não pode ser vinculada individualmente ao SIA ou à APAC. A comparação de variações entre essas séries não estima efeito do tratamento nem relação causal.

**N18 permanece preliminar e foi excluído dos totais e do painel final.** A reextração N18 está restrita à auditoria: a categoria N18 e a categoria TabNet N17–N19 têm abrangências diferentes, há pendências de compatibilidade do processamento e a diferença histórica de 12 linhas entre rotinas não foi localizada. Ver a [nota de auditoria SIH N18](Dados/04_documentacao_e_auditoria/LEIA-ME_SIH_N18_2024_2025.md).

Com os dados disponíveis, a etapa descritiva/associativa territorial está em andamento. O estudo não busca avaliar eficácia ou efetividade; os dados agregados não vinculam produção, internações e resultados clínicos por pessoa e não permitem atribuir mudanças ao tratamento.

## Figuras

- [Série mensal Brasil (SVG)](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/graficos/serie_mensal_brasil.svg)
- [Série mensal SIA por região (SVG)](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/graficos/serie_mensal_sia_por_regiao.svg)
- [Série mensal SIH por região (SVG)](Dados/03_bases_analiticas/descritiva_territorial_2024_2025/graficos/serie_mensal_sih_por_regiao.svg)

## Próximas explorações

1. Descrever sazonalidade e amplitude mensal SIA/SIH sem interpretar flutuações de 24 meses como tendência de longo prazo.
2. Explorar correlações mensais por UF como descrição, mostrando a distribuição das correlações e considerando dependência temporal; não selecionar estados por p-valores isolados.
3. Avaliar sensibilidade das associações ecológicas a indicadores/denominadores alternativos que tenham cobertura temporal comparável e validação documental.
4. Investigar os extremos estaduais observados com dados complementares e registro de hipóteses, sem atribuir causas a partir das séries agregadas.
5. Manter a interpretação no nível ecológico; não atribuir resultados ao tratamento com estas bases.
6. Continuar documentando a anomalia APAC e a diferença histórica de 12 linhas SIH; N18 permanece excluído dos totais finais.
