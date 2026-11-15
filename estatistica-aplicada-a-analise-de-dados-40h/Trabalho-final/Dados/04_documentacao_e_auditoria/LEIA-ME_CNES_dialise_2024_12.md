# CNES — diálise e serviços de atenção à doença renal crônica (competência 2024/12)

## Decisão de uso no estudo

Após revisar o significado dos campos, estes dados foram **excluídos do conjunto analítico principal**: são registros cadastrais de uma competência e não informam capacidade operacional máxima, vagas ou atendimento efetivamente realizado. Os arquivos permanecem nesta pasta como documentação da extração e referência contextual; não devem ser usados como indicador central de oferta real. O plano passa a priorizar dados de produção e pacientes distintos por CNES publicados no [SUS 360º — Monitor de Hemodiálise](https://sus360.saude.gov.br/painel/hemodialise/), sujeitos a download e validação.

## Objetivo

Relacionar o perfil complementar de diálise do CNES (`tbDialise`) ao cadastro de estabelecimentos (`tbEstabelecimento`) e aos vínculos de serviço/classificação (`rlEstabServClass`), descrevendo registros de hemodiálise e diálise peritoneal por município e UF. A competência analisada é dezembro de 2024.

## Arquivos derivados

- [`../02_derivados_preliminares/CNES/cnes_dialise_servicos_2024_12.csv`](../02_derivados_preliminares/CNES/cnes_dialise_servicos_2024_12.csv): registros de serviço/classificação 130/001 e 130/005, enriquecidos com CNES e localização. Cada linha corresponde a um vínculo registrado, não necessariamente a um estabelecimento distinto.
- [`../02_derivados_preliminares/CNES/cnes_dialise_estabelecimentos_2024_12.csv`](../02_derivados_preliminares/CNES/cnes_dialise_estabelecimentos_2024_12.csv): uma linha por estabelecimento com pelo menos um vínculo 130/001 ou 130/005; contém indicadores derivados, situação/código de desativação e campos não pessoais do perfil de diálise.
- [`../02_derivados_preliminares/CNES/cnes_dialise_resumo_uf_2024_12.csv`](../02_derivados_preliminares/CNES/cnes_dialise_resumo_uf_2024_12.csv): agregação por UF e Brasil, com contagens distintas de CNES e totais de máquinas segundo o recorte descrito abaixo.
- [`../02_derivados_preliminares/CNES/cnes_dialise_perfis_sem_classificacao_dialitica_2024_12.csv`](../02_derivados_preliminares/CNES/cnes_dialise_perfis_sem_classificacao_dialitica_2024_12.csv): nove registros de `tbDialise` sem vínculo 130/001 nem 130/005, mantidos à parte para auditoria do critério.
- [`../01_fontes_originais/CNES/BASE_DE_DADOS_CNES_202412.ZIP`](../01_fontes_originais/CNES/BASE_DE_DADOS_CNES_202412.ZIP): arquivo-fonte original preservado.

Os CSVs derivados estão em UTF-8 com BOM e separados por ponto e vírgula. Campos pessoais (nomes, CPF e identificadores profissionais) foram excluídos. Chaves CNES, códigos territoriais e variáveis institucionais foram mantidos para permitir a análise e a auditoria das junções.

## Relação entre as tabelas e critério

1. `tbDialise202412` fornece o perfil complementar com salas e máquinas de hemodiálise. Seus campos pessoais não foram exportados.
2. `tbEstabelecimento202412` fornece o CNES e os códigos de município/UF usados para enriquecer geograficamente os registros. O vínculo foi feito pela chave `CO_UNIDADE`; não foram levados ao CSV nomes, endereços, CNPJ/CPF ou dados de responsáveis.
3. `rlEstabServClass202412` registra os vínculos de serviço e classificação. Para estimar estabelecimentos com modalidade dialítica cadastrada, foram selecionados serviço 130 e classificações 001 (tratamento dialítico — hemodiálise) e 005 (tratamento dialítico — peritoneal). As descrições foram conferidas na tabela de domínio CNES do próprio ZIP e na [Portaria GM/MS nº 389/2014](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2014/prt0389_13_03_2014.html), que dispõe sobre a atenção à pessoa com doença renal crônica e apresenta o serviço 130 e suas classificações.
4. Os vínculos do arquivo de serviços foram relacionados aos estabelecimentos pelo `CO_UNIDADE`, e depois ao perfil de diálise pela mesma chave. A localização foi ligada ao município cadastrado no estabelecimento.
5. A coluna `atendimento_*_sus_codigo` preserva o código do campo de atendimento SUS do registro. As contagens “SUS” consideram o código `1` no campo ambulatorial ou hospitalar. O dicionário de dados e as tabelas de domínio devem ser consultados junto à documentação oficial do [CNES](https://cnes.datasus.gov.br/pages/downloads/documentacao.jsp); códigos originais permanecem disponíveis no CSV de vínculos para rastreabilidade.
6. Os números por UF contam CNES distintos em cada indicador. Um mesmo estabelecimento pode estar presente em mais de uma modalidade e em mais de uma categoria de atendimento; portanto, não se devem somar colunas sobrepostas.

O arquivo de exceções contém nove perfis sem classificação dialítica 001/005: sete sem qualquer vínculo de serviço 130 e dois apenas com a classificação 130/004 (nefrologia em geral). Eles não foram incluídos nas contagens de estabelecimentos com hemodiálise ou diálise peritoneal. Isso não significa que os dados estejam necessariamente errados; indica apenas que o perfil complementar não foi acompanhado das classificações que definem os recortes desta extração.

## Principais resultados descritivos

Na competência 2024/12, os arquivos derivados registram:

- 1.788 CNES com classificação 130/001 de hemodiálise; 1.233 com indicação de atendimento ambulatorial SUS e 1.022 com indicação de atendimento hospitalar SUS. São 1.509 CNES com indicação SUS em pelo menos uma dessas modalidades.
- 782 CNES com classificação 130/005 de diálise peritoneal; 682 com indicação de atendimento ambulatorial SUS e 388 com indicação de atendimento hospitalar SUS. São 714 CNES com indicação SUS em pelo menos uma modalidade.
- 1.811 CNES distintos no conjunto de estabelecimentos com pelo menos uma das classificações 001 ou 005. Há sobreposição entre as modalidades.
- Entre os estabelecimentos com perfil complementar (`tbDialise`) e classificação 130/001 com indicação SUS, os campos de máquinas somam 28.567 próprias e 3.103 de terceiros. Restringindo a esses mesmos registros sem código de motivo de desativação informado, as somas são 27.054 e 2.904, respectivamente.

Essas contagens descrevem cadastros/vínculos existentes na competência, não pacientes tratados, produção realizada, sessões efetivamente prestadas nem capacidade operacional confirmada. Os totais de máquinas refletem valores declarados no perfil complementar e não comprovam que todos os equipamentos estavam instalados, funcionando, disponíveis ou destinados exclusivamente ao SUS. A ausência de código de motivo de desativação foi preservada como condição cadastral; isoladamente, não é prova suficiente de funcionamento efetivo.

## Limites e uso analítico

- É um retrato de uma única competência, 2024/12; não sustenta inferência de tendência temporal.
- Registro de serviço e indicação de atendimento SUS são informação cadastral, não confirmação de utilização nem de acesso efetivo pela população.
- O total de estabelecimentos não equivale ao número de pacientes ou de sessões. Para produção assistencial, usar a base SIA/SUS; para internações, usar SIH/SUS, respeitando conceitos e denominadores distintos.
- Indicadores populacionais exigem compatibilizar geografia e período. Uma taxa por população residente pode ser calculada após a junção com a estimativa IBGE adequada.
- As tabelas CNES são atualizáveis e refletem registros administrativos. Para comparações com competências de 2025 em diante, revisar alterações de layout, categorias e regras de registro na documentação CNES da competência correspondente.

## Fontes

- Ministério da Saúde/DATASUS. [CNES — Documentação: dicionário de dados e tabelas de domínio](https://cnes.datasus.gov.br/pages/downloads/documentacao.jsp).
- Ministério da Saúde. [Portaria GM/MS nº 389, de 13 de março de 2014](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2014/prt0389_13_03_2014.html).
- Ministério da Saúde/DATASUS. Arquivo CNES competência 2024/12, `../01_fontes_originais/CNES/BASE_DE_DADOS_CNES_202412.ZIP`, preservado nesta pasta; tabelas e domínios internos usados na junção e leitura dos códigos.

**Extração/organização registrada em 25/10/2026.**
