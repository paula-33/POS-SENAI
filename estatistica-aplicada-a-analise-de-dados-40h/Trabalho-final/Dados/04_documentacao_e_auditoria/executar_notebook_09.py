"""Executa o notebook 09 em kernel limpo e exporta HTML e manifestos.

Execute da raiz do curso: .venv/bin/python caminho/este_script.py
Leia os LEIA-ME das saídas descritivas e da tendência linear SIH.
Não coleta dados nem altera fontes; as figuras/CSVs são gerados pelo notebook.
Os manifestos incluem a documentação disponível em docs/Trabalho-final/.
"""
import hashlib
import json
import os
from pathlib import Path
import tempfile

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter


def executar():
    projeto = Path(__file__).resolve().parents[2]
    notebook = projeto / 'Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb'
    # Jupyter e matplotlib escrevem cache apenas no diretório temporário.
    with tempfile.TemporaryDirectory(prefix='drc-notebook-') as temporario:
        for variavel in ['JUPYTER_CONFIG_DIR', 'JUPYTER_DATA_DIR', 'JUPYTER_RUNTIME_DIR', 'IPYTHONDIR', 'MPLCONFIGDIR']:
            os.environ[variavel] = str(Path(temporario) / variavel.lower())
        os.environ['MPLBACKEND'] = 'module://matplotlib_inline.backend_inline'
        n = nbformat.read(notebook, as_version=4)
        NotebookClient(n, timeout=180, kernel_name='python3',
                       resources={'metadata': {'path': str(projeto / 'Notebook')}}).execute()
        nbformat.write(n, notebook)
        entrega = projeto / 'Dados/03_bases_analiticas/analise_estatistica_final_2024_2025'
        html, _ = HTMLExporter().from_notebook_node(n)
        (entrega / 'notebook_09_executado.html').write_text(html, encoding='utf-8')
    for pasta in [entrega, projeto / 'Dados/03_bases_analiticas/tendencia_linear_sih_2024_2025']:
        arquivos = sorted(f for f in pasta.iterdir() if f.is_file() and f.name != 'manifesto_sha256.json')
        documentacao = projeto.parent / 'docs/Trabalho-final'
        pasta_docs = documentacao / pasta.relative_to(projeto)
        arquivos.extend(sorted(pasta_docs.glob('*.md')))
        arquivos.extend(f for f in [
            documentacao / 'relatorio_final_analise_estatistica_drc_2024_2025.md',
            documentacao / 'plano_analise_estatistica_e_previsao_drc.md',
            documentacao / 'revisao_final_metodologia_e_coerencia_2026-11-15.md',
            documentacao / 'referencias_bibliograficas_doenca_renal_cronica_sus.md',
        ] if f.is_file())
        manifesto = {(f.name if f.parent == pasta else os.path.relpath(f, pasta)):
                     hashlib.sha256(f.read_bytes()).hexdigest() for f in arquivos}
        (pasta / 'manifesto_sha256.json').write_text(
            json.dumps(manifesto, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'OK: {sum(c.cell_type == "code" for c in n.cells)} células executadas; HTML e manifestos exportados.')


if __name__ == '__main__':
    executar()
