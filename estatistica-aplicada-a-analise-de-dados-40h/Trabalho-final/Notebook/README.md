# Ordem de execução dos notebooks

Os prefixos numéricos organizam a trilha principal até a base UF-mês tratada. As exportações de TabNet/IBGE e os arquivos brutos são obtidos fora destes notebooks e preservados em `Dados/01_fontes_originais/`; por isso, não há notebook de exportação nesta sequência.

## Trilha principal: fontes → base final

1. **`01_VALIDACAO_SIA_hemodialise.ipynb` — Validação:** confere a extração SIA/SUS de hemodiálise, cobertura temporal, UFs, valores e totais.
2. **`02_TRATAMENTO_SIH_TabNet_N17_N19.ipynb` — Tratamento:** seleciona e valida os dados TabNet SIH N17–N19 de 2024–2025 e grava a cópia analítica usada no estudo.
3. **`03_VALIDACAO_IBGE_populacao_UF.ipynb` — Validação e dimensão:** verifica população por UF e prepara os denominadores anuais usados em comparações territoriais.
4. **`04_TRATAMENTO_E_ANALISE_base_final_DRC.ipynb` — Integração e análise descritiva:** combina SIA, SIH TabNet e população, valida chaves e cobertura e grava a base final em `Dados/03_bases_analiticas/descritiva_territorial_2024_2025/painel_descritivo_uf_mes_2024_2025.csv` (648 linhas UF-mês). Também produz sumários e gráficos. Esta é a etapa que gera o dataframe final tratado.
5. **`09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb` — Análise final:** usa o painel tratado para documentar o problema, aplicar imputação sazonal ajustada à única ausência SIH, descrever as variáveis, estimar probabilidades, realizar inferência exploratória e comparar modelos de previsão para SIA.

Execute a trilha na ordem acima, a partir da raiz do curso ou da pasta do trabalho final, e confira os caminhos e notas em `Dados/04_documentacao_e_auditoria/` antes de rodar. Os arquivos de origem não são sobrescritos.

## Cadernos complementares

Estes cadernos tratam análises ou auditorias independentes; não são pré-requisitos para gerar o painel final:

- **`05_AUDITORIA_SIH_DBC_N18.ipynb` — Auditoria:** reconciliação de N18 em microdados DBC contra fontes preliminares e TabNet. N18 fica fora do painel final.
- **`06_ANALISE_CNES_dialise_202412.ipynb` — Análise cadastral:** descreve estabelecimentos/serviços CNES em uma competência.
- **`07_ANALISE_IBGE_populacao_municipio.ipynb` — Análise territorial auxiliar:** valida dados municipais e reconcilia município, UF e Brasil.
- **`08_AUDITORIA_APAC_e_proximas_etapas_SIH.ipynb` — Auditoria e planejamento:** documenta achados APAC e decisões para etapas futuras.

Os prefixos indicam a ordem de leitura recomendada, não uma dependência automática entre notebooks. Consulte cada caderno e seu `LEIA-ME` para requisitos específicos.


## Entrega estatística final

O notebook 09 está executado e documentado para o painel local de 2024–2025. O [relatório consolidado](../relatorio_final_analise_estatistica_drc_2024_2025.md) apresenta resultados e figuras. Os [artefatos finais](../Dados/03_bases_analiticas/analise_estatistica_final_2024_2025/LEIA-ME.md) incluem ambiente, SHA-256, tabelas, PNGs e HTML. Novos insumos externos são pesquisa futura e não bloqueiam essa entrega.
