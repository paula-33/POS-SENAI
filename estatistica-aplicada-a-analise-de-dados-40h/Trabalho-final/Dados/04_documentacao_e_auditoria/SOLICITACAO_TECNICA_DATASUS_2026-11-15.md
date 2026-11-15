# Minuta de solicitação técnica ao DATASUS

**Destino sugerido:** canal oficial “Fale conosco” do DATASUS.  
**Assunto:** esclarecimentos sobre SIH/TabNet 2025 e campos ATDAC

## 1. Maturidade da série SIH/TabNet

Solicitamos confirmar o status de consolidação ou revisão das competências de novembro e dezembro de 2025 na tabulação SIH/SUS, por local de internação, medida “Internações”, morbidade “Insuficiência renal” (CID-10 N17–N19), por UF e mês de atendimento.

Na extração local registrada, novembro e dezembro de 2025 apresentaram quedas em relação ao mesmo período de 2024; em dezembro, Roraima estava sem valor. Precisamos saber:

1. Se as competências de novembro e dezembro de 2025 estavam consolidadas na data da consulta;
2. Se houve revisão posterior dos valores ou da célula de Roraima/dezembro;
3. Qual data de extração/corte deve ser citada para uso analítico;
4. Se há regra específica de atualização ou defasagem aplicável a essas competências.

## 2. Compatibilidade operacional N18

Em 648 DBCs RD de 2024–2025, filtramos `DIAG_PRINC` iniciado por N18 e `DT_INTER` no período. A releitura produziu 213.789 registros; nas 647 células TabNet preenchidas, esse recorte ficou abaixo do agregado N17–N19. Não solicitamos igualdade entre categorias diagnósticas distintas.

Solicitamos orientação sobre a comparação entre esse recorte de microdados por competência de processamento e a tabulação TabNet por mês de atendimento/“Internações”, especialmente quanto a:

1. Revisões, reapresentações e cobertura do arquivo RD por competência;
2. Tratamento de `IDENT` e AIHs de prorrogação de longa permanência;
3. Procedimento recomendado para reproduzir uma tabulação por diagnóstico principal com unidade comparável à medida “Internações”.

## 3. Campos da APAC dialítica ATDAC

Em 648 arquivos ATDAC de 2024–2025 foram encontrados 146 valores de `ATD_DTPDR` e 1.162 de `ATD_DTCLI` posteriores a 31/12/2025, inclusive anos distantes, embora sejam datas válidas no calendário. Também há 12 linhas com `AP_TPAPAC=4` e `AP_PRIPAL` vazio.

O informe técnico disponível documenta os campos como datas de início e os tipos 1, 2 e 3 de APAC, mas não explica esses valores. Solicitamos:

1. O leiaute técnico vigente ou a regra de codificação aplicável a `ATD_DTPDR`, `ATD_DTCLI`, `AP_TPAPAC`, `AP_APACANT` e `AP_CNSPCN` nos arquivos ATDAC;
2. A interpretação dos valores de tipo 4 e dos registros sem procedimento principal;
3. A regra de reapresentação, renovação e referência de autorização anterior;
4. Se `AP_CNSPCN` pode ser considerado estável para seguimento longitudinal em arquivos públicos e quais limitações devem ser aplicadas.

## Anexos agregados sugeridos

- `auditoria_sih_dbc_reconciliacao_20261105_221707/resumo.csv`;
- `auditoria_excecoes_20261105_v2/resumo.csv` e `datas_futuras_por_ano.csv`;
- `auditoria_continuidade_20261105_v1/referencias_apac_agregadas.csv`.

Não anexar DBCs nem identificadores de paciente/autorização. Registrar protocolo, data de envio e resposta recebida em uma nova nota de auditoria.
