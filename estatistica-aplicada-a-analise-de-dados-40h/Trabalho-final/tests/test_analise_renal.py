"""Verifica falhas que alterariam totais, comparações e denominadores do estudo."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest

import numpy as np
import pandas as pd

ARQUIVO = Path(__file__).resolve().parents[1] / 'Notebook/analise_renal.py'
if ARQUIVO.exists():
    spec = importlib.util.spec_from_file_location('analise_renal', ARQUIVO)
    analise = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(analise)
else:
    analise = SimpleNamespace()


class AnaliseRenalTest(unittest.TestCase):
    def setUp(self):
        for nome in ['validar_grade', 'integrar_bases', 'comparar_periodos', 'taxas_anuais']:
            self.assertTrue(callable(getattr(analise, nome, None)), f'Função necessária: {nome}')
        self.meses = pd.period_range('2024-01', '2025-12', freq='M').astype(str).tolist()
        self.base = pd.DataFrame([
            {'codigo_uf': uf, 'ano_mes': m, 'valor': valor, 'status': 'observado'}
            for uf, valor in [('11', 10), ('12', 20)] for m in self.meses])
        self.dim = pd.DataFrame([
            {'cod_uf': uf, 'sigla_uf': sigla, 'uf': nome, 'regiao': 'Norte', 'ano': ano,
             'populacao_ibge_referencia_anual': pop, 'populacao_data_referencia': f'{ano}-07-01'}
            for uf, sigla, nome, pop in [('11', 'RO', 'Rondônia', 1000), ('12', 'AC', 'Acre', 3000)]
            for ano in [2024, 2025]])

    def test_grade_rejeita_uf_mes_duplicada_ou_faltante(self):
        for base in [pd.concat([self.base, self.base.iloc[[0]]]), self.base.iloc[1:]]:
            with self.subTest(linhas=len(base)), self.assertRaises(ValueError):
                analise.validar_grade(base, ['11', '12'], self.meses)

    def test_grade_rejeita_contagem_nao_finita_fracionaria_negativa_ou_ausente(self):
        for valor in [np.nan, np.inf, -1, 1.5, 'erro']:
            base = self.base.copy().astype({'valor': object}); base.loc[0, 'valor'] = valor
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                analise.validar_grade(base, ['11', '12'], self.meses)

    def test_integracao_preserva_fontes_e_rejeita_dimensao_sem_correspondencia(self):
        original = self.base.copy(deep=True)
        painel = analise.integrar_bases(self.base, self.base, self.dim)
        self.assertEqual(len(painel), 48)
        self.assertEqual(painel.sia_hemodialise_quantidade_aprovada.sum(), 720)
        pd.testing.assert_frame_equal(self.base, original)
        with self.assertRaises(ValueError):
            analise.integrar_bases(self.base, self.base, self.dim.iloc[1:])

    def test_integracao_rejeita_populacao_nao_positiva_e_dimensao_duplicada(self):
        dim = self.dim.copy();dim.loc[0, 'populacao_ibge_referencia_anual'] = 0
        for d in [dim, pd.concat([self.dim, self.dim.iloc[[0]]])]:
            with self.subTest(linhas=len(d)), self.assertRaises(ValueError):
                analise.integrar_bases(self.base, self.base, d)

    def test_comparacao_pareia_anos_e_preserva_uma_uf_por_linha(self):
        sia = self.base.copy();sia.loc[sia.ano_mes.str.startswith('2025'), 'valor'] *= 2
        painel = analise.integrar_bases(sia, self.base, self.dim)
        c = analise.comparar_periodos(painel, 10).set_index('sigla_uf')
        self.assertEqual(len(c), 2)
        self.assertEqual(c.loc['RO', 'sia_variacao_absoluta'], 100)
        self.assertEqual(c.loc['RO', 'sia_variacao_pct'], 100)
        self.assertEqual(c.loc['AC', 'sih_variacao_absoluta'], 0)

    def test_comparacao_rejeita_janela_incompleta_e_denominador_zero(self):
        painel = analise.integrar_bases(self.base, self.base, self.dim)
        for d in [painel.iloc[1:], painel.assign(sia_hemodialise_quantidade_aprovada=0)]:
            with self.subTest(linhas=len(d)), self.assertRaises(ValueError):
                analise.comparar_periodos(d, 10)

    def test_taxa_regional_usa_populacao_uma_vez_e_razao_das_somas(self):
        painel = analise.integrar_bases(self.base, self.base, self.dim)
        uf, reg = analise.taxas_anuais(painel)
        self.assertEqual(uf.query("sigla_uf == 'RO' and ano == 2024").iloc[0].taxa_sia_por_100_mil, 12000)
        r = reg.query('ano == 2024').iloc[0]
        self.assertEqual(r.populacao_ibge_referencia_anual, 4000)
        self.assertEqual(r.taxa_sia_por_100_mil, 9000)

    def test_taxa_anual_rejeita_meses_incompletos_ou_populacao_variavel(self):
        painel = analise.integrar_bases(self.base, self.base, self.dim)
        variavel = painel.copy();variavel.loc[0, 'populacao_ibge_referencia_anual'] += 1
        for d in [painel.iloc[1:], variavel]:
            with self.subTest(linhas=len(d)), self.assertRaises(ValueError):
                analise.taxas_anuais(d)

    def test_integracao_exige_status_observado_e_geografia_estavel(self):
        with self.assertRaises(ValueError):
            analise.integrar_bases(self.base.drop(columns='status'), self.base, self.dim)
        for coluna, valor in [('sigla_uf', 'XX'), ('uf', 'Outro nome'), ('regiao', 'Sul')]:
            dim = self.dim.copy(); dim.loc[1, coluna] = valor
            with self.subTest(coluna=coluna), self.assertRaises(ValueError):
                analise.integrar_bases(self.base, self.base, dim)
