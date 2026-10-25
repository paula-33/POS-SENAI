# Organizar repositório — Plano de implementação

> **Execução:** seguir `superpowers:executing-plans` após revisão do plano.

**Objetivo:** facilitar a navegação por disciplina e manter arquivos locais fora do Git.

**Abordagem:** manter a hierarquia existente, padronizar os nomes das duas pastas de disciplina, incluir um README na raiz e mover o notebook solto de Python para sua disciplina.

**Escopo:** `.gitignore`, `README.md`, `questao-01.ipynb` e renomeação das pastas `Materia_01` e `Estatistica`. Preservar o conteúdo e a pasta de trabalho final já existente.

## Tarefas

- [x] Renomear `Materia_01` para `programacao-python-para-ciencia-de-dados-30h` e `Estatistica` para `estatistica-aplicada-a-analise-de-dados-40h`.
- [x] Mover `questao-01.ipynb` para a pasta de Python.
- [x] Criar `README.md` na raiz com links para as disciplinas e trabalhos principais.
- [x] Criar `.gitignore` incluindo `.DS_Store`, `.venv/`, `venv/`, `env/`, `__pycache__/` e `*.py[cod]`.
- [x] Remover `.DS_Store` já versionados do índice, preservando arquivos locais.
- [x] Atualizar caminhos absolutos nos documentos de Estatística e conferir links e estado final do Git.

Ruling: atualizei os caminhos absolutos antigos nos documentos de Estatística para caminhos relativos — as referências apontariam para um diretório que foi renomeado — custo se errado: apenas a forma exibida do caminho muda.
