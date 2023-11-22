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

bolsaPessoas = pd.read_csv(folderPath+'bolsa\\bolsaPess.csv', sep=";", index_col=0, header=1, decimal=',')
bolsaPessoas = bolsaPessoas.drop(['Estado', 'Código', '2012'], axis=1)

#LATROCINIO / Valor Bolsa
#latrocinio_data = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)
#
#
#plt.figure(figsize=(12, 8))
#a = ""
#b = ""
#pltTitle = []
#for uf in latrocinio_data.index:
#    x = bolsa.loc[uf].values
#    y = latrocinio_data.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.ylabel('Taxa de Latrocinios')
#plt.xlabel('Verba Gasta em Bolsa Familia')
#plt.suptitle('Relação entre Latrocinio e Verba Gasta em Bolsa Familia(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#Latrocinio / Bolsa Pessoas
#traficoData = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in traficoData.index:
#    x = bolsaPessoas.loc[uf].values
#    y = traficoData.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.ylabel('Taxa de Latrocinio')
#plt.xlabel('Numero de Pessoas Beneficiadas pelo Bolsa Familia')
#plt.suptitle('Relação entre Taxa de Latrocinio e Numero de Pessoas Beneficiadas pelo Bolsa Familia(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#Trafico / Valor Bolsa
#traficoData = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in traficoData.index:
#    x = bolsa.loc[uf].values
#    y = traficoData.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.ylabel('Taxa de Trafico')
#plt.xlabel('Verba Gasta em Bolsa Familia')
#plt.suptitle('Relação entre Taxa de Trafico e Verba Gasta em Bolsa Familia(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#Trafico / Bolsa Pessoa
#traficoData = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in traficoData.index:
#    x = bolsaPessoas.loc[uf].values
#    y = traficoData.loc[uf].values
#    if uf == 'MG' or uf == 'ES':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.ylabel('Taxa de Trafico')
#plt.xlabel('Numero de Pessoas Beneficiadas pelo Bolsa Familia')
#plt.suptitle('Relação entre Taxa de Trafico e Numero de Pessoas Beneficiadas pelo Bolsa Familia(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#HOMICIDIO / Bolsa Valores
#homTx = pd.read_csv(folderPath+'crime\\hom-tx-cmil-oc.csv', sep=';', index_col=0, header=1, decimal=',').T
#homTx = homTx.drop(['Estado', 'Código', 'Unnamed: 10'])
#
#homicidios_data = homTx.T
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in homicidios_data.index:
#    x = homicidios_data.loc[uf].values.astype(float)
#    y = bolsa.loc[uf].values
#    if uf == 'RR' or uf == 'AL':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.xlabel('Taxa de Homicidios')
#plt.ylabel('Verba Gasta em Bolsa Familia')
#plt.suptitle('Relação entre Homicidios e Verba Gasta em Bolsa Familia (por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#HOMICIDIO / Bolsa Pessoas
homTx = pd.read_csv(folderPath+'crime\\hom-tx-cmil-oc.csv', sep=';', index_col=0, header=1, decimal=',').T
homTx = homTx.drop(['Estado', 'Código', 'Unnamed: 10'])

homicidios_data = homTx.T

plt.figure(figsize=(12, 8))

a = ""
b = ""
pltTitle = []
for uf in homicidios_data.index:
    x = homicidios_data.loc[uf].values.astype(float)
    y = bolsaPessoas.loc[uf].values
    if uf == 'RR' or uf == 'AL':
        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
        a, b = np.polyfit(x, y, 1)
        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
        sns.regplot(x=x, y=y)

plt.xlabel('Taxa de Homicidios')
plt.ylabel('Numero de Pessoas Beneficiadas pelo Bolsa Familia')
plt.suptitle('Relação entre Homicidios e Numero de Pessoas Beneficiadas pelo Bolsa Familia (por Estado)')
plt.title('\n'.join(pltTitle))

plt.legend()
plt.grid(True)
plt.show()