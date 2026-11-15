# Limitações e próximos passos — auditoria DRC

## Decisão de encerramento interno

A auditoria local está encerrada para o escopo territorial do projeto. Os arquivos DBC foram relidos, os hashes disponíveis foram conferidos e as exceções APAC foram reproduzidas. O painel analítico permanece restrito a SIA agregado, SIH TabNet N17–N19 e população IBGE. Não há correção local adicional que transforme APAC em coorte individual ou N18 em medida diretamente equivalente ao TabNet.

O N18 reextraído (213.789 linhas; 213.788 com `IDENT=1`) é coerente como subconjunto de N17–N19 nas 647 células TabNet preenchidas. O CSV histórico de 368.917 linhas é incompatível com a releitura atual dos DBCs e permanece apenas como artefato histórico. A diferença de 12 linhas entre duas rotinas antigas não é reproduzível porque o código e a saída linha a linha da rotina de 368.905 não foram preservados; ela não bloqueia o painel atual.

## Limitações de dados e próximos passos externos

| Tema | Evidência local | Dependência externa | Critério para encerrar | Efeito enquanto aberta |
|---|---|---|---|---|
| Maturidade SIH 2025 | Quedas amplas em novembro/dezembro e uma célula RR/dezembro ausente no TabNet. | Nova extração TabNet datada ou confirmação do DATASUS de fechamento das competências. | Comparar a nova extração com a versão atual e registrar data, células e diferenças. | Manter novembro/dezembro fora da inferência SIH; RR/dezembro não é zero. |
| Unidade operacional N18 | N18 reextraído fica abaixo de N17–N19, mas DBC é por processamento e TabNet é por atendimento/AIH aprovada. | Esclarecimento DATASUS ou tabulação oficial com filtros idênticos. | Demonstrar a mesma unidade, período e regra de contagem. | N18 não entra em totais finais; N17–N19 segue como indicador hospitalar do painel. |
| Datas APAC `ATD_DTPDR` e `ATD_DTCLI` | 146 e 1.162 datas posteriores a 2025, inclusive anos distantes, embora sintaticamente válidas. | Especificação técnica ATDAC aplicável ou validação com fonte clínica. | Explicar origem dos valores e aprovar regra documentada de tratamento. | Não usar essas datas para tempo zero, duração ou seguimento. |
| Continuidade APAC | 49,3% dos 81.416 pares são autorreferências; 13,2% não têm alvo no recorte; 94,9% das linhas tipo 2 não trazem referência anterior. | Regra oficial de reapresentação/renovação e validação da estabilidade de `AP_CNSPCN`. | Mostrar que a chave liga a mesma pessoa e que as cadeias obedecem à regra. | Não formar trajetórias, pacientes únicos ou coorte APAC. |
| Óbito e desfecho APAC | Flags e motivo de saída são coerentes; `AP_DTOCOR` também ocorre quando `AP_OBITO=0`. | Dicionário/regra de completude e, se necessário, fonte de mortalidade vinculável. | Definir desfecho, data e cobertura com validação independente. | Não estimar mortalidade ou sobrevida. |

## Limitações metodológicas e próximos passos

| Decisão necessária | Responsável sugerido | Condição mínima |
|---|---|---|
| Pergunta de efetividade | Nefrologista e epidemiologista clínico | Definir população elegível, modalidade/intervenção, comparador e estimando. |
| Desenho observacional | Epidemiologista e equipe de dados | Definir tempo zero comum, seguimento, desfecho, censura e covariáveis de confundimento. |
| Fonte de comparador e desfecho | Gestor da base e equipe clínica | Comprovar cobertura, vínculo permitido e qualidade para elegíveis não expostos e desfechos. |
| Uso da previsão | Coordenação do projeto | Atualizar a série e validar novamente; com 24 meses, a projeção é somente exploratória. |

Sem essas condições, o resultado metodologicamente correto é manter o projeto como análise descritiva/ecológica, sem inferência causal ou de efetividade.

## Próximos passos operacionais

1. Encaminhar a [minuta de solicitação técnica ao DATASUS](SOLICITACAO_TECNICA_DATASUS_2026-11-15.md), que reúne maturidade SIH, compatibilidade N18 e campos ATDAC.
2. Com a resposta ou nova extração datada, comparar as células SIH, registrar o corte e reexecutar o notebook 09. N18 continua fora dos totais se a equivalência operacional não for demonstrada.
3. Com a resposta técnica APAC, decidir se datas, continuidade, identificador e desfecho são utilizáveis. Sem validação, encerrar a frente longitudinal como não estimável.
4. Apenas se a etapa anterior for favorável, aplicar o [checklist para decisão clínica e epidemiológica](../../CHECKLIST_DECISAO_CLINICA_EPIDEMIOLOGICA_DRC.md) antes de desenhar qualquer coorte.
5. Atualizar e revalidar a previsão SIA quando houver série temporal mais longa; até então, conservar o cenário de 2026 como exploratório.

## Registro de verificação externa — 15/11/2026

A página oficial de versões APAC lista `layout_Exportacao_APAC.pdf` (09/07/2026) e `LERNOTAS.TXT` (21/10/2026), mas não disponibiliza na listagem uma especificação recente dos campos dialíticos ATDAC. As consultas de cronograma e versões mínimas do SIA retornaram “sessão inválida”, portanto não forneceram evidência sobre remessas ou atualização das competências analisadas. A busca não autoriza recodificar datas APAC nem declarar madura a série SIH; a solicitação técnica permanece necessária.

Fontes consultadas: [versões APAC](https://sia.datasus.gov.br/versao/listar_ftp_apac.php) e [consulta de remessas SIA](https://sia.datasus.gov.br/remessa/remessa.php).

## Limitações decorrentes das etapas 2 a 4 — 15/11/2026

- **Limitação de maturidade e compatibilidade SIH/N18 (etapa 2):** não há no repositório resposta do DATASUS nem nova extração TabNet datada. Por isso, não se confirma a maturidade de novembro/dezembro de 2025 nem a equivalência operacional entre N18 em DBC e “Internações” no TabNet. A inferência mantém janeiro–outubro, RR/dezembro é valor desconhecido e N18 fica fora dos totais.
- **Limitação longitudinal da APAC (etapa 3):** datas sem semântica confirmada, continuidade não reconstruível, identificador sem estabilidade demonstrada e desfecho sem completude validada impedem tempo zero, seguimento e vínculo por pessoa. A APAC fica restrita à auditoria; uma especificação oficial futura poderá reabrir a avaliação.
- **Limitação para inferência clínica (etapa 4):** sem uma fonte longitudinal tecnicamente válida, não há população, comparador, tempo zero, seguimento ou desfecho aprovados para coorte. Portanto, o estudo não estima prognóstico, comparação entre modalidades, efetividade ou causalidade; o checklist clínico permanece condicional.
