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
