# Execução final — plano estatístico SIA/SIH/IBGE

Plano: `Trabalho-final/plano_analise_estatistica_e_previsao_drc.md`, seções 12 e 13. Data de referência da entrega: 15/11/2026, America/Sao_Paulo.

## Escopo e decisões de execução

- Ruling: executar no diretório solicitado, na branch existente `feature/avaliacao-inicial-dados`, preservando as alterações locais — o usuário indicou explicitamente o arquivo e o trabalho em continuidade; não criar worktree nem mover dados — custo se incorreto: alterações ficam na mesma árvore para revisão por diff.
- Ruling: usar este registro como ledger durável, com três tarefas editoriais, em vez dos scripts SDD — o plano estatístico não usa o formato de tarefas desses scripts e a raiz Git fica acima da área gravável — custo se incorreto: acompanhamento manual, sem automatismo dos scripts.
- Ruling: validar alterações de apresentação por renderização e execução integral, mantendo os quatro testes existentes — não se introduzem novos estimadores ou regras de transformação; não criar testes que apenas repitam textos de rótulos — custo se incorreto: inspeção visual pode deixar passar um defeito de apresentação.

## Tarefas e dependências

1. Revisão visual e ajuste dos seis gráficos; métodos e dados preservados.
2. Execução final em kernel Jupyter, gravação das saídas e exportação das figuras/tabelas usadas pelo relatório; depende dos rótulos finais da tarefa 1.
3. Relatório acadêmico consolidado e atualização do checklist; consome os artefatos executados da tarefa 2.

Pre-flight: usar a mesma base e a mesma família de três testes do notebook 09 em todas as entregas. A síntese territorial anterior conserva sua família de cinco testes e não será apresentada como a família final do notebook 09.

## Verificação inicial

- Árvore Git sem modificações no início desta rodada.
- `python -m unittest discover -s Trabalho-final/tests -v`, com o Python de `.venv`: 4 testes passaram.
- Seis PNGs existentes extraídos do notebook e inspecionados. Ajustes necessários: período nos títulos, aviso explícito de cobertura SIH, identificação de p bruto/Holm e cenário de 2026 condicionado ao corte de 2025.
- Fontes originais e painel analítico não serão alterados.

## Execução e evidências finais

### Task 1: complete — revisão gráfica

Os seis PNGs finais foram abertos e inspecionados individualmente. Títulos/eixos/legendas aparecem sem cortes ou sobreposição impeditiva. As alterações foram editoriais: período nos títulos, valores SIA sem notação exponencial, aviso SIH e anotação RR, p bruto/Holm na dispersão, retirada da reta OLS para não confundir com Spearman, cenário de 2026 rotulado pelo corte de dezembro/2025 e pontos regionais sem duplicar os outliers do boxplot. Estimadores e agregações foram preservados.

### Task 2: complete — kernel Jupyter e integridade

A execução por `nbclient` iniciou um kernel `ipykernel` usando o executável da `.venv`, executou e salvou 11 células de código com contadores 1–11, sem saídas de erro. O sandbox inicial bloqueou a abertura de portas locais; a execução autorizada fora dessa restrição foi concluída. A advertência de transporte TCP local do kernel não é um erro de análise.

- Data/hora, Python e versões: `../03_bases_analiticas/analise_estatistica_final_2024_2025/registro_execucao.json`.
- SHA-256 do painel, antes/depois: `5d8f671d31c7b83aa4e1e20c1221731e941957ed32e6f756c10a5e1a5e2d91a4`.
- Artefatos: nove CSVs, seis PNGs idênticos aos bytes das saídas Jupyter, HTML do notebook e JSON de execução. Fontes e painel preservados.
- Verificação adicional: 648 chaves únicas, 27 UFs em cada competência, 540 linhas na janela janeiro–outubro, diferenças nacionais +585.014 SIA e +5.284 SIH, frequências 25 e 17, reconciliação das taxas regionais e MAPE de 3,014402% do candidato selecionado.

### Task 3: complete — relatório e consistência editorial

Relatório final em `../../relatorio_final_analise_estatistica_drc_2024_2025.md`, contendo resumo, objetivo, fontes, métodos, resultados, seis figuras, discussão, conclusão, referências locais e reprodução. Todos os links locais do relatório, plano, README dos notebooks e README de artefatos foram conferidos. O checklist do plano e o roteiro de próximas etapas foram atualizados.

