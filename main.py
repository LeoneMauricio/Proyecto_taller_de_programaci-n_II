from db import crear_tabla
from tkinter import *
from agregar import ventana_agregar
from actualizar import ventana_actualizar
from eliminar import ventana_eliminar
from mostrar import ventana_productos

crear_tabla()


ventana_principal = Tk()
ventana_principal.title("Registros de Productos")
# Maximiza la ventana después de crearla
ventana_principal.after(100, lambda: ventana_principal.state("zoomed"))
ventana_principal.resizable(0,0)
ventana_principal.grid_anchor("center")
ventana_principal.configure(bg="purple")
Label(
    ventana_principal,
    text = "Menu Principal",
    font = ("Arial",23, "bold"),
    bg="purple",
    fg="white"
).grid(row=0, column=0, columnspan=2, pady=10)

Button(
    ventana_principal,
    text="Mis productos",
    font=("Arial", 20),
    bg="gray36",
    fg="white",
    cursor="hand2",
    bd=2,
    relief="solid",
    command= ventana_productos
).grid(row=1, column=0, padx=10, pady=10)
Button(
    ventana_principal,
    text="Agregar productos",
    font=("Arial", 20),
    bg="forest green",
    fg="white",
    cursor="hand2",
    bd=2,
    relief="solid",
    command= ventana_agregar
).grid(row=1, column=1, padx=10, pady=10)
Button(
    ventana_principal,
    text="Eliminar productos",
    font=("Arial", 20),
    bg="red2",
    fg="white",
    bd=2,
    relief="solid",
    cursor="hand2",
    command=lambda: [ventana_eliminar(), ventana_productos()]
).grid(row=2, column=0, padx= 10, pady= 10)
Button(
    ventana_principal,
    text="Modifcar productos",
    font=("Arial", 20),
    bg="blue",
    fg="white",
    cursor="hand2",
    bd=2,
    relief="solid",
    command=ventana_actualizar
).grid(row=2, column=1, padx=10, pady=10)


ventana_principal.mainloop()


