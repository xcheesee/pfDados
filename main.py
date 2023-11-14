import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

#dados 2012-2019
folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\emprego\\'
txDesempregoQuarter = pd.read_csv(folderPath+'taxaDesemprego2012-2021.csv', sep=";", decimal=',')
empregadosMes = pd.read_csv(folderPath+'empregados2012-2019.csv', sep=";")
demissoesMes = pd.read_csv(folderPath+'demissoes2012-2019.csv', sep=";")
rendimentoMedioQuarter = pd.read_csv(folderPath+'rendimentoMedio2012-2021.csv', sep=";")
txDesemprego = txDesempregoQuarter.filter(regex='T4$|Sigla').copy()
rendimentoMedio = rendimentoMedioQuarter.filter(regex='T4$|Sigla').copy()
empregados = {
    'Estado': empregadosMes['Sigla'],
    '2012': empregadosMes.filter(regex='^2012').sum(axis=1),
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
    '2012': demissoesMes.filter(regex='^2012').sum(axis=1),
    '2013': demissoesMes.filter(regex='^2013').sum(axis=1),
    '2014': demissoesMes.filter(regex='^2014').sum(axis=1),
    '2015': demissoesMes.filter(regex='^2015').sum(axis=1),
    '2016': demissoesMes.filter(regex='^2016').sum(axis=1),
    '2017': demissoesMes.filter(regex='^2017').sum(axis=1),
    '2018': demissoesMes.filter(regex='^2018').sum(axis=1),
    '2019': demissoesMes.filter(regex='^2019').sum(axis=1),
}


txDesemprego.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
rendimentoMedio.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
empregadosDf = pd.DataFrame(empregados).set_index('Estado')
demissoesDf = pd.DataFrame(demissoes).set_index('Estado')
txDesemprego.set_index('Sigla', inplace=True)
rendimentoMedio.set_index('Sigla',inplace=True)

empregadosDf = empregadosDf.T
demissoesDf = demissoesDf.T
txDesemprego = txDesemprego.T
rendimentoMedio = rendimentoMedio.T



#for estado in empregadosDf.columns:
#    plt.plot(empregadosDf.index, empregadosDf[estado], label=estado)
#plt.title('Pessoas contratadas no Ano(formal/informal)')
#plt.ylabel('Pessoas(Milhao)')
#plt.xlabel('Ano')

#Calcular diferenca entra contratados e demitidos

#for estado in demissoesDf.columns:
#    plt.plot(demissoesDf.index, demissoesDf[estado], label=estado)
#plt.title('Pessoas demitidas no Ano(formal/informal)')
#plt.ylabel('Pessoas(Milhao)')
#plt.xlabel('Ano')
empregadosTotais = empregadosDf.T.sum(axis=0)
#for estado in txDesemprego.columns:
#    plt.plot(txDesemprego.index, txDesemprego[estado], label=estado)
#plt.title('Taxa de Desemprego')
#plt.ylabel('Porcentagem')
#plt.xlabel('Ano')
print(empregadosTotais)

#for estado in rendimentoMedio.columns:
#    plt.plot(rendimentoMedio.index, rendimentoMedio[estado], label=estado)
#plt.title('Rendimento medio em R$')
#plt.ylabel('R$')
#plt.xlabel('Ano')
#plt.legend(title='Estado')
#print(rendimentoMedio)


plt.show()