As 15 tabelas HTML foram conferidas quanto à presença de estrutura/linhas e os resultados centrais reconciliados com CSVs e fonte; a revisão visual direta desta rodada cobre os seis gráficos. A tentativa de abrir o HTML em navegador não foi possível porque o host do navegador estava indisponível. Isso não bloqueou a leitura dos PNGs nem a validação do conteúdo das tabelas; não se declara uma inspeção visual completa da interface Jupyter no navegador.

O verificador auxiliar tentou inicialmente `pandas.read_html`, mas o pacote opcional `lxml` não estava instalado. A checagem estrutural foi feita com `html.parser` da biblioteca padrão, sem instalar dependências; ela passou junto com as demais verificações de integridade.

## Testes e revisão final

` .venv/bin/python -m unittest discover -s Trabalho-final/tests -v `: 4/4 testes passaram após as alterações. `git diff --check`: sem erros de whitespace. Verificação dos artefatos: passou. Revisão independente final: aprovada, sem achados críticos, importantes ou menores; nenhuma questão deixada sem julgamento. O revisor leu o diff e os documentos, inspecionou os seis PNGs e recalculou independentemente as métricas de previsão. Não houve nova execução do kernel pelo revisor.


### Fechamento da revisão

O arredondamento de p-Holm SIA no relatório foi conferido contra o CSV e fixado em 0,00001694. Não há achados pendentes ou menores adiados. As verificações finais repetiram os quatro testes existentes, a integridade dos artefatos e `git diff --check`.

As alterações permanecem na branch/diretório solicitados, sem commit, merge ou publicação. O registro durável foi preservado junto à auditoria para que as evidências não dependam da conversa ou de arquivos temporários.

## Atualização didática — cinco probabilidades básicas

A pedido do usuário, a seção 7 do notebook foi ampliada para apresentar experimento, espaço amostral, eventos A/B e cinco estudos separados: aumento SIA, aumento SIH, interseção, união inclusiva e dupla redução. Cada estudo contém pergunta, fórmula, célula de código com resultado numérico e interpretação em Markdown. Há quadro-resumo e subseção complementar com os intervalos binomiais anteriores. Foi adicionado um sumário com links para as 11 seções, visando leitura e avaliação acadêmica.

O teste comportamental novo utiliza cinco UFs fictícias com os casos ++, +−, −+, −− e empate duplo. Ele falhou antes da implementação por ausência do estudo e passou depois: contagens esperadas 2, 2, 1, 3 e 1. Assim, verifica interseção/união e impede interpretar empate como redução. Os quatro testes anteriores também passaram (total atual: 5/5).

A nova execução integral em kernel Jupyter concluiu **18 células de código**, contadores 1–18, sem erros. As saídas mostram 25/27 = 92,59%; 17/27 = 62,96%; 15/27 = 55,56%; 27/27 = 100%; 0/27 = 0%. Os novos cálculos usam a tabela UF da janela janeiro–outubro, sem alterar o painel, os testes inferenciais ou os modelos. A data/hora mais recente está em `registro_execucao.json`.

O quadro-resumo foi exportado em `probabilidades_basicas.csv`, elevando a entrega para **dez CSVs**. O HTML do notebook e o manifesto foram atualizados; o plano e o relatório receberam as cinco probabilidades. A integridade final conferiu seis PNGs idênticos às saídas, 16 tabelas HTML, dez CSVs, contagens, taxas, métricas, links e o mesmo SHA-256 do painel. Esta atualização não altera o conteúdo dos seis gráficos revisados anteriormente.

A verificação desta ampliação foi execução Jupyter, teste comportamental e conferência do conteúdo das saídas; não foi feita nova inspeção de interface em navegador. `git diff --check` passou. As alterações desta atualização ficam locais, sem novo commit ou push nesta rodada.

## Organização por metodologia aplicada

O notebook foi reorganizado com Markdown para explicitar a sequência metodológica: contextualização, objetivos, preparação da base, controle de qualidade, sensibilidade, estatística descritiva, probabilidades, inferência, modelagem preditiva, discussão e reprodutibilidade. As subseções identificam medidas descritivas, comparação pareada, teste de sinais, Spearman, Holm, pressupostos regionais, ANOVA/Kruskal–Wallis, validação móvel e extrapolação.

