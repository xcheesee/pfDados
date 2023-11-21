
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\'
def flatten(lista):
    return [item for sublist in lista  for item in sublist]

#LATROCINIO / Ens.Medio
#latrocinio_data = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)
#
#medioCursand = pd.read_csv(folderPath+'estudo\\fundComp.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#plt.figure(figsize=(12, 8))
#
#for uf in latrocinio_data.index:
#    x = medioCursand.loc[uf].values
#    y = latrocinio_data.loc[uf].values
#    if uf == 'PA' or uf == 'RR':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.ylabel('Taxa de Latrocinios')
#plt.xlabel('Porcentagem de Jovens no Ensino Medio')
#plt.title('Relação entre Latrocinio e Taxa de Jovens no Ensino Medio(por Estado)')
#
#plt.legend()
#plt.grid(True)
#plt.show()

#HOMICIDIO / Ens.Medio
#homicidio_data = pd.read_csv(folderPath+'crime\\homicidio2013-2019.csv', index_col=0, sep=';')
#
#medioCursand = pd.read_csv(folderPath+'estudo\\fundComp.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#plt.figure(figsize=(12, 8))
#
#for uf in homicidio_data.index:
#    x = medioCursand.loc[uf].values
#    y = homicidio_data.loc[uf].values
#    #if uf == 'SP':
#    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.ylabel('Numero de Homicidios')
#plt.xlabel('Porcentagem de Jovens no Ensino Medio')
#plt.title('Relação entre Homicidios e Taxa de Jovens no Ensino Medio(por Estado)')
#
#plt.legend()
#plt.grid(True)
#plt.show()

#Trafico / Ens.Medio
#traficoData = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#
#medioCursand = pd.read_csv(folderPath+'estudo\\fundComp.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#plt.figure(figsize=(12, 8))
#
#for uf in traficoData.index:
#    x = medioCursand.loc[uf].values
#    y = traficoData.loc[uf].values
#    if uf == 'ES' or uf == 'MG':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.ylabel('Taxa de Trafico')
#plt.xlabel('Porcentagem de Jovens no Ensino Medio')
#plt.title('Relação entre Taxa de Trafico e Porcentagem de Jovens no Ensino Medio(por Estado)')
#
#plt.legend()
#plt.grid(True)
#plt.show()

#HOMICIDIO / Ens. Medio
homTx = pd.read_csv(folderPath+'crime\\hom-tx-cmil-oc.csv', sep=';', index_col=0, header=1, decimal=',').T
homTx = homTx.drop(['Estado', 'Código', 'Unnamed: 10'])

medioCursand = pd.read_csv(folderPath+'estudo\\fundComp.csv', sep=";", index_col=0, header=1, decimal=',')
medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)

homicidios_data = homTx.T
txDesemprego_data = medioCursand

plt.figure(figsize=(12, 8))

for uf in homicidios_data.index:
    x = homicidios_data.loc[uf].values
    y = txDesemprego_data.loc[uf].values
    if uf == 'SP':
        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
        sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')

plt.xlabel('Taxa de Homicidios')
plt.ylabel('Porcentagem de Jovens no Ensino Medio')
plt.title('Relação entre Homicidios e Porcentagem de Jovens no Ensino Medio (por Estado)')

plt.legend()
plt.grid(True)
plt.show()