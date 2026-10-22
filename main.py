#import db 
from tkinter import *
from tkinter import messagebox
#db.crear_tabla()

def ventana_producto():
    ventana = Tk()
    ventana.title("Mis productos")
    ventana.geometry("500x500")    
def ventana_agregar():
    ventana = Tk()
    ventana.title("Agregar productos")
    ventana.geometry("500x500") 
def ventana_eliminar():
    ventana = Tk()
    ventana.title("Eliminar productos")
    ventana.geometry("500x500") 
def ventana_modificar():
    ventana = Tk()
    ventana.title("Modificar productos")
    ventana.geometry("500x500") 

ventana_principal = Tk()
ventana_principal.title("Registros de Productos")
ventana_principal.geometry("500x500")
ventana_principal.resizable(0,0)

Label(
    ventana_principal,
    text = "Menu Principal",
    font = ("Arial",18, "bold")
).pack(pady=20)

Button(
    ventana_principal,
    text="Mis productos",
    command= ventana_producto
).pack(pady=5)
Button(
    ventana_principal,
    text="Agregar productos",
    command= ventana_agregar
).pack(pady=5)
Button(
    ventana_principal,
    text="Eliminar productos",
    command= ventana_eliminar
).pack(pady=5)
Button(
    ventana_principal,
    text="Modifcar productos",
    command=ventana_modificar
).pack(pady=5)


ventana_principal.mainloop()


 
