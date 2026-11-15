"""Contratos entre o plano estatístico e o notebook final."""

import json
from pathlib import Path
import unittest


NOTEBOOK = Path(__file__).resolve().parents[1] / "Notebook" / "09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb"


def fontes_de_codigo():
    conteudo = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    return "\n".join(
        "".join(celula["source"])
        for celula in conteudo["cells"]
        if celula["cell_type"] == "code"
    )


class NotebookNoveContratoTest(unittest.TestCase):
    def test_imputacao_sensibilidade_usa_jan_out(self):
        codigo = fontes_de_codigo()
        self.assertIn("mes <= 10", codigo)
        self.assertIn("fator_crescimento_jan_out", codigo)
        self.assertNotIn("fator_crescimento_jan_nov", codigo)

    def test_mape_usa_observados_da_validacao(self):
        codigo = fontes_de_codigo()
        self.assertIn("erro / observados_validacao", codigo)
        self.assertNotIn("erro / teste", codigo)


if __name__ == "__main__":
    unittest.main()
