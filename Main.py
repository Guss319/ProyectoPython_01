import pandas as pd 
import Datos as dt
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

def obtener_valor_seleccionado():
    elemento = variable.get()
    parametros=desvio[elemento]
    dt.SeleccionarDatos(elemento,parametros[0],parametros[1],parametros[2],parametros[3],parametros[4],parametros[5],parametros[6])



ventana=Tk()
ventana.title('Control de calidad')
fondo=ImageTk.PhotoImage(Image.open('Altar_01.jpg'))
etiqueta=Label(image=fondo)
etiqueta.pack()
ventana.iconbitmap('Grafico.ico')


etiquita=Label(ventana,text="Seleccione un elemento:")
etiquita.place(x=20,y=35)

 # se lee desde el excel la hoja desvios con los elementos a graficar
desvio=pd.read_excel("Datos.xlsx",sheet_name="Desvios", header=0)
#cabeza=["Seleccione un elemento"]
cabeza=desvio.columns

#se crea una variable para almacenar el valor seleccionado
variable = tk.StringVar(ventana)

# se crea el combobox o lista desplegable
cbElementos = OptionMenu(ventana, variable, *cabeza)
cbElementos.config(width=10,height=1)
cbElementos.place(x=160,y=30)

# se crea el boton graficar
btnGraficar = tk.Button(ventana, text="Graficar", command=obtener_valor_seleccionado)
btnGraficar.place(x=280,y=33)





ventana.mainloop()
