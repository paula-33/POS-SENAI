# Protocolo provisório para decidir a viabilidade comparativa

> **Status atualizado em 05/11/2026: suspenso e fora do escopo vigente.** O estudo seguirá como descritivo/associativo, conforme decisão do usuário. Este arquivo fica preservado como registro metodológico anterior; não orientar as próximas análises nem construir uma coorte comparativa.

**Status:** rascunho metodológico para discussão com nefrologista e epidemiologista clínico. Não é protocolo aprovado, não define tratamento clínico e não autoriza estimativa de efeito com os dados atuais.

## Pergunta a avaliar

Entre pessoas com doença renal crônica que iniciam terapia renal substitutiva no SUS, há diferença em desfechos clínicos entre hemodiálise e diálise peritoneal?

Essa pergunta é uma alternativa metodologicamente mais próxima das APAC disponíveis do que diálise versus cuidado conservador, porque as fontes locais contêm registros de tratamento dialítico. Ainda assim, não se presume comparabilidade clínica entre modalidades nem viabilidade causal.

## Componentes que precisam de decisão clínica

| Componente | Proposta para discussão | Questão pendente |
|---|---|---|
| População | Pessoas com DRC iniciando terapia dialítica, com elegibilidade definida antes da análise | Quais idades, diagnósticos e condições clínicas devem ser incluídos? Como distinguir início real de uma clínica nova, transferência ou reentrada? |
| Estratégias | Hemodiálise versus diálise peritoneal | Quais códigos/procedimentos representam cada estratégia em cada competência? Como classificar mudança de modalidade? |
| Tempo zero | Início confirmado da modalidade, com janela de elegibilidade e exposição explicitadas | `ATD_DTPDR` é início da primeira diálise; `ATD_DTCLI` é início na clínica. Qual campo e regra representam o início da estratégia comparada? |
| Desfecho | Mortalidade por todas as causas em horizonte fixo, apenas se houver data e cobertura confiáveis; outros desfechos podem ser definidos com especialista | `AP_OBITO` é flag administrativa de saída e `AP_DTOCOR` não é exclusivamente data de óbito. Há fonte capaz de identificar óbito e data com completude adequada? |
| Seguimento | Horizonte fixo, por exemplo 12 meses, escolhido antes da análise | A série de 2024–2025 permite janela completa? É necessário ampliar o período de dados? |
| Estimando | Diferença de risco no horizonte escolhido entre estratégias, sob pressupostos observacionais explícitos | É defensável estimar efeito comparativo com covariáveis e eventos disponíveis? |
| Confundidores | Idade, sexo, raça/cor, diagnóstico e demais fatores clínicos disponíveis antes do tempo zero | As APAC contêm severidade, comorbidades, exames e fatores de escolha da modalidade em qualidade e temporalidade suficientes? |

## Leitura preliminar das fontes locais

- A APAC dialítica contém registros mensais/autorizativos, não uma tabela de pacientes pronta. Repetições por competência, continuidade, transferência e identificação longitudinal precisam ser resolvidas antes de formar uma coorte.
- A auditoria prévia encontrou autorizações associadas a mais de um valor de identificador pseudonimizado. Isso não prova troca ou erro, mas impede usar o número da autorização como chave de pessoa e deixa a estabilidade do identificador individual por validar.
- `ATD_DTPDR` e `ATD_DTCLI` têm valores futuros muito distantes. A varredura de 05/11/2026 confirmou datas calendariamente válidas, não que sejam clinicamente verdadeiras. Até esclarecer a origem, esses campos não devem definir tempo zero ou seguimento.
- A flag `AP_OBITO` e o motivo de saída apresentam coerência interna documentada, mas isso não comprova cobertura de óbitos nem fornece, por si só, uma data de evento confiável.
- SIH N17–N19 é agregado para essa finalidade e não pode ser ligado publicamente à APAC como desfecho individual. SIA agregado e CNES também não fornecem uma coorte comparadora.
- Para diálise versus cuidado conservador, não foi identificada nas fontes locais uma população elegível não dialítica. Essa comparação não é estimável com os dados atualmente reunidos.

## Critérios de viabilidade antes de qualquer estimativa

Uma análise comparativa individual só deve avançar se forem demonstrados todos estes itens:

1. Identificador individual utilizável e estável no período, com avaliação de ausência, mudanças e colisões.
2. Definição reproduzível de primeira exposição e tempo zero, separando inícios, continuidade, transferência e mudança de modalidade.
3. Comparador clinicamente apropriado e positividade plausível: pacientes com perfis comparáveis recebem ambas as estratégias.
4. Desfecho definido com fonte, data, cobertura e seguimento suficientes.
5. Covariáveis prognósticas e de seleção medidas antes do tratamento em quantidade suficiente para enfrentar confundimento por indicação.
6. Janela temporal sem censura administrativa diferencial e critérios explícitos de elegibilidade.

Se algum item central falhar, registrar a pergunta como não estimável com as fontes atuais e restringir o relatório a descrição ou associação compatível com a unidade de dados. Não apresentar diferenças brutas entre modalidades como efeito do tratamento.

## Próxima reunião técnica

Levar a um nefrologista e a um epidemiologista clínico: a tabela de códigos SIGTAP por modalidade, a nota de auditoria APAC, a distribuição de datas futuras por competência/valor e este rascunho. Solicitar decisão sobre população, comparador, tempo zero e desfecho; em paralelo, procurar a documentação técnica de campo ATDAC e validar identificador/continuidade sem exportar identificadores pessoais.
