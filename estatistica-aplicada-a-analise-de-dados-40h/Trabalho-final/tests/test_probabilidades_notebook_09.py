"""Confere os eventos compostos usando um conjunto de UFs calculado à mão."""

from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import unittest

import pandas as pd
from IPython.display import display


NOTEBOOK = Path(__file__).resolve().parents[1] / 'Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb'


class ProbabilidadesNotebookTest(unittest.TestCase):
    def test_uniao_intersecao_e_reducao_nao_confundem_empate_com_queda(self):
        # Cinco UFs: ++, +-, -+, --, 00. O empate não é redução.
        comparacao = pd.DataFrame({
            'sigla_uf': ['AA', 'BB', 'CC', 'DD', 'EE'],
            'sia_variacao_pct': [1, 1, -1, -1, 0],
            'sih_variacao_pct': [1, -1, 1, -1, 0],
        })
        contexto = {'pd': pd, 'comparacao': comparacao, 'display': display}
        notebook = json.loads(NOTEBOOK.read_text(encoding='utf-8'))
        with redirect_stdout(StringIO()):
            for celula in notebook['cells']:
                if celula['cell_type'] == 'code' and 'probabilidades_basicas' in celula.get('metadata', {}).get('tags', []):
                    exec(''.join(celula['source']), contexto)
        self.assertIn('estudo_probabilidades', contexto, 'A seção deve calcular os cinco eventos.')
        resultado = contexto['estudo_probabilidades']
        self.assertEqual(resultado['ufs_favoraveis'].tolist(), [2, 2, 1, 3, 1])
        self.assertEqual(resultado['ufs_total'].tolist(), [5, 5, 5, 5, 5])
        self.assertEqual(resultado['probabilidade'].tolist(), [0.4, 0.4, 0.2, 0.6, 0.2])


if __name__ == '__main__':
    unittest.main()
