import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\'
def flatten(lista):
    return [item for sublist in lista  for item in sublist]

#LATROCINIO / DESEMPREGO
homicidios_data = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)

txDesempregoQuarter = pd.read_csv(folderPath+'emprego\\taxaDesemprego2012-2021.csv', sep=";", decimal=',', index_col=0)
txDesemprego = txDesempregoQuarter.filter(regex='T4$|Sigla').copy()
txDesemprego.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
txDesemprego = txDesemprego.drop(['2020 T4','2021 T4', '2012'], axis=1)

anos_intersecao = homicidios_data.columns.intersection(txDesemprego.columns)

homicidios_data = homicidios_data
txDesemprego_data = txDesemprego

plt.figure(figsize=(12, 8))

a = ""
b = ""
pltTitle = []
for uf in homicidios_data.index:
    x = homicidios_data.loc[uf].values
    y = txDesemprego_data.loc[uf].values
    if uf == 'SP':
        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
        a, b = np.polyfit(x, y, 1)
        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
        sns.regplot(x=x, y=y)

plt.xlabel('Taxa de Latrocinios')
plt.ylabel('Taxa de Desemprego')
plt.suptitle('Relação entre Latrocinio e Taxa de Desemprego(por Estado)')
plt.title('\n'.join(pltTitle))

plt.legend()
plt.grid(True)
plt.show()

#HOMICIDIO / DESEMPREGO
#homTx = pd.read_csv(folderPath+'crime\\hom-tx-cmil-oc.csv', sep=';', index_col=0, header=1, decimal=',').T
#homTx = homTx.drop(['Estado', 'Código', 'Unnamed: 10'])
#
#txDesempregoQuarter = pd.read_csv(folderPath+'emprego\\taxaDesemprego2012-2021.csv', sep=";", decimal=',', index_col=0)
#txDesemprego = txDesempregoQuarter.filter(regex='T4$|Sigla').copy()
#txDesemprego.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
#txDesemprego = txDesemprego.drop(['2020 T4','2021 T4', '2012'], axis=1)
#
#anos_intersecao = homTx.columns.intersection(txDesemprego.columns)
#
#homicidios_data = homTx.T
#txDesemprego_data = txDesemprego
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in homicidios_data.index:
#    x = homicidios_data.loc[uf].values.astype(float)
#    y = txDesemprego_data.loc[uf].values.astype(float)
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.xlabel('Taxa de Homicidios')
#plt.ylabel('Taxa de Desemprego')
#plt.suptitle('Relação entre Homicidios e Taxa de Desemprego(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#TRAFICO / DESEMPREGO
#homicidios_data = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#
#txDesempregoQuarter = pd.read_csv(folderPath+'emprego\\taxaDesemprego2012-2021.csv', sep=";", decimal=',', index_col=0)
#txDesemprego = txDesempregoQuarter.filter(regex='T4$|Sigla').copy()
#txDesemprego.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
#txDesemprego = txDesemprego.drop(['2020 T4','2021 T4', '2012'], axis=1)
#
#anos_intersecao = homicidios_data.columns.intersection(txDesemprego.columns)
#
#homicidios_data = homicidios_data
#txDesemprego_data = txDesemprego
#
#plt.figure(figsize=(12, 8))
#
#a = ""
#b = ""
#pltTitle = []
#for uf in homicidios_data.index:
#    y = homicidios_data.loc[uf].values.astype(float)
#    x = txDesemprego_data.loc[uf].values
#    if uf == 'MG' or uf == 'ES':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#        a, b = np.polyfit(x, y, 1)
#        pltTitle.append(f"{uf}: " + "y=%.2fx+%.2f "%(a,b) + f"R²={correlacao_pearson**2}")
#        plt.scatter(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#        sns.regplot(x=x, y=y)
#
#plt.ylabel('Taxa de Trafico de Drogas/Ocorrencias por 100mil Hab.')
#plt.xlabel('Taxa de Desemprego')
#plt.suptitle('Relação entre Taxa de Trafico de Drogas e Desemprego(por Estado)')
#plt.title('\n'.join(pltTitle))
#
#plt.legend()
#plt.grid(True)
#plt.show()

#PAIA
#traficoData = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#latData = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)
#
#txDesempregoQuarter = pd.read_csv(folderPath+'emprego\\taxaDesemprego2012-2021.csv', sep=";", decimal=',', index_col=0)
#txDesemprego = txDesempregoQuarter.filter(regex='T4$|Sigla').copy()
#txDesemprego.rename(columns={"2012 T4":'2012', "2013 T4":'2013', "2014 T4":'2014', "2015 T4":'2015', "2016 T4":'2016', "2017 T4":'2017', '2018 T4': '2018', '2019 T4': '2019'}, inplace=True)
#txDesemprego = txDesemprego.drop(['2020 T4','2021 T4', '2012'], axis=1)
#
#medioCursand = pd.read_csv(folderPath+'estudo\\fundComp.csv', sep=";", index_col=0, header=1, decimal=',')
#medioCursand = medioCursand.drop(['Estado', 'Código', '2012', '2020', '2021', 'Unnamed: 13'], axis=1)
#
#
#for uf in traficoData.index:
#    x = traficoData.loc[uf].values
#    s = txDesemprego.loc[uf].values
#    y = latData.loc[uf].values
#    if uf == 'SP':
#        correlacao_pearson = pd.Series(x).corr(pd.Series(s))
#        plt.scatter(x=x, y=y, label=f'{uf}: Corr - {correlacao_pearson}', s=s*10)
#
#plt.show()