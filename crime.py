import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

folderPath = 'C:\\Users\\lucas\\repos\\pfDados\\crime\\'
latTx = pd.read_excel(folderPath+'lt-tx-cmil-vit.xlsx', index_col=0, header=0).T
trafTx = pd.read_excel(folderPath+'tr-tx-cmil-oc.xlsx', index_col=0, header=0).T
latAb = pd.read_excel(folderPath+'lt-ab-vit.xlsx', index_col=0, header=0).T
trafAb = pd.read_excel(folderPath+'tr-ab-oc.xlsx', index_col=0, header=0).T
homAb = pd.read_csv(folderPath+'homicidio2013-2019.csv', index_col=0, sep=';', header=0)

latBr = latAb.sum(axis=1)
trafBr = trafAb.sum(axis=1)

#FAZER GRAFICO DE PIZZA SOBRE TIPO DE CRIME RELACIONADO A UM BREAKPOINT DE OUTRO DADO

#TAXA LATROCINIO 100MIL HAB
#ano = 2016
#pos = 0
#for estado in latTx.columns:
#    plt.plot(latTx.index, latTx[estado], label=estado)
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.annotate(estado, xy=(2016, latTx[estado][ano]), xytext=(2016, latTx[estado][ano] + 0.05))
#plt.title('Latrocinio/Taxa por 100 mil Habitantes')
#plt.ylabel('Taxa')
#plt.xlabel('Ano')
#plt.legend(title="Estado")

#LATROCINIO ABSOLUTO
#ano = 2016
#pos = 0
#for estado in latAb.columns:
#    plt.plot(latAb.index, latAb[estado], label=estado)
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.annotate(estado, xy=(2016, latAb[estado][ano]), xytext=(2016, latAb[estado][ano] + 0.05))
#plt.title('Latrocinio/Numeros Absolutos')
#plt.ylabel('Nro.')
#plt.xlabel('Ano')
#plt.legend(title="Estado")

#LATROCINIO BR TOTAL
#plt.bar(latBr.index, latBr.values)
#plt.title('Latrocinios/Nacional')
#plt.ylabel('Nro.')
#plt.xlabel('Ano')

#TRAFICO ABSOLUTO
#ano = 2016
#pos = 0
#for estado in trafAb.columns:
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.plot(trafAb.index, trafAb[estado], label=estado)
#    plt.annotate(estado, xy=(2016, trafAb[estado][ano]), xytext=(2016, trafAb[estado][ano] + 0.05))
#plt.title('Trafico de Drogas/Numeros Absolutos')
#plt.ylabel('Nro.')
#plt.xlabel('Ano')
#plt.legend(title="Estado")

#TRAFICO BR TOTAL
#plt.bar(trafBr.index, trafBr.values)
#plt.title('Trafico/Nacional')
#plt.ylabel('Nro.')
#plt.xlabel('Ano')

#TRAFICO TAXA
#ano = 2016
#pos = 0
#for estado in trafTx.columns:
#    if estado != 'SP' and estado != 'MG' and estado != 'RJ' and estado != 'PR' and estado != 'RS':
#        continue
#    plt.plot(trafTx.index, trafTx[estado], label=estado)
#    plt.annotate(estado, xy=(2016, trafTx[estado][ano]), xytext=(2016, trafTx[estado][ano] + 0.05))
#plt.title('Trafico de Drogas/Taxa por 100Mil Habitantes')
#plt.ylabel('Taxa')
#plt.xlabel('Ano')
#plt.legend(title="Estado")

#plt.show()

#MEDIAS CRIME BR/ANO
mediaLat = latAb.T.mean()
mediaLatTx = latTx.T.mean()
varLatTx = latTx.T.var()
desvioLatTx = latTx.T.std()

mediaHom = homAb.mean()

mediaTraf = trafAb.T.mean()
mediaTrafTx = trafTx.T.mean()
varTrafTx = trafTx.T.var()
desvioTrafTx = trafTx.T.std()
