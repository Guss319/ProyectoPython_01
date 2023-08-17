import pandas as pd #libreria para la manipulacion de datos
import GraficosParte_02 as gf


datos=pd.read_excel("Datos.xlsx", header=0)
#print(datos['Au_ppm'])
Xsample=[]
Ymedia=[]
elemento2="Au_ppm"

Nmuestras=datos["N°Samples"]
media=datos["Au_ppm_Mean"]
# 1° Desvio
desv1U=datos["Au_ppm_1SD_Up"]
desv1D=datos["Au_ppm_1SD_Down"]
# 2° Desvio
desv2U=datos["Au_ppm_2SD_Up"]
desv2D=datos["Au_ppm_2SD_Down"]
# 3° Desvio
desv3U=datos["Au_ppm_3SD_Up"]
desv3D=datos["Au_ppm_3SD_Down"]
# valores de oro
elemento=datos["Au_ppm"]
# numero de muestra
etiquetas=datos["Sample"]

gf.fnHacerGraficos(elemento,elemento2,Nmuestras, media,desv1U,desv1D,desv2U,desv2D,desv3U,desv3D,etiquetas)