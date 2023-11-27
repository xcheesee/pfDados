
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\'
def flatten(lista):
    return [item for sublist in lista  for item in sublist]

#LATROCINIO / Ens.Medio
latrocinio_data = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)

medioCursand = pd.read_csv(folderPath+'estudo\\15-17medio.csv', sep=";", index_col=0, header=1, decimal=',')
medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)

plt.figure(figsize=(12, 8))
a = ""
b = ""
pltTitle = []
for uf in latrocinio_data.index:
    x = medioCursand.loc[uf].values
    y = latrocinio_data.loc[uf].values
    if uf == 'SP':
        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
        a, b = np.polyfit(x, y, 1)
        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2:.2f}")
        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
        sns.regplot(x=x, y=y)

plt.ylabel('Taxa de Latrocinios')
plt.xlabel('Porcentagem de Jovens no Ensino Medio')
plt.suptitle('Grafico 19 -- Relação entre Latrocinio e Taxa de Jovens no Ensino Medio(por Estado)')
plt.title('\n'.join(pltTitle))

plt.legend()
plt.grid(True)
plt.show()

#Latrocinio / 6-14 Escola
traficoData = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)

medioCursand = pd.read_csv(folderPath+'estudo\\6-14escola.csv', sep=";", index_col=0, header=1, decimal=',')
medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)

plt.figure(figsize=(12, 8))

a = ""
b = ""
pltTitle = []
for uf in traficoData.index:
    x = medioCursand.loc[uf].values
    y = traficoData.loc[uf].values
    if uf == 'SP':
        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
        a, b = np.polyfit(x, y, 1)
        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2:.2f}")
        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
        sns.regplot(x=x, y=y)

plt.ylabel('Taxa de Latrocinio')
plt.xlabel('Porcentagem de Criancas 6-14 na escola')
plt.suptitle('Grafico 18 -- Relação entre Taxa de Latrocinio e Porcentagem de Criancas 6-14 na escola(por Estado)')
plt.title('\n'.join(pltTitle))

plt.legend()
plt.grid(True)
plt.show()

#Trafico / Ens.Medio
#traficoData = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#
#medioCursand = pd.read_csv(folderPath+'estudo\\15-17medio.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in traficoData.index:
#    x = medioCursand.loc[uf].values
#    y = traficoData.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2:.2f}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.ylabel('Taxa de Trafico')
#plt.xlabel('Porcentagem de Jovens no Ensino Medio')
#plt.suptitle('Grafico 6 -- Relação entre Taxa de Trafico e Porcentagem de Jovens no Ensino Medio(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#Trafico / 6-14 Escola
#traficoData = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#
#medioCursand = pd.read_csv(folderPath+'estudo\\6-14escola.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in traficoData.index:
#    x = medioCursand.loc[uf].values
#    y = traficoData.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2:.2f}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.ylabel('Taxa de Trafico')
#plt.xlabel('Porcentagem de Criancas 6-14 na escola')
#plt.suptitle('Grafico 5 -- Relação entre Taxa de Trafico e Porcentagem de Criancas 6-14 na escola(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#HOMICIDIO / Ens. Medio
#homTx = pd.read_csv(folderPath+'crime\\hom-tx-cmil-oc.csv', sep=';', index_col=0, header=1, decimal=',').T
#homTx = homTx.drop(['Estado', 'Código', 'Unnamed: 10'])
#
#medioCursand = pd.read_csv(folderPath+'estudo\\15-17medio.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#homicidios_data = homTx.T
#txDesemprego_data = medioCursand
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in homicidios_data.index:
#    x = homicidios_data.loc[uf].values.astype(float)
#    y = txDesemprego_data.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.xlabel('Taxa de Homicidios')
#plt.ylabel('Porcentagem de Jovens no Ensino Medio')
#plt.suptitle('Relação entre Homicidios e Porcentagem de Jovens no Ensino Medio (por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#HOMICIDIO / 6-14 escola
#homTx = pd.read_csv(folderPath+'crime\\hom-tx-cmil-oc.csv', sep=';', index_col=0, header=1, decimal=',').T
#homTx = homTx.drop(['Estado', 'Código', 'Unnamed: 10'])
#
#medioCursand = pd.read_csv(folderPath+'estudo\\6-14escola.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#homicidios_data = homTx.T
#txDesemprego_data = medioCursand
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in homicidios_data.index:
#    x = homicidios_data.loc[uf].values.astype(float)
#    y = txDesemprego_data.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.xlabel('Taxa de Homicidios')
#plt.ylabel('Porcentagem de Criancas na Escola')
#plt.suptitle('Relação entre Homicidios e Porcentagem de Criancas na Escola (por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()