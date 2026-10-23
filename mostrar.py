from tkinter import *
from tkinter import ttk
from db import obtener_todos

def ventana_productos():
    ventana = Tk()
    ventana.title("Mis productos")
    ventana.geometry("500x500")

    tabla = ttk.Treeview(ventana, columns=("id", "nombre","descripcion", "precio"), show="headings")

    tabla.heading("id", text="ID", anchor="center")
    tabla.heading("nombre", text="Nombre", anchor="center")
    tabla.heading("descripcion", text="Descripción", anchor="center")
    tabla.heading("precio", text="Precio", anchor="center")
    
    tabla.column("id", width=50)
    tabla.column("nombre", width=100)
    tabla.column("descripcion", width=120)
    tabla.column("precio", width=80)

# Agregar filas
    productos = obtener_todos()
    for fila in productos:
        tabla.insert("", END, values=fila)


    tabla.pack(fill="both", expand=True)


