import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

folderPath = 'C:\\Users\\lucas\\repos\\pfDados\\'
def flatten(lista):
    return [item for sublist in lista  for item in sublist]

#LATROCINIO / DESEMPREGO
#homicidios_data = pd.read_excel(folderPath+'crime\\lt-tx-cmil-vit.xlsx', index_col=0)
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
#for uf in homicidios_data.index:
#    x = homicidios_data.loc[uf].values
#    y = txDesemprego_data.loc[uf].values
#    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.xlabel('Número de Latrocinios')
#plt.ylabel('Taxa de Desemprego')
#plt.title('Relação entre Latrocinio e Taxa de Desemprego(por Estado)')
#
#plt.legend()
#plt.grid(True)
#plt.show()

#HOMICIDIO / DESEMPREGO
#homicidios_data = pd.read_csv(folderPath+'crime\\homicidio2013-2019.csv', index_col=0, sep=';')
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
#for uf in homicidios_data.index:
#    x = homicidios_data.loc[uf].values
#    y = txDesemprego_data.loc[uf].values
#    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.xlabel('Número de Homicidios')
#plt.ylabel('Taxa de Desemprego')
#plt.title('Relação entre Homicidios e Taxa de Desemprego(por Estado)')
#
#plt.legend()
#plt.grid(True)
#plt.show()

#TRAFICO / DESEMPREGO
#homicidios_data = pd.read_excel(folderPath+'crime\\tr-tx-cmil-oc.xlsx', index_col=0)
#print(homicidios_data)
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
#for uf in homicidios_data.index:
#    y = homicidios_data.loc[uf].values
#    x = txDesemprego_data.loc[uf].values
#    correlacao_pearson = pd.Series(x).corr(pd.Series(y))
#    sns.scatterplot(x=x, y=y, label=f'{uf} - Corr: {correlacao_pearson:.2f}')
#
#plt.ylabel('Taxa de Homicidios')
#plt.xlabel('Taxa de Desemprego')
#plt.title('Relação entre Taxa de Homicidios e Taxa de Desemprego(por Estado)')
#
#plt.legend()
#plt.grid(True)
#plt.show()