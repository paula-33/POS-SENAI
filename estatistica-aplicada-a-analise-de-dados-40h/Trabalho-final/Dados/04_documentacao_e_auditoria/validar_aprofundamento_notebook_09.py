"""Reconcilia os resultados O1–O5 com as fontes atualizadas, sem gravar dados.

Executar da raiz do curso com .venv/bin/python. Leia o LEIA-ME dos artefatos
finais: comparação territorial jan–out, séries mensais completas e taxas anuais.
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
    base = projeto / registro['base']
    assert hashlib.sha256(base.read_bytes()).hexdigest() == registro['sha256_base']
    for nome, esperado in registro['fontes_sha256'].items():
        assert hashlib.sha256((projeto / nome).read_bytes()).hexdigest() == esperado, nome
    painel = pd.read_csv(base, sep=';')
    mensal = pd.read_csv(entrega / 'exploracao_mensal.csv', sep=';')
    territorial = pd.read_csv(entrega / 'exploracao_territorial.csv', sep=';')
    regional = pd.read_csv(entrega / 'exploracao_regional.csv', sep=';')
    concentracao = pd.read_csv(entrega / 'exploracao_concentracao.csv', sep=';')
    temporal = pd.read_csv(entrega / 'exploracao_resumo_temporal.csv', sep=';')
    direcoes = pd.read_csv(entrega / 'exploracao_direcoes_uf.csv', sep=';').set_index('sigla_uf')
    conjunta = pd.read_csv(entrega / 'exploracao_mudancas_conjuntas.csv', sep=';')
    assert painel.shape[0] == 648 and painel.sih_n17_n19_internacoes_tabnet.isna().sum() == 0
    assert len(territorial) == 54 and len(mensal) == 24 and len(conjunta) == 9
    assert conjunta.n_ufs.sum() == 27
    for ind, coluna, meses in [('SIA', 'sia_hemodialise_quantidade_aprovada', 12),
                                ('SIH', 'sih_n17_n19_internacoes_tabnet', 12)]:
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
    # O1: conferir cada célula integrada diretamente contra os dois CSVs fontes.
    fontes = projeto / 'Dados/03_bases_analiticas/atualizacao_sih_sia_20261115'
    for sistema, coluna in [('sia', 'sia_hemodialise_quantidade_aprovada'), ('sih', 'sih_n17_n19_internacoes_tabnet')]:
        fonte = pd.read_csv(fontes / f'{sistema}_uf_mes.csv', dtype={'codigo_uf': str})
        fonte = fonte[fonte.ano_mes.between('2024-01', '2025-12')]
        integrado = painel.assign(codigo_uf=painel.cod_uf.astype(str).str.zfill(2)).set_index(['codigo_uf', 'competencia'])[coluna].sort_index()
        origem = fonte.set_index(['codigo_uf', 'ano_mes']).valor.sort_index()
        np.testing.assert_array_equal(integrado.index.to_numpy(), origem.index.to_numpy())
        np.testing.assert_array_equal(integrado, origem)
    assert painel[['cod_uf', 'ano', 'mes']].duplicated().sum() == 0
    assert painel.populacao_ibge_referencia_anual.gt(0).all()
    assert painel.groupby(['sigla_uf', 'ano']).populacao_ibge_referencia_anual.nunique().eq(1).all()
    # O2/O5: eventos, testes condicionais e sensibilidades, independentes do módulo.
    from scipy import stats
    from statsmodels.stats.multitest import multipletests
    c = pd.read_csv(entrega / 'comparacao_uf_jan_out.csv', sep=';').set_index('sigla_uf')
    a, b = c.sia_variacao_absoluta > 0, c.sih_variacao_absoluta > 0
    eventos = pd.read_csv(entrega / 'probabilidades_basicas.csv', sep=';')
    esperados = [a.sum(), b.sum(), (a & b).sum(), (a | b).sum(), ((c.sia_variacao_absoluta < 0) & (c.sih_variacao_absoluta < 0)).sum()]
    np.testing.assert_array_equal(eventos.ufs_favoraveis, esperados)
    np.testing.assert_allclose(eventos.probabilidade, np.array(esperados)/27)
    p_sia = stats.binomtest(int(a.sum()), 27, p=.5).pvalue
    p_sih = stats.binomtest(int(b.sum()), 27, p=.5).pvalue
    rho, p_rho = stats.spearmanr(c.sia_variacao_pct, c.sih_variacao_pct)
    inf = pd.read_csv(entrega / 'inferencias_familia_3.csv', sep=';')
    np.testing.assert_allclose(inf.p_valor, [p_sia, p_sih, p_rho])
    np.testing.assert_allclose(inf.p_valor_holm, multipletests([p_sia,p_sih,p_rho], method='holm')[1])
    np.testing.assert_allclose(inf.iloc[2].estatistica_ou_positivos, rho)
    sens = pd.read_csv(entrega / 'sensibilidade_janelas.csv', sep=';')
    for _, linha in sens.iterrows():
        coluna = 'sia_hemodialise_quantidade_aprovada' if linha.indicador == 'SIA' else 'sih_n17_n19_internacoes_tabnet'
        totais = painel[painel.mes <= linha.mes_final].groupby('ano')[coluna].sum()
        assert linha.total_2024 == totais[2024] and linha.total_2025 == totais[2025]
        np.testing.assert_allclose(linha.variacao_pct, 100*(totais[2025]/totais[2024]-1))
    # O3: a série ampliada tem 36 meses, sem usar população de 2023.
    ampliada = pd.read_csv(entrega / 'serie_sia_ampliada.csv', sep=';')
    origem = pd.read_csv(fontes / 'sia_uf_mes.csv').groupby('ano_mes').valor.sum()
    assert len(ampliada) == 36
    np.testing.assert_array_equal(ampliada.set_index('ano_mes').valor.sort_index(), origem.sort_index())
    datas = pd.to_datetime(ampliada.ano_mes + '-01')
    np.testing.assert_array_equal(ampliada.dias_mes, datas.dt.days_in_month)
    np.testing.assert_allclose(ampliada.media_por_dia_calendario, ampliada.valor / datas.dt.days_in_month)
    # O4: os totais regionais usam uma única população de cada UF-ano.
    taxas = pd.read_csv(entrega / 'taxa_sia_anual_regiao.csv', sep=';').set_index(['regiao','ano']).sort_index()
    por_uf = painel.groupby(['sigla_uf','regiao','ano']).agg(volume=('sia_hemodialise_quantidade_aprovada','sum'), pop=('populacao_ibge_referencia_anual','first')).reset_index()
    reg = por_uf.groupby(['regiao','ano'])[['volume','pop']].sum().sort_index()
    np.testing.assert_array_equal(taxas.sia_quantidade_aprovada, reg.volume)
    np.testing.assert_array_equal(taxas.populacao_ibge_referencia_anual, reg['pop'])
    np.testing.assert_allclose(taxas.taxa_sia_por_100_mil, 100000*reg.volume/reg['pop'])
    n = json.loads((projeto / 'Notebook/09_ANALISE_ESTATISTICA_E_PREVISAO_DRC.ipynb').read_text())
    celulas = [c for c in n['cells'] if c['cell_type'] == 'code']
    assert [c['execution_count'] for c in celulas] == list(range(1, len(celulas)+1))
    assert not any(o['output_type'] == 'error' for c in celulas for o in c['outputs'])
    print(f'OK: objetivos O1–O5 reconciliados com as fontes, sete tabelas exploratórias e resultados associados; hashes preservados; {len(celulas)} células sequenciais sem erro.')


if __name__ == '__main__':
    validar()
