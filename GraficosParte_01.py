import pandas as pd
import matplotlib.pyplot as plt

#tamaño del grafico
plt.figure(figsize=(20,8))

datos=pd.read_excel("Datos.xlsx", header=0)
#print(datos['Au_ppm'])
Xsample=[]
Ymedia=[]
Xsample=datos['N°Samples']
Ymedia=datos["Au_ppm_Mean"]
# 1° Desvio
y1DesvioU=datos["Au_ppm_1SD_Up"]
y1DesvioD=datos["Au_ppm_1SD_Down"]
# 2° Desvio
y2DesvioU=datos["Au_ppm_2SD_Up"]
y2DesvioD=datos["Au_ppm_2SD_Down"]
# 3° Desvio
y3DesvioU=datos["Au_ppm_3SD_Up"]
y3DesvioD=datos["Au_ppm_3SD_Down"]
# valores de oro
Au=datos["Au_ppm"]
# numero de muestra
lblAu=datos["Sample"]



# Grafica de las lineas de control
plt.plot(Xsample, Ymedia, color='g')
# primer desvio
plt.plot(Xsample, y1DesvioU, color='b')
plt.plot(Xsample, y1DesvioD , color='b')
#segundo desvio
plt.plot(Xsample, y2DesvioU, color='m')
plt.plot(Xsample, y2DesvioD , color='m')
# tercer desvio
plt.plot(Xsample, y3DesvioU, color='r')
plt.plot(Xsample, y3DesvioD , color='r')
# grafico de datos
plt.plot(Xsample, Au , color='k',marker='.')
# etiquetas

for i, label in enumerate(lblAu):
    plt.annotate(label, (Xsample[i] + 0.1, Au[i]),rotation=90)

plt.show()
