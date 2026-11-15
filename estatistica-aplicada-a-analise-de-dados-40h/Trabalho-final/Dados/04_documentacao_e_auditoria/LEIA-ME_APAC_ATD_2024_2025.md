# Microdados SIA/APAC — atendimento dialítico, 2024–2025

## Extração

- Fonte: [DATASUS, arquivos públicos APAC](https://sia.datasus.gov.br/documentos/listar_ftp_apac.php), diretório oficial [SIASUS/200801_/Dados](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/).
- Arquivos: `ATDAC` por UF e competência de janeiro de 2024 a dezembro de 2025.
- Cobertura: 27 UFs × 24 meses = **648 arquivos DBC**, sem competência/UF faltante; tamanho total aproximado de 190 MB.
- Pasta dos arquivos brutos: [`APAC_ATD_2024_2025_bruto/`](../01_fontes_originais/APAC/APAC_ATD_2024_2025_bruto/). Os arquivos originais foram preservados.
- Data de extração e auditoria: 25/10/2026.

## Auditoria estrutural

Os 648 arquivos foram descompactados e lidos. Todos possuem o mesmo esquema ordenado de 65 campos. O conjunto tem **3.186.282 registros** e nenhum arquivo vazio. Campos de interesse presentes em todos os arquivos incluem `AP_CNSPCN`, `AP_MVM`, `AP_CMP`, `AP_PRIPAL`, `AP_TPAPAC`, `AP_DTINIC`, `AP_DTFIM`, `AP_MOTSAI`, `AP_OBITO`, `AP_DTOCOR`, `AP_SEXO`, `AP_NUIDADE`, `AP_RACACOR`, `AP_CIDPRI` e campos clínicos `ATD_*`.

Preenchimento em todos os registros: `AP_MVM`, `AP_CMP`, `AP_TPAPAC`, datas `AP_DTINIC`/`AP_DTFIM`, `AP_MOTSAI`, `AP_OBITO`, sexo, idade, raça/cor e CID principal. `AP_CNSPCN` está vazio em 2,3686% dos registros. `AP_DTOCOR` está vazio em 95,6758%; `ATD_KTVSEM`, `ATD_ALBUMI` e `ATD_PTH` estão vazios em 13,2511%, 7,8203% e 10,2419%, respectivamente. `ATD_DTPDR`, `ATD_DTCLI`, `ATD_HB` e `ATD_FOSFOR` têm cada um 0,0004% de ausência. As datas preenchidas auditadas têm formato de oito dígitos.

## Achados que exigem cautela

- `AP_CMP` nos arquivos de movimento 2024–2025 varia de 202310 a 202512. Para restringir o período analítico, usar e documentar a competência apropriada, não presumir que o nome do arquivo determine a competência do atendimento.
- O identificador `AP_CNSPCN` aparece preenchido em 97,6314% dos registros e tem formato consistente. A sobreposição mensal dos conjuntos de identificadores é um sinal de possível acompanhamento longitudinal, mas **não comprova** formalmente estabilidade da anonimização, unicidade de paciente ou ligação com outros sistemas. Nenhum identificador foi reproduzido neste documento.
- `AP_OBITO=1` em 35.201 registros; `AP_DTOCOR` está preenchido em todos eles, mas também está preenchido em 102.579 registros com `AP_OBITO=0`. A coocorrência não valida por si só o significado, a completude nem a data do óbito. Não interpretar como sobrevida ou mortalidade confirmada sem validar o dicionário e as regras oficiais.
- `AP_TPAPAC` inclui o valor 4 em 12 registros, que requer validação de domínio.
- `AP_PRIPAL` apresenta seis códigos não vazios e 12 registros sem código. Confirmar descrição e modalidade na tabela SIGTAP correspondente antes de separar hemodiálise, diálise peritoneal e outras modalidades.

## Uso analítico e limites

Esta é uma extração administrativa de APAC de atendimento dialítico. Ela pode apoiar uma análise da coorte registrada após validar códigos, competência, regras de autorização/continuidade e a semântica dos desfechos. A base isolada não oferece grupo de pessoas comparável em cuidado conservador e não demonstra eficácia/efetividade causal. Por isso, ainda não foi produzida uma tabela analítica consolidada nem estimativa de mortalidade/sobrevida.

## Próximas validações

1. Conferir o layout oficial vigente e os domínios dos campos de modalidade, tipo de APAC, motivo de saída e óbito.
2. Definir competência e regra para registros reapresentados, continuidade/renovação de APAC e eventuais duplicidades; validar `AP_MVM` versus `AP_CMP`.
3. Validar estabilidade e interpretação do identificador pseudonimizado sem divulgar valores.
4. Avaliar se os dados de óbito e seguimento são suficientes e qual comparador clínico pode ser obtido.
5. Só então derivar uma base analítica, documentando filtros, exclusões e unidade de análise.

## Referências oficiais

- [Documentação e arquivos APAC do SIA/SUS](https://sia.datasus.gov.br/documentos/listar_ftp_apac.php)
- [Serviço do Ministério da Saúde: microdados anonimizados oriundos do SUS](https://www.gov.br/pt-br/servicos/obter-aplicativos-documentos-e-microdados-anonimizados-oriundos-do-sus)
- [Diretório público DATASUS SIASUS](ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Dados/)


## Validação de domínios e indicadores (25/10/2026)

O layout de exportação APAC publicado pelo DATASUS em julho de 2026 descreve a interface de remessa do sistema. Para interpretar os campos do DBC ATDAC, foi consultado também o capítulo do Informe Técnico SIASUS/DATASUS que documenta o layout do arquivo dialítico `ATD*.DBF`; esse documento técnico disponível é de 2019. O layout de diálise lista variáveis clínicas e vários campos condicionais. A presença de um campo no esquema não significa que ele deva estar preenchido em todas as linhas.

- **Tipo de APAC (`AP_TPAPAC`):** o domínio documentado é 1 = inicial, 2 = continuidade, 3 = única. No conjunto: 1.123.437, 2.058.092 e 4.741 registros, respectivamente. Há mais 12 registros com valor 4; todos os 12 também estão sem `AP_PRIPAL`. O valor 4 não consta no domínio consultado e deve ser investigado/excluído de qualquer categorização até esclarecimento.
- **Motivo de saída (`AP_MOTSAI`) e indicadores:** os códigos observados são compatíveis com a tabela da Portaria SAS/MS nº 719/2007: 11–18 alta (33.777 registros), 21–28 permanência (3.054.823), 31 transferência (48.465), 41–43 óbito (35.201) e 51 encerramento administrativo (14.016). Em todos os registros, os indicadores `AP_ALTA`, `AP_PERMAN`, `AP_TRANSF`, `AP_OBITO` e `AP_ENCERR` correspondem exatamente a esses grupos de motivos. Os três códigos de óbito se distribuem em 41=24.069, 42=1.707 e 43=9.425. Isso confirma consistência interna entre motivo e flags, mas não comprova completude nem cobertura de mortalidade de todos os pacientes.
- **Data de ocorrência (`AP_DTOCOR`):** a documentação a descreve como data de ocorrência que substitui o fim de validade da APAC; não como uma variável exclusivamente de data de óbito. Está preenchida nos 35.201 registros com `AP_OBITO=1` e também em 102.579 registros com `AP_OBITO=0`. Portanto, não usar `AP_DTOCOR` isoladamente como data de óbito.
- **Característica do tratamento (`ATD_CARACT`):** o domínio documentado (1 caso novo, 2 continuidade, 3 usuário em trânsito, 4 transferência de local) é observado nos arquivos: 447.035, 2.670.959, 14.710 e 53.566 registros, além de 12 vazios. Os 12 vazios coincidem com os registros de tipo APAC=4/código principal vazio; precisam ser tratados juntos como exceção não classificada.
- **Campos condicionais da parte dialítica:** entre registros `ATD_CARACT=1`, `ATD_MAISNE` apresenta somente S/N/I (149.589/82.688/214.758) e `ATD_SITINI` somente A/H/I (186.407/52.224/208.404), conforme domínios publicados. Entre registros com `ATD_SITTRA=1` (apto a transplante), `ATD_SEAPTO` apresenta apenas os códigos documentados 1–4 (590.695/223.280/198.584/122.771). `ATD_INTERC` e `ATD_SEPERI` usam S/N/I quando preenchidos. Ausências fora das situações em que o layout exige/preconiza o campo são esperadas e não devem ser imputadas como “não”.
- **Datas da primeira diálise e início na clínica (`ATD_DTPDR`, `ATD_DTCLI`):** os valores preenchidos têm formato de data interpretável, mas 146 registros de `ATD_DTPDR` e 1.162 de `ATD_DTCLI` estão depois de 31/12/2025, embora o maior `AP_CMP` observado seja 202512. Os extremos chegam a anos muito distantes. São incompatibilidades temporais que exigem inspeção e exclusão/recodificação documentada antes de usar essas datas em seguimento.
- **Procedimento principal (`AP_PRIPAL`):** aparecem seis códigos não vazios — 0305010026 (586), 0305010107 (2.931.694), 0305010115 (114.761), 0305010166 (129.102), 0305010182 (4.741) e 0305010204 (5.386) — além de 12 vazios. Antes de agrupar modalidades ou comparar tratamentos, conferir a descrição e a vigência de cada código na competência correspondente do SIGTAP.

**Conclusão desta etapa:** os motivos de saída e as flags resumidas são internamente coerentes; os domínios clínicos condicionais conferem nas situações de aplicação; os seis códigos de procedimento foram confirmados em todas as competências SIGTAP baixadas, incluindo todo o intervalo APAC observado. A APAC ainda não está pronta para análise longitudinal de desfecho: resolver os 12 registros sem tipo/procedimento classificado, tratar as datas futuras e definir como tratar autorizações de continuidade, reapresentações e transferências. Ainda não foi criado CSV analítico de pacientes nem estimativa de sobrevida.


## Repetição de autorizações e continuidade (25/10/2026)

A verificação foi feita com identificadores transformados apenas para comparação interna; nenhum valor foi gravado neste relatório.

- Os 3.186.282 registros correspondem a 1.199.885 valores distintos de `AP_AUTORIZ`. Não houve repetição da mesma combinação `AP_AUTORIZ` + `AP_CMP` + `AP_MVM`.
- 1.054.990 números de autorização aparecem em mais de uma competência (`AP_CMP`); nenhum aparece em mais de três competências distintas. 1.050.505 aparecem em mais de um mês de movimento (`AP_MVM`). Assim, somar linhas ou tratar cada linha como APAC/pessoa independente inflaria contagens. A repetição é compatível com registros de continuidade/validade mensal, mas precisa ser confirmada contra as regras do SIA antes de definir uma linha analítica por pessoa-mês ou por autorização.
- 12.065 números de autorização estão associados a mais de um valor não vazio de `AP_CNSPCN` no conjunto. Isso pode refletir inconsistência da chave, mudança de identificador anonimizado ou problema nos dados; impede tratar `AP_AUTORIZ` isoladamente como identificador de pessoa e exige investigação.
- `AP_APACANT` é zero-preenchido quando não há autorização anterior. Ignorando os campos vazios e os valores compostos só por zeros, foram identificadas 149.406 referências a uma APAC anterior; 142.826 apontam para uma autorização encontrada nos arquivos 2024–2025, e 6.580 não foram encontradas nesse recorte. Estas últimas podem se referir a períodos anteriores, mas isso precisa ser verificado.

## Interpretação preliminar dos procedimentos principais

Os seis códigos observados não representam todos hemodiálise. As descrições abaixo eram preliminares e foram corroboradas em documentos públicos da [ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/perfil-do-setor/dados-e-indicadores-do-setor/copy_of_Ficha_Tecnica_IDSS_ab2023_atualizada_em_abr2024__retificacaoo_1.3.pdf), da [Prefeitura do Rio](https://saude.prefeitura.rio/wp-content/uploads/sites/47/2026/05/Edital-de-Chamamento-Publico-no-003.2026-Prestacao-de-Servicos-Ambulatoriais-na-Area-de-Terapia-Renal-Substitutiva-TRS.pdf) e do [Ministério da Saúde](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2008/prt2281_10_10_2008.html). A validação por competência agora foi feita com as versões integrais oficiais do SIGTAP de 2023–2025; ver `../01_fontes_originais/SIGTAP/SIGTAP_2023_2025/`.

- `0305010107`: hemodiálise, máximo 3 sessões/semana.
- `0305010115`: hemodiálise em paciente com sorologia positiva para HIV e/ou hepatite B/C, máximo 3 sessões/semana.
- `0305010204`: hemodiálise pediátrica, máximo 4 sessões/semana.
- `0305010026`: diálise peritoneal intermitente (DPI), máximo 2 sessões/semana.
- `0305010166`: manutenção e acompanhamento domiciliar de paciente em DPA/DPAC.
- `0305010182`: treinamento de paciente submetido a diálise peritoneal DPAC/DPA, por 9 dias.

Essas descrições sugerem que a coorte deve ser delimitada a partir do procedimento principal e da competência, separando hemodiálise de diálise peritoneal e de treinamento/acompanhamento. `AP_PRIPAL` é o procedimento principal registrado na APAC; antes de definir tratamento/exposição, conferir também o restante do registro e os atributos SIGTAP vigentes.

## Complemento da auditoria — 25/10/2026

- **Associação autorização–identificador:** repetida a conferência dos 648 arquivos com identificadores protegidos por hash apenas durante o processamento. Os 12.065 números de `AP_AUTORIZ` associados a mais de um `AP_CNSPCN` ocorrem sempre em mais de uma competência: 730 em duas competências e 11.335 em três. Não houve autorização com múltiplos identificadores limitada a uma competência. Isso não permite decidir se a causa é continuidade, troca de identificador ou inconsistência; `AP_AUTORIZ` não deve ser usado como chave de pessoa. Nenhum identificador ou hash foi salvo no relatório.
- **Datas futuras:** permanecem identificados 146 valores de `ATD_DTPDR` e 1.162 de `ATD_DTCLI` posteriores a 31/12/2025. Não foram corrigidos nem removidos; antes de qualquer uso, é necessário verificar a codificação, as competências correspondentes e as regras do layout. A tentativa de detalhar a distribuição por ano foi interrompida antes de produzir resultado, portanto nenhum resumo por ano é afirmado.
- **SIGTAP:** em tentativa posterior, foi acessado o FTP oficial `ftp2.datasus.gov.br/pub/sistemas/tup/downloads/`; os ZIPs de janeiro/2023 a dezembro/2025 foram baixados, testados e lidos. Os seis códigos observados em `AP_PRIPAL` constam nas 36 competências, e as descrições oficiais correspondem aos rótulos listados acima. A planilha por competência, os ZIPs e os checksums estão em `../01_fontes_originais/SIGTAP/SIGTAP_2023_2025/`.

**Decisão analítica provisória:** manter a base APAC bruta preservada e não criar ainda uma coorte ou indicador de sobrevida. As descrições e a presença dos seis procedimentos foram conferidas nas 36 competências SIGTAP 2023–2025. Ainda precisamos confirmar as regras de autorização/continuidade e a estabilidade do identificador, resolver a semântica das datas futuras e classificar os 12 registros sem procedimento principal. A consistência interna dos campos de óbito continua insuficiente para afirmar completude ou eficácia do tratamento.

## Rechecagem do estado local (25/10/2026)

O diretório bruto contém 648 arquivos com prefixo `ATD` (27 UFs × 24 competências) segundo os nomes; isso confirma presença nominal, não leitura, integridade criptográfica ou completude do conteúdo. O manifesto SIH não cobre os arquivos APAC. Nesta sessão não havia leitor DBC instalado, então os totais e achados de conteúdo registrados acima não foram reextraídos independentemente. Mantêm-se como resultados da auditoria prévia documentada, não como contagens reproduzidas nesta rechecagem.

**Status:** conjunto bruto presente; auditoria estrutural e de campos relatada previamente; validade semântica para seguimento longitudinal ainda não demonstrada nesta rechecagem; coorte, mortalidade e sobrevida não prontas para análise.

## Reextração de exceções e integridade local (05/11/2026)

Com o leitor DBC já instalado no ambiente virtual local, foi feita nova varredura dos 648 arquivos, sem download ou alteração dos brutos. Foram lidos novamente **3.186.282 registros**. Uma rotina nova calculou SHA-256 individual de cada arquivo e guardou hashes apenas como inventário de integridade desta execução (não havia manifesto APAC anterior contra o qual comparar). Resumos e hashes estão em [`auditoria_excecoes_20261105_v2/`](../02_derivados_preliminares/APAC/auditoria_excecoes_20261105_v2/); a rotina reexecutável está em [`auditar_excecoes_apac.py`](auditar_excecoes_apac.py). Nenhum identificador de paciente ou autorização foi exportado.

Resultados reproduzidos: 12 registros têm `AP_TPAPAC=4` e `AP_PRIPAL` vazio; não foram encontrados outros registros nesse critério. `ATD_DTPDR` contém 146 datas sintaticamente válidas posteriores a 31/12/2025 e `ATD_DTCLI`, 1.162; não houve valor não vazio que falhasse a leitura estrita `AAAAMMDD`/calendário nesta checagem. Há valores com anos como 2202 e 4024, além de datas em 2026–2029. A distribuição por ano e por `AP_CMP`, além dos valores de data sem chaves de registro, está nos CSVs do diretório de auditoria. Validade de calendário não resolve sua validade semântica.

O leitor confirma os valores observados, mas não explica por si só se as datas anômalas são erro de origem, codificação, digitação ou outra regra do layout. A listagem oficial do DATASUS inclui `Layout_Exportacao_APAC.pdf`, datado de 09/07/2026 ([página oficial de documentos APAC](https://sia.datasus.gov.br/documentos/listar_ftp_apac.php)); essa listagem confirma a disponibilidade de um layout de interface, mas não esclarece as variáveis específicas da parte dialítica dos DBCs ATDAC. A consulta à página não permitiu obter documentação oficial de campo que explique os anos distantes vistos em `ATD_DTPDR` e `ATD_DTCLI`. Exemplos e frequências, sem chaves pessoais, estão em [`valores_datas_futuras.csv`](../02_derivados_preliminares/APAC/auditoria_excecoes_20261105_v2/valores_datas_futuras.csv). Até validação técnica do leiaute ATDAC, as datas ficam fora de qualquer seguimento; não foram corrigidas nem excluídas dos brutos.

A busca local pelos termos das contagens antigas do SIH também só encontrou documentação e a rotina de contagem agregada do CSV preservadas; não foi localizado o script/saída linha a linha que gerou 368.905. A diferença de 12 segue não localizável com o material presente e não bloqueia o painel N17–N19. A auditoria agregada de continuidade de 05/11/2026 tampouco validou estabilidade longitudinal do identificador, semântica da autorização/continuidade ou completude de óbito; essas são limitações para coorte e próximos passos externos, consolidados em [Limitações e próximos passos — auditoria DRC](PENDENCIAS_EXTERNAS_E_METODOLOGICAS_2026-11-15.md).

### Consulta externa de documentação (15/11/2026)

A página oficial de versões APAC lista `layout_Exportacao_APAC.pdf` (09/07/2026) e `LERNOTAS.TXT` (21/10/2026). A listagem não identifica especificação recente dos campos dialíticos ATDAC. As consultas públicas de cronograma e de versões mínimas do SIA exigiram sessão autenticada e não retornaram conteúdo. Assim, a consulta não esclarece as datas futuras, o tipo 4, a continuidade ou a estabilidade do identificador; não foi aplicada recodificação. Ver [registro de limitações e próximos passos](PENDENCIAS_EXTERNAS_E_METODOLOGICAS_2026-11-15.md).


## Esclarecimento documental dos campos dialíticos (05/11/2026)

O [Informe Técnico SIASUS 2019.07, layout do arquivo de APAC dialítica ATD](https://rfsaldanha.github.io/sis/assets/sia/Informe_Tecnico_SIASUS_2019_07.pdf) descreve `ATD_DTPDR` como data de início da primeira diálise e `ATD_DTCLI` como data de início da diálise na clínica, ambas em formato `AAAAMMDD`. O documento também descreve `AP_TPAPAC` como 1=inicial, 2=continuidade e 3=única, e `AP_APACANT` como número da APAC anterior. A página oficial atual do DATASUS lista um layout genérico de exportação APAC, mas não fornece nessa listagem uma especificação recente do ATDAC ([documentos APAC](https://sia.datasus.gov.br/documentos/listar_ftp_apac.php)).

Isso esclarece os rótulos e o formato documentados, mas **não explica** datas de início em anos posteriores às competências APAC ou em anos muito distantes. Como os campos representam inícios de diálise, não se deve corrigir ano por inferência, converter datas em branco, ou usá-las como tempo zero/seguimento. É necessário esclarecimento técnico sobre a origem/versão do ATDAC ou validação com fonte clínica independente.

O layout documenta que existe uma referência a APAC anterior, mas isso, sozinho, não valida uma cadeia longitudinal de pessoa: foram observadas referências para fora do recorte 2024–2025 e autorizações ligadas a mais de um `AP_CNSPCN`. `AP_AUTORIZ` identifica autorização, não pessoa. A estabilidade da anonimização, a lógica de reapresentação/continuidade e a completude dos campos de saída/óbito continuam sem validação. Nenhum identificador foi salvo nesta rechecagem documental.


## Auditoria agregada das referências de continuidade APAC (05/11/2026)

Foi executada uma leitura independente dos 648 ATDAC DBCs locais, totalizando novamente 3.186.282 linhas. `AP_AUTORIZ`, `AP_APACANT` e `AP_CNSPCN` foram usados somente em memória para formar contagens agregadas; nenhum número, identificador, hash ou registro individual foi exportado. Script: [`auditar_cadeias_apac.py`](auditar_cadeias_apac.py). Saídas agregadas: [`auditoria_continuidade_20261105_v1/`](../02_derivados_preliminares/APAC/auditoria_continuidade_20261105_v1/).

Principais contagens, com unidades distintas explicitadas:

- 1.199.885 autorizações distintas observadas; 12.065 autorizações aparecem associadas a mais de um valor não vazio de identificador pseudonimizado no recorte.
- 149.406 linhas têm `AP_APACANT` não vazio/não zero; essas linhas se reduzem a 81.416 pares distintos autorização-filho → referência anterior.
- Entre esses pares distintos, 40.170 são autorreferências (número atual igual ao indicado como anterior); 70.660 referências apontam para um número de autorização encontrado no período; 10.756 apontam para número não encontrado no recorte. Ausência no recorte não significa necessariamente erro: a referência pode anteceder janeiro/2024.
- Entre referências com alvo presente, houve alguma interseção do identificador pseudonimizado em 67.653 pares; em 1.308 pares com identificadores dos dois lados não se observou interseção; 5.098 pares tinham múltiplos identificadores em pelo menos um dos lados e são ambíguos para comparação simples. Essas categorias não devem ser somadas como mutuamente exclusivas.
- 1.953.456 linhas `AP_TPAPAC=2` não trazem `AP_APACANT` preenchido; não interpretar esse campo ausente como prova de inexistência de APAC anterior.
- Em 77.203 pares com datas parseáveis no conjunto, a data inicial observada da APAC filha veio após o fim observado da anterior em 35.608; em 41.587 a data inicial ficou antes do fim registrado da anterior; em 8 caiu no mesmo dia. Como os intervalos foram resumidos entre snapshots e competências, essa comparação não confirma continuidade clínica nem erro por si só.

A definição documental de `AP_APACANT` como número da APAC anterior não explica autorreferências, grande ausência do campo em APAC de continuidade ou referências sem alvo neste recorte. A igualdade de identificador em referência direta é um sinal de consistência local, mas não prova estabilidade longitudinal geral; diferenças podem refletir anonimização, cadastro, transferência ou inconsistência. **Resultado:** a cadeia administrativa de autorização não pode ser usada como seguimento de pessoa sem esclarecimento técnico e validação de identificador/datas. Nenhuma coorte foi criada.
