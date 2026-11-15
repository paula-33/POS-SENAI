# Artefatos da análise estatística final — 2024–2025

Fonte: notebook `09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb`, executado em kernel Python da `.venv`. Consulte `registro_execucao.json` para data/hora real, versões, cobertura e SHA-256 do painel. A data editorial da entrega é 15/11/2026.

## Conteúdo

- 17 CSVs UTF-8 com separador `;` e ponto decimal: resumo numérico, cobertura SIH, comparação UF janeiro–outubro, produção SIA por população anual (UF e região), proporções de aumento com IC, cinco probabilidades básicas (`probabilidades_basicas.csv`), família de três testes, métricas de previsão e cenário ilustrativo de 2026.
- Seis PNGs extraídos diretamente das saídas do notebook executado; nomes numerados de 01 a 06. Os títulos, eixos e alertas foram inspecionados visualmente.
- `notebook_09_executado.html`: exportação da execução para leitura; o notebook `.ipynb` é a fonte executável.
- `registro_execucao.json`: proveniência da execução e ambiente. A coluna `index` do resumo numérico identifica o indicador; as estatísticas SIH usam somente células observadas.

As taxas SIA são anuais (janeiro–dezembro); a comparação de mudanças utiliza janeiro–outubro em ambos os anos. O total anual SIH observado não comprova cobertura completa. O cenário de 2026 parte do corte de dezembro de 2025 e não representa previsão atualizada ou operacional.

## Reexecutar no Jupyter

A partir da raiz do curso, com as dependências instaladas:

```sh
.venv/bin/python -m jupyter lab
```

Abra o notebook 09, selecione o kernel da `.venv`, reinicie o kernel, execute todas as células em ordem e salve. A última célula exporta os 17 CSVs e `registro_execucao.json` neste diretório; não altera fontes ou painel original. Execute com uma cópia do painel cujo SHA-256 corresponda ao registro quando o objetivo for reproduzir esta versão.

Para executar sem interface, pode-se registrar um kernel temporário e usar `nbconvert`:

```sh
.venv/bin/python -m ipykernel install --prefix /private/tmp/drc-jupyter --name drc-final --display-name 'Python DRC final'
JUPYTER_PATH=/private/tmp/drc-jupyter/share/jupyter .venv/bin/python -m jupyter nbconvert --execute --to notebook --inplace --ExecutePreprocessor.kernel_name=drc-final --ExecutePreprocessor.timeout=180 Trabalho-final/Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb
```

A execução precisa de comunicação local entre processo e kernel Jupyter. Não requer acesso a novas fontes. Para exportar HTML após salvar o notebook:

```sh
.venv/bin/python -m jupyter nbconvert --to html --output notebook_09_executado --output-dir Trabalho-final/Dados/03_bases_analiticas/analise_estatistica_final_2024_2025 Trabalho-final/Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb
```

Os PNGs desta entrega foram extraídos do campo `image/png` das saídas, na ordem das seis figuras. Se o código dos gráficos mudar, regenere os PNGs antes de atualizar o relatório. Não combine figuras antigas com tabelas de uma nova execução.

## Aprofundamento exploratório da seção 12.3

Sete CSVs `exploracao_*.csv`: comparação mensal homóloga (12 meses SIA e dez SIH), resumo temporal por indicador/ano, participações e contribuições por UF, agregação regional, concentração das cinco maiores UFs, nove categorias conjuntas e direções das 27 UFs. A [síntese](sintese_padroes_exploratorios.md) conecta perguntas, resultados, métodos, figuras existentes e limites.

Participações e contribuições usam janeiro–outubro. Contribuição em pontos percentuais divide a diferença pelo total nacional de 2024, preservando reduções. Os extremos usam cercas de 1,5 IQR e não são removidos. As colunas de taxa anual na tabela territorial são sempre SIA, inclusive nas linhas SIH, apenas para contextualização da mesma UF. CV é desvio-padrão mensal amostral/média, sem remoção de tendência; variações mês a mês são calculadas dentro de cada ano.
