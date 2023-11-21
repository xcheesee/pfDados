
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

folderPath = 'C:\\Users\\lucas\\repos\\pfDados\\'
def flatten(lista):
    return [item for sublist in lista  for item in sublist]

#LATROCINIO / Ens.Medio
#latrocinio_data = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)
#
#medioCursand = pd.read_csv(folderPath+'estudo\\fundComp.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
##medioCursand = medioCursand.filter(regex='T4$|Sigla').copy()
##medioCursand.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
##medioCursand = medioCursand.drop(['2020 T4','2021 T4', '2012'], axis=1)
#
#plt.figure(figsize=(12, 8))
#
#for uf in latrocinio_data.index:
#    x = medioCursand.loc[uf].values
#    y = latrocinio_data.loc[uf].values
#    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.xlabel('Taxa de Latrocinios')
#plt.ylabel('Porcentagem de Jovens no Ensino Medio')
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
#    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.xlabel('Numero de Homicidios')
#plt.ylabel('Porcentagem de Jovens no Ensino Medio')
#plt.title('Relação entre Homicidios e Taxa de Jovens no Ensino Medio(por Estado)')
#
#plt.legend()
#plt.grid(True)
#plt.show()

#Trafico / Ens.Medio
traficoData = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)

medioCursand = pd.read_csv(folderPath+'estudo\\fundComp.csv', sep=";", index_col=0, header=1, decimal=',')
medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)

plt.figure(figsize=(12, 8))

for uf in traficoData.index:
    x = medioCursand.loc[uf].values
    y = traficoData.loc[uf].values
    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')

plt.xlabel('Taxa de Trafico')
plt.ylabel('Porcentagem de Jovens no Ensino Medio')
plt.title('Relação entre Homicidios e Taxa de Jovens no Ensino Medio(por Estado)')

plt.legend()
plt.grid(True)
plt.show()