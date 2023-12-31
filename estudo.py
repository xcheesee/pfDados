import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\estudo\\'

#15-17 Medio
percentual01 = pd.read_csv(folderPath+'15-17medio.csv' , sep=";" , header=1, index_col=0, decimal=",").T
percentual01 = percentual01.drop(['Estado', 'Código', '2012', '2020', '2021'])

ano = 2016
pos = 0
for estado in percentual01.columns:
    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS' and estado != 'PA' and estado != 'RR':
        continue
    plt.plot(percentual01.index, percentual01[estado], label=estado)
    plt.annotate(estado, xy=(3, percentual01[estado][str(ano)]), xytext=(3, percentual01[estado][str(ano)]))
plt.title('Grafico 21 -- Pessoas 15 a 17 anos na Escola\Percentual')
plt.ylabel('Indice')
plt.xlabel('Ano')
plt.legend(title='Estado')

plt.show()

#6-14 Escola
#percentual02 = pd.read_csv(folderPath+'6-14escola.csv' , sep=";", header=1, index_col=0, decimal=",").T
#percentual02 = percentual02.drop(['Estado', 'Código', '2012', '2020', '2021'])
#
#ano = 2016
#pos = 0
#for estado in percentual02.columns:
#    if (estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS' and estado != 'RR' and estado != 'PA'):
#        continue
#    plt.plot(percentual02.index, percentual02[estado], label=estado)
#    plt.annotate(estado, xy=(3, percentual02[estado][str(ano)]), xytext=(3, percentual02[estado][str(ano)]))
#plt.title('Grafico 20 -- Pessoas 6 a 14 anos na Escola\Percentual')
#plt.ylabel('Indice')
#plt.xlabel('Ano')
#plt.legend(title='Estado')
#
#plt.show()

#18-24funcomp
#percentual03 = pd.read_csv(folderPath+'fundComp.csv' , sep=";", header=1, index_col=0, decimal=",").T
#percentual03 = percentual03.drop(['Estado', 'Código', '2012', '2020', '2021'])
#
#ano = 2016
#pos = 0
#for estado in percentual03.columns:
#    plt.plot(percentual03.index, percentual03[estado], label=estado)
#    if (estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS'):
#        continue
#    plt.annotate(estado, xy=(3, percentual03[estado][str(ano)]), xytext=(3, percentual03[estado][str(ano)]))
#plt.title('18 a 24 Fundamental Completo/Porcentagem')
#plt.ylabel('Indice')
#plt.xlabel('Ano')
#plt.legend(title='Estado')
#
#plt.show()

#FreqSup
txFreqEnsinoSuperior = pd.read_csv(folderPath+'taxaFreqEnsinoSuperior2012-2021.csv' , sep=";", header=1, index_col=0, decimal=",").T
txFreqEnsinoSuperior = txFreqEnsinoSuperior.drop(['Estado', 'Código', '2012', '2020', '2021'])

ano = 2016
pos = 0
for estado in txFreqEnsinoSuperior.columns:
    plt.plot(txFreqEnsinoSuperior.index, txFreqEnsinoSuperior[estado], label=estado)
    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
        continue
    plt.annotate(estado, xy=(3, txFreqEnsinoSuperior[estado][str(ano)]), xytext=(3, txFreqEnsinoSuperior[estado][str(ano)]))
plt.title('Taxa de Frequencia Ensino Superior/Porcentagem')
plt.ylabel('Indice')
plt.xlabel('Ano')
plt.legend(title='Estado')

plt.show()