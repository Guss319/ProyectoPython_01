import pandas as pd 
import Datos as dt
import tkinter as tk
from tkinter import OptionMenu

def obtener_valor_seleccionado():
    elemento = variable.get()
    cuadro_texto.delete(0, tk.END)  # Limpiar el cuadro de texto
    cuadro_texto.insert(0, elemento)
    
    #elementosParametros=pd.read_excel("Datos.xlsx",sheet_name="Desvios2")
    #parametros=elementosParametros[elemento]
    parametros=desvio[elemento]
    dt.SeleccionarDatos(elemento,parametros[0],parametros[1],parametros[2],parametros[3],parametros[4],parametros[5],parametros[6])
    #print(parametros)

# se crea la ventana principal
ventana1=tk.Tk()
ventana1.title("Control de caliad")
ventana1.geometry('380x300')
ventana1.configure(background='orange')
var=tk.StringVar(ventana1)
var.set('Elija un elemento')
 # se lee desde el excel la hoja desvios con los elementos a graficar
desvio=pd.read_excel("Datos.xlsx",sheet_name="Desvios2", header=0)
cabeza=["Seleccione un elemento"]
cabeza=desvio.columns

#se crea una variable para almacenar el valor seleccionado
variable = tk.StringVar(ventana1)
variable.set(cabeza[0])
# se crea el combobox o lista desplegable
option_menu = OptionMenu(ventana1, variable, *cabeza)
option_menu.pack()


cuadro_texto = tk.Entry(ventana1)
cuadro_texto.pack()

boton_obtener = tk.Button(ventana1, text="Graficar", command=obtener_valor_seleccionado)
boton_obtener.pack()







ventana1.mainloop()



