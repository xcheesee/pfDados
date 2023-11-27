import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\'
def flatten(lista):
    return [item for sublist in lista  for item in sublist]

bolsaValores = pd.read_csv(folderPath+'bolsa\\bolsaValores.csv',sep=';', index_col=0, header=1, decimal=',')
bolsaValores = bolsaValores.drop(['Estado', 'Código'], axis=1)

bolsa = {
    'Estado': bolsaValores.index,
    '2013': bolsaValores.filter(regex='^2013').sum(axis=1),
    '2014': bolsaValores.filter(regex='^2014').sum(axis=1),
    '2015': bolsaValores.filter(regex='^2015').sum(axis=1),
    '2016': bolsaValores.filter(regex='^2016').sum(axis=1),
    '2017': bolsaValores.filter(regex='^2017').sum(axis=1),
    '2018': bolsaValores.filter(regex='^2018').sum(axis=1),
    '2019': bolsaValores.filter(regex='^2019').sum(axis=1),
}
bolsa = pd.DataFrame(bolsa).set_index('Estado')
bolsaTotal = bolsa.sum(axis=0)

bolsaPessoas = pd.read_csv(folderPath+'bolsa\\bolsaPess.csv', sep=";", index_col=0, header=1, decimal=',')
bolsaPessoas = bolsaPessoas.drop(['Estado', 'Código', '2012'], axis=1)
bolsaPessoasTotal = bolsaPessoas.sum(axis=0)

#VERBA BOLSA
#ano=2016
#for estado in bolsa.index:
#    plt.plot(bolsa.columns, bolsa.loc[estado], label=estado)
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.annotate(estado, xy=(3, bolsa.loc[estado][str(ano)]), xytext=(3, bolsa.loc[estado][str(ano)]))
#plt.title('Pessoas Beneficiadas pelo Bolsa Familia/Estado')
#plt.legend(title="Estado")
#plt.xlabel('Ano')
#plt.ylabel('R$(Dez.Milhao)')
#plt.show()

#PESSOAS BOLSA
#ano=2016
#for estado in bolsaPessoas.index:
#    plt.plot(bolsaPessoas.columns, bolsaPessoas.loc[estado], label=estado)
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.annotate(estado, xy=(3, bolsaPessoas.loc[estado][str(ano)]), xytext=(3, bolsaPessoas.loc[estado][str(ano)]))
#plt.title('Verba Gasta com Bolsa Familia/Estado')
#plt.legend(title="Estado")
#plt.xlabel('Ano')
#plt.ylabel('R$(Dez.Milhao)')
#plt.show()

#VERBA BOLSA BR
plt.bar(bolsaTotal.index, bolsaTotal.values)
plt.title('Grafico 14 -- Verba Gasta em Bolsa Familia/Brasil')
plt.xlabel('Ano')
plt.ylabel('R$(Dez.Milhoes)')
plt.show()

#PESSOAS BOLSA BR
plt.bar(bolsaPessoasTotal.index, bolsaPessoasTotal.values)
plt.title('Grafico 15 -- Pessoas Beneficiadas pelo Bolsa Familia/Brasil')
plt.xlabel('Ano')
plt.ylabel('Pessoas(Milhao)')
plt.show()