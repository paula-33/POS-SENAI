"""Auditoria independente da incerteza convencional e HAC da seção 6.6."""
import importlib.util
from pathlib import Path
import unittest
import pandas as pd

PROJETO = Path(__file__).resolve().parents[1]
ARQUIVO = PROJETO / 'Dados/04_documentacao_e_auditoria/validar_tendencia_sih.py'
spec = importlib.util.spec_from_file_location('auditoria_sih', ARQUIVO)
auditoria = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auditoria)


class InferenciaSIHTest(unittest.TestCase):
    def setUp(self):
        pasta = PROJETO / 'Dados/03_bases_analiticas/tendencia_linear_sih_2024_2025'
        self.base = pd.read_csv(pasta / 'base_mensal_modelo.csv', sep=';')
        self.coef = pd.read_csv(pasta / 'coeficientes.csv', sep=';')

    def conferir(self, coef):
        self.assertTrue(callable(getattr(auditoria, 'validar_inferencia', None)),
                        'Auditoria deve conferir também a incerteza OLS/HAC')
        auditoria.validar_inferencia(self.base, coef)

    def test_reproduz_incerteza_exportada_sem_reutilizar_statsmodels(self):
        self.conferir(self.coef.sample(frac=1, random_state=10))

    def test_rejeita_incerteza_pvalor_r2_e_n_alterados(self):
        for campo in ['erro_padrao', 'ic95_inferior', 'ic95_superior',
                      'p_valor_exploratorio', 'r_quadrado', 'n']:
            for metodo in ['convencional', 'HAC_3_Bartlett_t']:
                coef = self.coef.copy()
                coef.loc[coef.covariancia.eq(metodo) & coef.termo.eq('tempo'), campo] += 1
                with self.subTest(campo=campo, metodo=metodo), self.assertRaises(AssertionError):
                    self.conferir(coef)

    def test_rejeita_termo_ausente_ou_repetido(self):
        for coef in [self.coef.iloc[1:], pd.concat([self.coef, self.coef.iloc[[0]]])]:
            with self.assertRaises(AssertionError):
                self.conferir(coef)


if __name__ == '__main__':
    unittest.main()
