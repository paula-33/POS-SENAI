"""Validações e agregações do estudo ecológico SIA/SIH/IBGE.

Não baixa dados nem altera entradas. A validação temporal ajusta somente a reta SIH. As funções recusam
agregações incompletas em vez de transformar ausências em zero.
"""
import numpy as np
import pandas as pd

SIA = 'sia_hemodialise_quantidade_aprovada'
SIH = 'sih_n17_n19_internacoes_tabnet'
POP = 'populacao_ibge_referencia_anual'


def validar_grade(dados, ufs, meses, coluna='valor'):
    """Exige exatamente a grade UF-mês e contagens inteiras observadas."""
    chaves = ['codigo_uf', 'ano_mes']
    if dados[chaves].isna().any().any() or dados.duplicated(chaves).any():
        raise ValueError('Chave UF-mês ausente ou repetida')
    esperado = {(str(u), str(m)) for u in ufs for m in meses}
    observado = set(map(tuple, dados[chaves].astype(str).to_numpy()))
    if not esperado or observado != esperado:
        raise ValueError('Grade UF-mês incompleta ou inesperada')
    valores = pd.to_numeric(dados[coluna], errors='coerce').to_numpy(dtype=float)
    if not (np.isfinite(valores).all() and (valores >= 0).all() and (valores == np.floor(valores)).all()):
        raise ValueError('Contagens devem ser inteiras, finitas e não negativas')
    if 'status' in dados and not dados.status.eq('observado').all():
        raise ValueError('Valor sem status observado')


def integrar_bases(sia, sih, dimensao):
    """Integra atendimento 2024–2025 e população por UF-ano, sem alterar fontes."""
    dim = dimensao.copy()
    dim['cod_uf'] = dim.cod_uf.astype(str).str.zfill(2)
    chaves = ['cod_uf', 'ano']
    if dim[chaves].isna().any().any() or dim.duplicated(chaves).any():
        raise ValueError('Dimensão UF-ano incompleta ou repetida')
    geografia = ['sigla_uf', 'uf', 'regiao']
    if (dim[geografia].isna().any().any()
            or dim.groupby('cod_uf')[geografia].nunique().gt(1).any().any()
            or dim.duplicated(['sigla_uf', 'ano']).any()):
        raise ValueError('Geografia UF deve ser estável e unívoca entre anos')
    pop = pd.to_numeric(dim[POP], errors='coerce')
    if not (np.isfinite(pop).all() and pop.gt(0).all()):
        raise ValueError('População deve ser finita e positiva')
    if not dim.populacao_data_referencia.eq(dim.ano.astype(str) + '-07-01').all():
        raise ValueError('Referência populacional diferente de julho do ano')
    meses = pd.period_range('2024-01', '2025-12', freq='M').astype(str)
    ufs = sorted(dim.cod_uf.unique())
    if set(zip(dim.cod_uf, dim.ano)) != {(u, a) for u in ufs for a in [2024, 2025]}:
        raise ValueError('Dimensão não cobre todos os pares UF-ano')
    bases = []
    for entrada, nome in [(sia, SIA), (sih, SIH)]:
        if 'status' not in entrada:
            raise ValueError('Integração exige status observado nas duas fontes')
        d = entrada.loc[entrada.ano_mes.between('2024-01', '2025-12')].copy()
        d['codigo_uf'] = d.codigo_uf.astype(str).str.zfill(2)
        validar_grade(d, ufs, meses)
        d['valor'] = pd.to_numeric(d.valor).astype('int64')
        bases.append(d[['codigo_uf', 'ano_mes', 'valor']].rename(columns={'valor': nome}))
    painel = bases[0].merge(bases[1], on=['codigo_uf', 'ano_mes'], validate='one_to_one')
    painel = painel.rename(columns={'codigo_uf': 'cod_uf', 'ano_mes': 'competencia'})
    painel['ano'] = painel.competencia.str[:4].astype(int)
    painel['mes'] = painel.competencia.str[5:7].astype(int)
    painel = painel.merge(dim, on=chaves, how='left', validate='many_to_one')
    if painel[['sigla_uf', 'uf', 'regiao', POP]].isna().any().any():
        raise ValueError('Dimensão territorial/populacional sem correspondência')
    painel['sih_status'] = 'observado'
    return painel.sort_values(['cod_uf', 'competencia']).reset_index(drop=True)


def comparar_periodos(painel, mes_final=10):
    """Compara os mesmos meses por UF; denominador zero exige outra definição."""
    if mes_final not in range(1, 13):
        raise ValueError('Mês final deve estar entre 1 e 12')
    d = painel.loc[painel.mes.between(1, mes_final) & painel.ano.isin([2024, 2025])].copy()
    meses = [f'{a}-{m:02}' for a in [2024, 2025] for m in range(1, mes_final + 1)]
    for col in [SIA, SIH]:
        validar_grade(d.rename(columns={'cod_uf': 'codigo_uf', 'competencia': 'ano_mes'}), painel.cod_uf.unique(), meses, col)
    totais = d.groupby(['sigla_uf', 'uf', 'regiao', 'ano'])[[SIA, SIH]].sum().unstack('ano')
    tabela = totais.reset_index()
    tabela.columns = ['sigla_uf', 'uf', 'regiao', 'sia_2024', 'sia_2025', 'sih_2024', 'sih_2025']
    for nome in ['sia', 'sih']:
        if not tabela[f'{nome}_2024'].gt(0).all():
            raise ValueError('Variação percentual indefinida: denominador zero')
        delta = tabela[f'{nome}_2025'] - tabela[f'{nome}_2024']
        tabela[f'{nome}_variacao_absoluta'] = delta
        tabela[f'{nome}_variacao_pct'] = 100 * delta / tabela[f'{nome}_2024']
    return tabela


