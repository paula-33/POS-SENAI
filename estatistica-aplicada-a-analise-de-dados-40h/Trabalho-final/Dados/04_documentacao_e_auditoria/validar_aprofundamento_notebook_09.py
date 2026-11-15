"""Confere os CSVs da seção 12.3 contra o painel original, sem gravar dados.

Executar da raiz do curso com .venv/bin/python. Leia o LEIA-ME dos artefatos
finais: SIH usa jan–out, taxas SIA são anuais, ausência não é zero.
"""
from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd


def validar():
    projeto = Path(__file__).resolve().parents[2]
    entrega = projeto / 'Dados/03_bases_analiticas/analise_estatistica_final_2024_2025'
    base = projeto / 'Dados/03_bases_analiticas/descritiva_territorial_2024_2025/painel_descritivo_uf_mes_2024_2025.csv'
    registro = json.loads((entrega / 'registro_execucao.json').read_text())
    assert hashlib.sha256(base.read_bytes()).hexdigest() == registro['sha256_base']
    painel = pd.read_csv(base, sep=';')
    mensal = pd.read_csv(entrega / 'exploracao_mensal.csv', sep=';')
    territorial = pd.read_csv(entrega / 'exploracao_territorial.csv', sep=';')
    regional = pd.read_csv(entrega / 'exploracao_regional.csv', sep=';')
    concentracao = pd.read_csv(entrega / 'exploracao_concentracao.csv', sep=';')
    temporal = pd.read_csv(entrega / 'exploracao_resumo_temporal.csv', sep=';')
    direcoes = pd.read_csv(entrega / 'exploracao_direcoes_uf.csv', sep=';').set_index('sigla_uf')
    conjunta = pd.read_csv(entrega / 'exploracao_mudancas_conjuntas.csv', sep=';')
    assert painel.shape[0] == 648 and painel.sih_n17_n19_internacoes_tabnet.isna().sum() == 1
    assert len(territorial) == 54 and len(mensal) == 22 and len(conjunta) == 9
    assert conjunta.n_ufs.sum() == 27
    for ind, coluna, meses in [('SIA', 'sia_hemodialise_quantidade_aprovada', 12),
                                ('SIH', 'sih_n17_n19_internacoes_tabnet', 10)]:
        dados = painel[painel.mes <= meses]
        assert dados[coluna].notna().all()
        for ano in [2024, 2025]:
            esperado = dados[dados.ano == ano].groupby('mes')[coluna].sum()
            obtido = mensal[mensal.indicador == ind].set_index('mes')[f'valor_{ano}']
            np.testing.assert_allclose(obtido.sort_index(), esperado.sort_index())
            resumo = temporal[(temporal.indicador == ind) & (temporal.ano == ano)].iloc[0]
            assert resumo.meses == meses and resumo.total == esperado.sum()
            assert resumo.mes_min == esperado.idxmin() and resumo.mes_max == esperado.idxmax()
            np.testing.assert_allclose(resumo.cv_pct, 100 * esperado.std() / esperado.mean())
        janela = painel[painel.mes <= 10]
        totais = janela.groupby(['sigla_uf', 'ano'])[coluna].sum().unstack()
        mudanca = totais[2025] - totais[2024]
        obtido = territorial[territorial.indicador == ind].set_index('sigla_uf').sort_index()
        np.testing.assert_allclose(obtido.variacao_absoluta, mudanca.sort_index())
        pct = 100 * mudanca / totais[2024]
        np.testing.assert_allclose(obtido.variacao_pct, pct.sort_index())
        q1, q3 = pct.quantile([.25, .75])
        np.testing.assert_array_equal(obtido.extremo_iqr, ((pct < q1-1.5*(q3-q1)) | (pct > q3+1.5*(q3-q1))).sort_index())
        for ano in [2024, 2025]:
            np.testing.assert_allclose(obtido[f'participacao_{ano}_pct'], 100 * totais[ano].sort_index() / totais[ano].sum())
            cinco = totais[ano].nlargest(5)
            linha = concentracao[(concentracao.indicador == ind) & (concentracao.ano == ano)].iloc[0]
            assert linha.cinco_maiores_ufs == ', '.join(cinco.index)
            np.testing.assert_allclose(linha.participacao_cinco_maiores_pct, 100 * cinco.sum()/totais[ano].sum())
        np.testing.assert_allclose(obtido.contribuicao_crescimento_pp, 100 * mudanca.sort_index()/totais[2024].sum())
        esperado_direcao = np.where(mudanca > 0, 'aumento', np.where(mudanca < 0, 'reducao', 'empate'))
        np.testing.assert_array_equal(direcoes.loc[mudanca.index, f'direcao_{ind.lower()}'], esperado_direcao)
        esperado_reg = janela.groupby(['regiao', 'ano'])[coluna].sum().unstack()
        obtido_reg = regional[regional.indicador == ind].set_index('regiao').sort_index()
        for ano in [2024, 2025]:
            np.testing.assert_allclose(obtido_reg[f'valor_{ano}'], esperado_reg[ano].sort_index())
        np.testing.assert_allclose(obtido_reg.variacao_pct, 100*(esperado_reg[2025]/esperado_reg[2024]-1))
    for _, linha in conjunta.iterrows():
        assert linha.n_ufs == ((direcoes.direcao_sia == linha.direcao_sia) & (direcoes.direcao_sih == linha.direcao_sih)).sum()
    for ano in [2024, 2025]:
        anual = painel[painel.ano == ano].groupby('sigla_uf').agg(
            volume=('sia_hemodialise_quantidade_aprovada', 'sum'),
            populacao=('populacao_ibge_referencia_anual', 'first'))
        for ind in ['SIA', 'SIH']:
            obtido = territorial[territorial.indicador == ind].set_index('sigla_uf').sort_index()
            np.testing.assert_allclose(obtido[f'taxa_sia_anual_{ano}_por_100_mil'], 100000 * anual.volume/anual.populacao)
    n = json.loads((projeto / 'Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb').read_text())
    celulas = [c for c in n['cells'] if c['cell_type'] == 'code']
    assert [c['execution_count'] for c in celulas] == list(range(1, len(celulas)+1))
    assert not any(o['output_type'] == 'error' for c in celulas for o in c['outputs'])
    print(f'OK: sete tabelas reconciliadas; base SHA-256 preservada; {len(celulas)} células sequenciais sem erro.')


if __name__ == '__main__':
    validar()
