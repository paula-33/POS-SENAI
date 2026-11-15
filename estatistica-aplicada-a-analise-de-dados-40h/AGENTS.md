# Repository Guidelines

## Project Structure & Module Organization

This repository contains course materials and applied analysis projects. In `estatistica-aplicada-a-analise-de-dados-40h/`, the renal disease study is under `Trabalho-final/`: Markdown plans and reports sit at the project root, Jupyter notebooks are in `Notebook/`, and datasets are organized under `Dados/`. Data folders use numbered stages: `00_inventario`, `01_fontes_originais`, `02_derivados_preliminares`, `03_bases_analiticas`, and `04_documentacao_e_auditoria`. Keep large raw inputs out of Git as specified in that project's `.gitignore`. Other course directories contain their own exercises and assets.

## Build, Test, and Development Commands

There is no repository-wide build system or automated test suite. For the renal analysis, create and activate a Python environment, then install dependencies:

```sh
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r estatistica-aplicada-a-analise-de-dados-40h/requirements.txt
jupyter lab
```

Open notebooks from `Trabalho-final/Notebook/` and run cells in order. Run audit scripts in `Trabalho-final/Dados/04_documentacao_e_auditoria/` with Python; read the script header and related `LEIA-ME` first.

## Coding Style & Naming Conventions

Use 4-space Python indentation, descriptive `snake_case` names, and comments for non-obvious assumptions. In notebooks, document data sources, filters, transformations, and interpretation with Markdown headings. Name notebooks descriptively in Portuguese and preserve the numbered stage/category prefix, such as `04_TRATAMENTO_E_ANALISE_<tema>.ipynb`. Preserve the numbered data-stage folders and use UTF-8 for Markdown and CSV documentation.

## Testing Guidelines

No formal test framework or coverage target is configured. Validate notebook changes by executing affected cells in order. For data transformations, compare row counts, keys, date ranges, missing values, and totals against source documentation; record checks and caveats in the relevant audit notes. Do not treat exploratory outputs as validated results without documenting the checks.

## Commit & Pull Request Guidelines

Recent commits use short imperative or descriptive subjects, for example `Organiza dados e documenta análise renal` and `Add dice roll exercise notebook`. Keep commits focused and explain the affected course or analysis. Pull requests should summarize the change, list relevant notebooks or data docs, describe validation, and link an issue when available. Include screenshots only when a visual notebook or rendered asset change needs review.

## Data & Configuration Safety

Never commit `.env`, virtual environments, editor settings, raw source archives, or local backup copies. Do not overwrite original datasets; write transformed outputs to the appropriate derived or analytical folder and document provenance, filters, and limitations. Keep credentials and personal or sensitive data out of notebooks and Git history.