def taxas_anuais(painel):
    """Exige doze meses e população constante por UF-ano; calcula razão das somas."""
    grupos = painel.groupby(['sigla_uf', 'uf', 'regiao', 'ano'])
    for _, g in grupos:
        if len(g) != 12 or set(g.mes) != set(range(1, 13)) or g[POP].nunique(dropna=False) != 1:
            raise ValueError('Ano incompleto ou população variável')
        valores = pd.to_numeric(g[POP], errors='coerce')
        if not (np.isfinite(valores).all() and valores.gt(0).all()):
            raise ValueError('Denominador populacional inválido')
        contagens = pd.to_numeric(g[SIA], errors='coerce')
        if not (np.isfinite(contagens).all() and contagens.ge(0).all()):
            raise ValueError('Quantidade SIA inválida')
    uf = grupos.agg(sia_quantidade_aprovada=(SIA, 'sum'), **{POP: (POP, 'first')}).reset_index()
    regional = uf.groupby(['regiao', 'ano'], as_index=False)[['sia_quantidade_aprovada', POP]].sum()
    for tabela in [uf, regional]:
        tabela['taxa_sia_por_100_mil'] = 100_000 * tabela.sia_quantidade_aprovada / tabela[POP]
    return uf, regional


UFS_BRASIL = ('11', '12', '13', '14', '15', '16', '17', '21', '22', '23',
              '24', '25', '26', '27', '28', '29', '31', '32', '33', '35',
              '41', '42', '43', '50', '51', '52', '53')


def preparar_serie_sih(sih, series_auditadas):
    """Prepara os 24 meses nacionais da extração SIH de 15/11/2026.

    A grade nacional e os totais anuais são contratos desta versão da fonte.
    Uma nova extração exige rever os contratos, nunca imputar diferenças.
    """
    if not {'codigo_uf', 'ano_mes', 'valor', 'status'}.issubset(sih.columns):
        raise ValueError('SIH exige chave, contagem e status observado')
    d = sih.copy()
    d['codigo_uf'] = d.codigo_uf.astype(str)
    meses = pd.period_range('2024-01', '2025-12', freq='M').astype(str)
    validar_grade(d, UFS_BRASIL, meses)
    d['valor'] = pd.to_numeric(d.valor).astype('int64')
    base = (d.groupby('ano_mes', as_index=False)
            .agg(internacoes=('valor', 'sum'), n_ufs=('codigo_uf', 'nunique'))
            .sort_values('ano_mes').reset_index(drop=True))
    ref = series_auditadas.loc[series_auditadas.sistema.eq('sih')].copy()
    if ref.ano_mes.duplicated().any() or set(ref.ano_mes) != set(meses):
        raise ValueError('Referência mensal SIH incompleta ou repetida')
    esperado = pd.to_numeric(ref.set_index('ano_mes').total.reindex(meses), errors='coerce')
    if not np.array_equal(base.internacoes.to_numpy(), esperado.to_numpy()):
        raise ValueError('Total mensal diverge da série nacional auditada')
    anuais = base.groupby(base.ano_mes.str[:4]).internacoes.sum()
    if anuais.tolist() != [156491, 166292]:
        raise ValueError('Totais anuais divergem da versão SIH aprovada')
    base['tempo'] = np.arange(24)
    base['dias_mes'] = pd.PeriodIndex(base.ano_mes, freq='M').days_in_month
    return base


def validar_tendencia_temporal(base_mensal):
    """Seis origens crescentes, horizonte de um mês e referência homóloga.

    Todas as previsões consomem somente o passado do mês-alvo. Os valores
    revisados avaliam retrospectivamente a extração atual, não vintages reais.
    """
    import statsmodels.api as sm

    meses = pd.period_range('2024-01', '2025-12', freq='M').astype(str).tolist()
    if (base_mensal.ano_mes.tolist() != meses
            or base_mensal.tempo.tolist() != list(range(24))):
        raise ValueError('Validação exige 24 meses consecutivos em ordem e tempo 0–23')
    y = pd.to_numeric(base_mensal.internacoes, errors='coerce').to_numpy(dtype=float)
    if not (np.isfinite(y).all() and (y >= 0).all() and (y == np.floor(y)).all()):
        raise ValueError('Contagem nacional inválida')
    linhas = []
    for alvo in range(18, 24):
        treino = base_mensal.iloc[:alvo]
        modelo = sm.OLS(y[:alvo], sm.add_constant(treino[['tempo']], has_constant='add')).fit()
        previsto = float(modelo.predict(pd.DataFrame({'const': [1.0], 'tempo': [alvo]})).iloc[0])
        linhas.append(dict(ano_mes=meses[alvo], ultimo_mes_treino=meses[alvo-1],
                           n_treino=alvo, observado=y[alvo], previsto_linear=previsto,
                           previsto_referencia=y[alvo-12], erro_linear=y[alvo]-previsto,
                           erro_referencia=y[alvo]-y[alvo-12]))
    validacao = pd.DataFrame(linhas)
    metricas = pd.DataFrame([
        dict(metodo=metodo, n_previsoes=6, mae=validacao[f'erro_{metodo}'].abs().mean(),
             rmse=np.sqrt(np.square(validacao[f'erro_{metodo}']).mean()))
        for metodo in ['linear', 'referencia']])
    return validacao, metricas
