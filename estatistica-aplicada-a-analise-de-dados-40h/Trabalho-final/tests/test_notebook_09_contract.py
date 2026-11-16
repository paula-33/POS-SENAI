"""Contratos numéricos da coleta versionada usada pelo notebook 09."""
from pathlib import Path
import sys
import unittest

import pandas as pd

PROJETO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJETO / 'Notebook'))
from analise_renal import integrar_bases, comparar_periodos


class NotebookNoveContratoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fontes = PROJETO / 'Dados/03_bases_analiticas/atualizacao_sih_sia_20261115'
        sia = pd.read_csv(fontes / 'sia_uf_mes.csv', dtype={'codigo_uf': str})
        sih = pd.read_csv(fontes / 'sih_uf_mes.csv', dtype={'codigo_uf': str})
        h = pd.read_csv(PROJETO / 'Dados/03_bases_analiticas/descritiva_territorial_2024_2025/painel_descritivo_uf_mes_2024_2025.csv', sep=';', dtype={'cod_uf': str})
        dim = h[['cod_uf','sigla_uf','uf','regiao','ano','populacao_ibge_referencia_anual','populacao_data_referencia']].drop_duplicates()
        cls.painel = integrar_bases(sia, sih, dim)

    def test_integracao_reproduz_totais_oficiais_e_rr_observado(self):
        totais = self.painel.groupby('ano')[['sia_hemodialise_quantidade_aprovada','sih_n17_n19_internacoes_tabnet']].sum()
        self.assertEqual(totais.sia_hemodialise_quantidade_aprovada.tolist(), [18311982,18997606])
        self.assertEqual(totais.sih_n17_n19_internacoes_tabnet.tolist(), [156491,166292])
        rr = self.painel.query("sigla_uf == 'RR' and competencia == '2025-12'")
        self.assertEqual(rr.sih_n17_n19_internacoes_tabnet.item(), 14)
        self.assertEqual(len(self.painel), 648)

    def test_jan_out_reproduz_magnitudes_e_direcoes_atualizadas(self):
        c = comparar_periodos(self.painel, 10)
        self.assertEqual(c.sia_2024.sum(),15187201)
        self.assertEqual(c.sia_2025.sum(),15773425)
        self.assertEqual(c.sih_2024.sum(),130752)
        self.assertEqual(c.sih_2025.sum(),137770)
        self.assertEqual((c.sia_variacao_absoluta>0).sum(),25)
        self.assertEqual((c.sih_variacao_absoluta>0).sum(),18)
        self.assertEqual(((c.sia_variacao_absoluta>0)&(c.sih_variacao_absoluta>0)).sum(),16)


if __name__ == '__main__':
    unittest.main()
