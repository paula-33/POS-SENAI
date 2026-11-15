---
name: analise-de-dados
description: Analyze datasets to answer concrete questions, assess data quality, identify patterns, and communicate evidence-based findings. Use for exploratory, descriptive, diagnostic, or basic statistical analysis of tabular data; not for building production data pipelines.
metadata:
  short-description: Analise dados e comunique resultados
---

# Análise de dados

Ajude a transformar dados disponíveis em respostas úteis e verificáveis para a pergunta do usuário. Preserve o contexto e as definições fornecidas; não presuma que correlação demonstra causalidade.

## Abordagem

1. **Defina a pergunta e o resultado esperado.** Identifique população, período, unidade de análise, métricas e comparações relevantes. Se algo essencial estiver ausente, faça uma pergunta curta; caso contrário, explicite uma suposição razoável e prossiga.
2. **Entenda os dados antes de calcular.** Inspecione formato, dimensões, nomes e tipos de colunas, granularidade, período coberto, chaves e categorias. Use os arquivos e ferramentas disponíveis, sem alterar a fonte original.
3. **Avalie qualidade e adequação.** Procure valores ausentes, duplicatas, categorias inconsistentes, tipos incorretos, unidades incompatíveis, valores extremos e possíveis vieses de cobertura. Verifique se o conjunto realmente permite responder à pergunta. Diferencie ausência de registro de valor zero.
4. **Escolha análises proporcionais à pergunta.** Comece por contagens e estatísticas descritivas; agregue, segmente ou compare grupos quando isso responder à questão. Use métodos estatísticos mais avançados apenas quando as premissas e a quantidade de dados os sustentarem. Documente filtros, exclusões e transformações que afetem o resultado.
5. **Confira os resultados.** Valide totais, denominadores, períodos, unidades e consistência entre cálculos. Investigue resultados inesperados antes de apresentá-los. Não invente valores quando os dados ou ferramentas não permitem calculá-los.
6. **Comunique a resposta primeiro.** Apresente as conclusões principais em linguagem simples, com números e unidades, período e base de comparação. Em seguida, resuma o método, limitações relevantes e próximos passos úteis. Use tabela ou gráfico quando facilitar a leitura; rotule eixos, unidades e período, e evite escalas ou agregações que distorçam comparações.

## Interpretação

- Descreva o que os dados mostram e separe isso de hipóteses sobre causas ou mecanismos.
- Ao comparar taxas, informe numerador e denominador quando forem importantes; não compare contagens de grupos de tamanhos muito diferentes sem contextualização.
- Diferencie mudança absoluta de mudança percentual e indique a base usada.
- Trate amostras pequenas, dados observacionais, cobertura incompleta e períodos sazonais como limitações que podem mudar a interpretação.
- Só recomende decisões quando a análise sustentar a recomendação; deixe claro o que ainda precisa ser confirmado.

## Entregáveis e alterações

Responda no formato pedido pelo usuário. Se ele pedir arquivo, produza um artefato organizado e fácil de revisar, preservando os dados de origem. Não substitua, apague ou envie dados a serviços externos sem instrução explícita. Não execute código ou altere arquivos além do necessário para a análise solicitada.