As instruções de código foram preservadas integralmente; o diagnóstico de cobertura foi deslocado para antes da sensibilidade, respeitando suas dependências. A nova ordem foi executada no kernel Jupyter: 18 células, contadores sequenciais 1–18, sem erros, com o mesmo SHA-256 do painel. Os cinco testes passaram e os artefatos foram reconciliados. O HTML acompanha a estrutura nova e o manifesto foi atualizado. Não houve nova inspeção de interface em navegador.

## Revisão editorial da abertura e referências

Título, apresentação, introdução e contexto foram reescritos em Markdown para leitura acadêmica. A abertura explica o recorte territorial/temporal e apresenta o sumário; as seções 1 e 2 distinguem contexto, delimitação, problema, contribuição estatística, objetivos e alcance. Foi adicionada a seção 12, ao final do notebook, com link relativo para a bibliografia existente e identificação das fontes SIA/SIH/IBGE. O sumário passou a incluir as referências.

Esta revisão alterou somente células Markdown. Código, contadores de execução e saídas foram comparados antes/depois e permaneceram iguais; não houve nova execução do kernel. O HTML foi atualizado e seu caminho relativo para a bibliografia ajustado à localização da exportação. Cinco testes passaram; âncoras e destino das referências foram conferidos. O manifesto foi atualizado para refletir a versão editorial.

## Ampliação da proposta exploratória

A abertura, o problema e os objetivos do notebook passaram a destacar exploração dos dados e identificação de padrões territoriais e temporais pela aplicação de metodologias estatísticas. O texto conecta tendências e oscilações descritivas, contrastes territoriais, frequências de eventos, testes, associações e validação preditiva às perguntas do estudo. Distingue identificação exploratória de confirmação independente e ressalta o limite da série curta para sazonalidade e persistência temporal.

A revisão foi exclusivamente em Markdown; código e saídas foram comparados antes/depois e preservados. Cinco testes passaram. O HTML e o manifesto foram atualizados, sem nova execução do kernel ou inclusão de novos testes estatísticos.

## Adendo — aprofundamento exploratório da seção 12.3

A seção 6.4 do notebook acrescenta o mapa de perguntas, unidades, métodos e limitações antes dos cálculos. Foram gerados sete CSVs exploratórios, elevando a entrega a 17 CSVs, e uma síntese Markdown incorporada à discussão do notebook e à seção 4.6 do relatório. A conclusão também foi ampliada. Mantiveram-se as fontes, os testes, a janela principal e os seis tipos de figura.

A execução completa em kernel Jupyter contém agora **19 células de código sequenciais sem erros**. O registro JSON contém a data real da execução e as versões utilizadas. A execução usou configuração e kernel temporários em `/private/tmp`; foi necessário permitir a comunicação local entre processo e kernel. HTML e seis PNGs foram regenerados a partir das saídas salvas. Uma visão conjunta das seis figuras foi inspecionada: títulos, eixos, unidades, alerta SIH e limite do cenário permanecem legíveis; a revisão adicional não constitui avaliação clínica dos gráficos.

Validação independente:

```sh
.venv/bin/python Trabalho-final/Dados/04_documentacao_e_auditoria/validar_aprofundamento_notebook_09.py
.venv/bin/python -m unittest discover -s Trabalho-final/tests -v
```

Resultado: sete tabelas reconciliadas com agregações do painel; 5 testes existentes aprovados. Conferidos totais mensais, CV, mínimos/máximos, diferenças e percentuais por UF, participações, concentração das cinco maiores UFs, contribuição ao crescimento, extremos IQR, taxas anuais, agregação regional e direções conjuntas. A base conserva SHA-256 `5d8f671d31c7b83aa4e1e20c1221731e941957ed32e6f756c10a5e1a5e2d91a4`. Não se substituiu ausência por zero nem se utilizou a imputação na exploração principal.

Os valores da síntese foram conferidos nas tabelas exportadas. Os padrões sustentam descrição e hipóteses: 11/12 meses homólogos SIA positivos, 9/10 SIH, concentração SIA próxima de 55%, maior crescimento relativo SIA no Norte e maior acréscimo absoluto no Sudeste, extremos percentuais com contribuições absolutas distintas e 12 UFs com direções divergentes. Não houve novo teste de significância. Perguntas sem suporte suficiente estão registradas na síntese; sazonalidade persistente, causalidade e validade anual do cenário continuam sem demonstração.

O manifesto SHA-256 foi atualizado após a documentação. As alterações locais anteriores foram preservadas; nenhum commit foi criado.
