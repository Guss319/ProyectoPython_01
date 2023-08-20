import pandas as pd 
import Datos as dt
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image


def obtener_valor_seleccionado():
    elemento = variable.get()
    parametros=desvio[elemento]
    dt.SeleccionarDatos(elemento,parametros[0],parametros[1],parametros[2],parametros[3],parametros[4],parametros[5],parametros[6])

def buscarArchivo():
    global archivo, desvio
    archivo = filedialog.askopenfilename() # Guarda el contenido del cuadro de texto en la variable
    desvio=pd.read_excel(archivo,sheet_name="Desvios", header=0)
#cabeza=["Seleccione un elemento"]
    cabeza=desvio.columns


    etiqueta=Label(ventana,text="Seleccione un elemento:")
    etiqueta.config(width=40,height=1)
    etiqueta.place(x=20,y=133)
# se crea el combobox o lista desplegable
    cbElementos = OptionMenu(ventana, variable, *cabeza)
    cbElementos.config(width=12,height=1)
    cbElementos.place(x=330,y=130)

# se crea el boton graficar
    btnGraficar = tk.Button(ventana, text="GRAFICAR", command=obtener_valor_seleccionado)
    btnGraficar.config(width=15,height=1)
    btnGraficar.place(x=480,y=133)




ventana=Tk()
ventana.title('Control de calidad')
fondo=ImageTk.PhotoImage(Image.open('Altar_01.jpg'))
etiqueta=Label(image=fondo)
etiqueta.pack()
ventana.iconbitmap('Grafico.ico')
#se crea una variable para almacenar el valor seleccionado
variable = tk.StringVar(ventana)

etiquita=Label(ventana,text="Presione buscar para seleccionar el archivo de datos: ")
etiquita.place(x=20,y=38)
btnBuscar = tk.Button(ventana, text="BUSCAR", command=buscarArchivo)
btnBuscar.config(width=15,height=1)
btnBuscar.place(x=330,y=35)






 # se lee desde el excel la hoja desvios con los elementos a graficar






ventana.mainloop()