import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

def flatten(lista):
    return [item for sublist in lista  for item in sublist]
#dados 2012-2019
folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\emprego\\'
txDesempregoQuarter = pd.read_csv(folderPath+'taxaDesemprego2012-2021.csv', sep=";", decimal=',')
empregadosMes = pd.read_csv(folderPath+'empregados2012-2019.csv', sep=";")
demissoesMes = pd.read_csv(folderPath+'demissoes2012-2019.csv', sep=";")
#fonte https://www.ibge.gov.br/estatisticas/sociais/trabalho/9173-pesquisa-nacional-por-amostra-de-domicilios-continua-trimestral.html?=&t=series-historicas&utm_source=landing&utm_medium=explica&utm_campaign=desemprego
desempregoBrQuarter = pd.read_csv(folderPath+'desempregoBrasil2012-2023.csv', sep=';')

rendimentoMedioQuarter = pd.read_csv(folderPath+'rendimentoMedio2012-2021.csv', sep=";")
txDesemprego = txDesempregoQuarter.filter(regex='T4$|Sigla').copy()
rendimentoMedio = rendimentoMedioQuarter.filter(regex='T4$|Sigla').copy()
txDesemprego = txDesemprego.drop(columns=['2012 T4', '2021 T4', '2020 T4'])
print(txDesemprego)
empregados = {
    'Estado': empregadosMes['Sigla'],
    #'2012': empregadosMes.filter(regex='^2012').sum(axis=1),
    '2013': empregadosMes.filter(regex='^2013').sum(axis=1),
    '2014': empregadosMes.filter(regex='^2014').sum(axis=1),
    '2015': empregadosMes.filter(regex='^2015').sum(axis=1),
    '2016': empregadosMes.filter(regex='^2016').sum(axis=1),
    '2017': empregadosMes.filter(regex='^2017').sum(axis=1),
    '2018': empregadosMes.filter(regex='^2018').sum(axis=1),
    '2019': empregadosMes.filter(regex='^2019').sum(axis=1),
}
demissoes = {
    'Estado': demissoesMes['Sigla'],
    #'2012': demissoesMes.filter(regex='^2012').sum(axis=1),
    '2013': demissoesMes.filter(regex='^2013').sum(axis=1),
    '2014': demissoesMes.filter(regex='^2014').sum(axis=1),
    '2015': demissoesMes.filter(regex='^2015').sum(axis=1),
    '2016': demissoesMes.filter(regex='^2016').sum(axis=1),
    '2017': demissoesMes.filter(regex='^2017').sum(axis=1),
    '2018': demissoesMes.filter(regex='^2018').sum(axis=1),
    '2019': demissoesMes.filter(regex='^2019').sum(axis=1),
}

txDesempregoBrAno = {
    '2013': flatten(desempregoBrQuarter.filter(regex='2013').values.tolist()),
    '2014': flatten(desempregoBrQuarter.filter(regex='2014').values.tolist()),
    '2015': flatten(desempregoBrQuarter.filter(regex='2015').values.tolist()),
    '2016': flatten(desempregoBrQuarter.filter(regex='2016').values.tolist()),
    '2017': flatten(desempregoBrQuarter.filter(regex='2017').values.tolist()),
    '2018': flatten(desempregoBrQuarter.filter(regex='2018').values.tolist()),
    '2019': flatten(desempregoBrQuarter.filter(regex='2019').values.tolist()),
}


txDesemprego.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
rendimentoMedio.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
empregadosDf = pd.DataFrame(empregados).set_index('Estado')
demissoesDf = pd.DataFrame(demissoes).set_index('Estado')
txDesempregoBrAnoDf = pd.DataFrame(txDesempregoBrAno)
txDesemprego.set_index('Sigla', inplace=True)
rendimentoMedio.set_index('Sigla',inplace=True)

empregadosDf = empregadosDf.T
demissoesDf = demissoesDf.T
txDesemprego = txDesemprego.T
rendimentoMedio = rendimentoMedio.T

empregadosTotais = empregadosDf.T.sum(axis=0)
demissoesTotais = demissoesDf.T.sum(axis=0)

#CONTRATADOS NO ANO LINE CHART
#ano = 2016
#pos = 0
#for estado in empregadosDf.columns:
#    if estado != 'MG':
#        continue
#    plt.plot(empregadosDf.index, empregadosDf[estado], label=estado)
#    plt.annotate(estado, xy=(3, empregadosDf[estado][str(ano)]), xytext=(3, empregadosDf[estado][str(ano)] + 50000))
#plt.title('Pessoas contratadas no Ano(formal/informal)')
#plt.ylabel('Pessoas(Milhao)')
#plt.xlabel('Ano')
#plt.legend(title="Estado")

#CONTRATADOS NO ANO BAR CHART
#plt.bar(empregadosTotais.index, empregadosTotais.values)
#plt.title("Pessoas Contratadas no Ano / Nacional")
#plt.xlabel("Ano")
#plt.ylabel("Nro. de Pessoas(Dez. Milhoes)")

#Calcular diferenca entra contratados e demitidos

#DEMISSOES NO ANO LINECHART
#ano = 2016
#pos = 0
#for estado in demissoesDf.columns:
#    plt.plot(demissoesDf.index, demissoesDf[estado], label=estado)
#    if demissoesDf[estado][str(ano)] < 1000000:
#        continue
#    plt.annotate(estado, xy=(3, demissoesDf[estado][str(ano)]), xytext=(3, demissoesDf[estado][str(ano)] + 50000))
#plt.title('Pessoas demitidas no Ano(formal/informal)')
#plt.ylabel('Pessoas(Milhao)')
#plt.xlabel('Ano')
#plt.legend(title="Estado")

#DEMISSOES NO ANO BAR CHART
#plt.bar(demissoesTotais.index, demissoesTotais.values)
#plt.title("Demissoes no Ano / Nacional")
#plt.xlabel("Ano")
#plt.ylabel("Nro. Pessoas(Dez. Milhoes)")

#TAXA DESEMPREGO LINE CHART
ano = 2016
pos = 0
for estado in txDesemprego.columns:
    plt.plot(txDesemprego.index, txDesemprego[estado], label=estado)
    if estado != 'SP':
        continue
    plt.annotate(estado, xy=(4, txDesemprego[estado][str(ano)]), xytext=(4, txDesemprego[estado][str(ano)] + 0.1))
plt.title('Grafico 16 -- Taxa de Desemprego')
plt.ylabel('Porcentagem')
plt.xlabel('Ano')
plt.legend(title="Estado")
plt.show()

#TAXA DESEMPREGO BOXPLOT
#plt.boxplot(txDesempregoBrAnoDf)
#plt.title('Taxa de Desemprego Nacional')
#plt.xlabel('Ano')
#plt.ylabel('Porcentagem')
#plt.xticks(np.arange(8), ['', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])

#RENDIMENTO MEDIO LINE CHART
#ano = 2016
#pos = 0
#for estado in rendimentoMedio.columns:
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.plot(rendimentoMedio.index, rendimentoMedio[estado], label=estado)
#    plt.annotate(estado, xy=(4, rendimentoMedio[estado][str(ano)]), xytext=(4, rendimentoMedio[estado][str(ano)] + 10))
#plt.title('Rendimento medio em R$')
#plt.ylabel('R$')
#plt.xlabel('Ano')
#plt.legend(title='Estado')
#
plt.show()
#plt.savefig('contratados-estado.png')
