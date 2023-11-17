import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

folderPath = 'C:\\Users\\x529427\\Documents\\Repos\\pfDados\\indicadores\\'
ivs = pd.read_excel(folderPath+'ivs-estados2013-2019.xlsx', index_col=0)
ivsBr = pd.read_excel(folderPath+'ivs-br2013-2019.xlsx')
print(ivsBr)


#IVS RENDA
#ano = 2016
#pos = 0
#for estado in ivs.index.drop_duplicates():
#    plt.plot(ivs.loc[estado]['ano'], ivs.loc[estado]['renda'], label=estado)
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.annotate(estado, xy=(2016, ivs.loc[estado]['renda'][3]), xytext=(2016, ivs.loc[estado]['renda'][3] + 0.001))
#plt.title('Indice de Vulnerabilidade/Renda')
#plt.ylabel('Indice')
#plt.xlabel('Ano')
#plt.legend(title="Estado")
#
#
plt.bar(ivsBr['ano'], ivsBr['renda'])
plt.title('Indice de Vulnerabilidade/Renda')
plt.ylabel('Indice')
plt.xlabel('Ano')
plt.show()