"""Contratos da preparação SIH e da validação sem informação futura."""
from pathlib import Path
import sys
import unittest
import numpy as np
import pandas as pd

PROJETO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJETO / 'Notebook'))
import analise_renal as renal


class TendenciaSIHTest(unittest.TestCase):
    def setUp(self):
        pasta = PROJETO / 'Dados/03_bases_analiticas/atualizacao_sih_sia_20261115'
        self.sih = pd.read_csv(pasta / 'sih_uf_mes.csv', dtype={'codigo_uf': str})
        self.ref = pd.read_csv(pasta / 'series_mensais_brasil.csv')

    def preparar(self, dados=None, ref=None):
        self.assertTrue(callable(getattr(renal, 'preparar_serie_sih', None)), 'Preparação SIH necessária')
        return renal.preparar_serie_sih(self.sih if dados is None else dados, self.ref if ref is None else ref)

    def test_serie_reconcilia_24_meses_e_totais_sem_alterar_fontes(self):
        original = self.sih.copy(deep=True)
        b = self.preparar(self.sih.sample(frac=1, random_state=8))
        self.assertEqual(len(b), 24)
        self.assertEqual(b.tempo.tolist(), list(range(24)))
        self.assertTrue(b.n_ufs.eq(27).all())
        self.assertEqual(b.groupby(b.ano_mes.str[:4]).internacoes.sum().tolist(), [156491, 166292])
        self.assertEqual(b.loc[b.ano_mes == '2024-02', 'dias_mes'].item(), 29)
        pd.testing.assert_frame_equal(self.sih, original)

    def test_preparacao_rejeita_lacuna_duplicata_uf_estranha_status_e_contagem(self):
        casos = [self.sih.iloc[1:], pd.concat([self.sih, self.sih.iloc[[0]]]),
                 self.sih.assign(codigo_uf=self.sih.codigo_uf.replace({'11': '99'})),
                 self.sih.assign(status='imputado'), self.sih.drop(columns='status')]
        for valor in [np.nan, np.inf, -1, 1.5, 'erro']:
            d = self.sih.astype({'valor': object}); d.loc[0, 'valor'] = valor; casos.append(d)
        for d in casos:
            with self.subTest(linhas=len(d)), self.assertRaises(ValueError):
                self.preparar(d)

    def test_reconciliacao_rejeita_total_incompativel_ou_mes_repetido(self):
        ref = self.ref.copy(); ref.loc[ref.sistema.eq('sih'), 'total'] += 1
        for r in [ref, pd.concat([self.ref, self.ref.query("sistema == 'sih'").iloc[[0]]])]:
            with self.assertRaises(ValueError):
                self.preparar(ref=r)

    def test_validacao_temporal_usa_so_passado_e_referencia_homologa(self):
        b = self.preparar()
        self.assertTrue(callable(getattr(renal, 'validar_tendencia_temporal', None)))
        v, m = renal.validar_tendencia_temporal(b)
        self.assertEqual(v.ano_mes.tolist(), [f'2025-{i:02}' for i in range(7, 13)])
        self.assertTrue((v.ultimo_mes_treino < v.ano_mes).all())
        self.assertEqual(v.n_treino.tolist(), list(range(18,24)))
        np.testing.assert_allclose(v.previsto_referencia, b.internacoes.iloc[6:12])
        # Alterar dezembro não pode mudar ajustes que preveem julho–novembro.
        alterada = b.copy(); alterada.loc[23, 'internacoes'] += 10000
        v2, _ = renal.validar_tendencia_temporal(alterada)
        np.testing.assert_allclose(v.previsto_linear, v2.previsto_linear)
        for metodo in ['linear', 'referencia']:
            erro = v.observado - v[f'previsto_{metodo}']
            linha = m.set_index('metodo').loc[metodo]
            self.assertAlmostEqual(linha.mae, abs(erro).mean())
            self.assertAlmostEqual(linha.rmse, np.sqrt((erro**2).mean()))
        with self.assertRaises(ValueError):
            renal.validar_tendencia_temporal(b.iloc[::-1])


class ArtefatosNotebookTest(unittest.TestCase):
    def test_execucao_preserva_nove_figuras_embutidas(self):
        import json
        n = json.loads((PROJETO / 'Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb').read_text())
        imagens = [o for c in n['cells'] if c['cell_type'] == 'code'
                   for o in c['outputs'] if 'image/png' in o.get('data', {})]
        self.assertEqual(len(imagens), 9, 'Cinco figuras descritivas e quatro de modelagem devem aparecer no notebook e HTML')


if __name__ == '__main__':
    unittest.main()
