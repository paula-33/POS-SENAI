"""Reconcilia a tendência SIH sem usar as funções do notebook.

Leia docs/Trabalho-final/Dados/03_bases_analiticas/tendencia_linear_sih_2024_2025/LEIA-ME.md. Executar com a .venv da raiz.
Confere fontes, agregação, OLS por numpy, seis origens, métricas e manifestos.
"""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


def validar_inferencia(base, coeficientes):
    """Reconstrói covariâncias OLS/HAC Bartlett(3) com numpy, sem statsmodels."""
    from scipy.stats import t

    X = np.column_stack([np.ones(len(base)), base.tempo.to_numpy()])
    y = base.internacoes.to_numpy(dtype=float)
    n, k = X.shape
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    residuo = y - X @ beta
    inversa = np.linalg.inv(X.T @ X)
    convencional = inversa * (residuo @ residuo) / (n-k)
    escores = X * residuo[:, None]
    miolo = escores.T @ escores
    for lag in range(1, 4):
        cruzado = escores[lag:].T @ escores[:-lag]
        miolo += (1 - lag/4) * (cruzado + cruzado.T)
    hac = inversa @ miolo @ inversa * n/(n-k)
    esperadas = {(c, termo) for c in ['convencional', 'HAC_3_Bartlett_t']
                 for termo in ['intercepto', 'tempo']}
    assert len(coeficientes) == 4
    assert set(zip(coeficientes.covariancia, coeficientes.termo)) == esperadas
    r2 = 1 - (residuo @ residuo) / np.sum((y-y.mean())**2)
    for metodo, covariancia in [('convencional', convencional), ('HAC_3_Bartlett_t', hac)]:
        grupo = (coeficientes.loc[coeficientes.covariancia.eq(metodo)]
                 .set_index('termo').loc[['intercepto', 'tempo']])
        erro = np.sqrt(np.diag(covariancia))
        margem = t.ppf(.975, n-k) * erro
        np.testing.assert_allclose(grupo.estimativa, beta)
        np.testing.assert_allclose(grupo.erro_padrao, erro)
        np.testing.assert_allclose(grupo.ic95_inferior, beta-margem)
        np.testing.assert_allclose(grupo.ic95_superior, beta+margem)
        np.testing.assert_allclose(grupo.p_valor_exploratorio, 2*t.sf(np.abs(beta/erro), n-k), atol=1e-14)
        np.testing.assert_allclose(grupo.r_quadrado, r2)
        assert grupo.n.eq(n).all()


def validar():
    projeto = Path(__file__).resolve().parents[2]
    pasta = projeto / 'Dados/03_bases_analiticas/tendencia_linear_sih_2024_2025'
    registro = json.loads((pasta / 'registro_execucao.json').read_text())
    for nome, esperado in registro['fontes_sha256'].items():
        assert hashlib.sha256((projeto / nome).read_bytes()).hexdigest() == esperado, nome
    assert hashlib.sha256((projeto / 'Notebook/analise_renal.py').read_bytes()).hexdigest() == registro['modulo_sha256']
    fonte = pd.read_csv(projeto / 'Dados/03_bases_analiticas/atualizacao_sih_sia_20261115/sih_uf_mes.csv')
    b = pd.read_csv(pasta / 'base_mensal_modelo.csv', sep=';')
    origem = fonte.groupby('ano_mes').valor.sum().sort_index()
    assert b.ano_mes.tolist() == pd.period_range('2024-01', '2025-12', freq='M').astype(str).tolist()
    np.testing.assert_array_equal(b.internacoes, origem)
    np.testing.assert_array_equal(b.tempo, np.arange(24))
    assert b.n_ufs.eq(27).all() and b.internacoes.sum() == 322783
    np.testing.assert_array_equal(b.dias_mes, pd.PeriodIndex(b.ano_mes, freq='M').days_in_month)
    X = np.column_stack([np.ones(24), np.arange(24)])
    beta = np.linalg.lstsq(X, b.internacoes, rcond=None)[0]
    coef = pd.read_csv(pasta / 'coeficientes.csv', sep=';')
    for _, grupo in coef.groupby('covariancia', sort=False):
        np.testing.assert_allclose(grupo.estimativa, beta)
        assert grupo.n.eq(24).all()
    validar_inferencia(b, coef)
    assert registro['hac'] == dict(maxlags=3, kernel='bartlett', use_correction=True, use_t=True)
    ajust = pd.read_csv(pasta / 'ajustes_residuos.csv', sep=';')
    np.testing.assert_allclose(ajust.ajustado, X @ beta)
    np.testing.assert_allclose(ajust.residuo, b.internacoes - X @ beta, atol=1e-8)
    residuos = b.internacoes.to_numpy() - X @ beta
    hat = np.diag(X @ np.linalg.inv(X.T @ X) @ X.T)
    cook = residuos**2 / (2 * (residuos @ residuos / 22)) * hat / (1-hat)**2
    np.testing.assert_allclose(ajust.cook, cook)
    np.testing.assert_array_equal(ajust.inspecionar_cook, cook > 4/24)
    v = pd.read_csv(pasta / 'validacao_temporal.csv', sep=';')
    assert v.ano_mes.tolist() == b.ano_mes.iloc[18:].tolist()
    assert (v.ultimo_mes_treino < v.ano_mes).all()
    for j, linha in v.iterrows():
        alvo = 18+j
        estimativa = np.linalg.lstsq(X[:alvo], b.internacoes.iloc[:alvo], rcond=None)[0]
        np.testing.assert_allclose(linha.previsto_linear, X[alvo] @ estimativa)
        assert linha.previsto_referencia == b.internacoes.iloc[alvo-12]
        assert linha.observado == b.internacoes.iloc[alvo]
        assert linha.ultimo_mes_treino == b.ano_mes.iloc[alvo-1] and linha.n_treino == alvo
    m = pd.read_csv(pasta / 'metricas_validacao.csv', sep=';').set_index('metodo')
    for metodo in ['linear','referencia']:
        erro = v.observado - v[f'previsto_{metodo}']
        np.testing.assert_allclose(v[f'erro_{metodo}'], erro)
        np.testing.assert_allclose(m.loc[metodo, ['mae','rmse']], [abs(erro).mean(), np.sqrt((erro**2).mean())])
    assert not registro['projecao_exportada'] and not (pasta / 'projecao_exploratoria.csv').exists()
    for diretorio in [pasta, projeto / 'Dados/03_bases_analiticas/analise_estatistica_final_2024_2025']:
        manifesto = json.loads((diretorio / 'manifesto_sha256.json').read_text())
        for nome, esperado in manifesto.items():
            assert hashlib.sha256((diretorio / nome).read_bytes()).hexdigest() == esperado, nome
    n = json.loads((projeto / 'Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb').read_text())
    codigos = [c for c in n['cells'] if c['cell_type'] == 'code']
    assert [c['execution_count'] for c in codigos] == list(range(1, len(codigos)+1))
    assert not any(o['output_type']=='error' for c in codigos for o in c['outputs'])
    print('OK: 24 meses, OLS e incerteza convencional/HAC independentes, Cook, seis origens, MAE/RMSE, hashes e ausência de projeção reconciliados.')


if __name__ == '__main__':
    validar()
