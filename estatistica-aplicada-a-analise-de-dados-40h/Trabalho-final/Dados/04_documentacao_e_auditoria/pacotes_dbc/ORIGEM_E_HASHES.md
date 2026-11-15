# Wheels locais para leitura de DBC

Os projetos e versões vêm do PyPI oficial: [`dbc-reader 0.1.2`](https://pypi.org/project/dbc-reader/0.1.2/) e [`dbf-reader 0.2.2`](https://pypi.org/project/dbf-reader/0.2.2/). O PyPI publica essas versões como source distributions, não wheels. Os arquivos fonte foram baixados do PyPI, conferidos contra os SHA-256 da página de release e então empacotados localmente em wheels universais para Python 3.

| Artefato | Origem | SHA-256 do artefato usado para build | SHA-256 do wheel local |
|---|---|---|---|
| `dbc_reader-0.1.2-py3-none-any.whl` | `dbc_reader-0.1.2.tar.gz` | `b22ef34b99ea48afe2d1cc32f570bd3207b924bd193006f4d9906be72e9c58e5` | `76a8323a1b986c9ff4a6482dd246025d39012212e08f6e4ec361ceca8707fd9b` |
| `dbf_reader-0.2.2-py3-none-any.whl` | `dbf_reader-0.2.2.tar.gz` | `f8b63053ac816cfb3bde184e703441b12c49206fde335c322de65a072e86c94b` | `ac443035d4bbaffd7be1f33b83cbc11cc45962362aa6349fbd6316c6c50cd043` |

Os hashes dos wheels também estão em `SHA256SUMS.txt`. `dbf-reader` é a dependência de `dbc-reader` e foi fixada em `requirements.txt` para builds reproduzíveis. O wheel contém o executável `blast-dbf-darwin` sem permissão de execução; o setup de auditoria concede `+x` somente ao arquivo instalado dentro do ambiente Python. Em Apple Silicon, esse executável x86_64 funciona com Rosetta, disponível neste Mac.

Instalação offline no venv do projeto:

```sh
.venv-sih-audit/bin/python -m pip install --no-index \
  --find-links=Trabalho-final/Dados/04_documentacao_e_auditoria/pacotes_dbc \
  dbc_reader==0.1.2 dbf-reader==0.2.2
```

A instalação funcional e a leitura de `RDAC2401.dbc` foram verificadas em `.venv-sih-audit` (4.315 registros, 113 campos). Não é necessário baixar novamente os DBCs.
