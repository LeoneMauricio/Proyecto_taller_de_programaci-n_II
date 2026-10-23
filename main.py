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

Label(
    ventana_principal,
    text = "Menu Principal",
    font = ("Arial",18, "bold")
).pack(pady=20)

Button(
    ventana_principal,
    text="Mis productos",
    command= ventana_productos
).pack(pady=5)
Button(
    ventana_principal,
    text="Agregar productos",
    command= ventana_agregar
).pack(pady=5)
Button(
    ventana_principal,
    text="Eliminar productos",
    command=lambda: [ventana_eliminar(), ventana_productos()]
).pack()
Button(
    ventana_principal,
    text="Modifcar productos",
    command=ventana_actualizar
).pack(pady=5)


ventana_principal.mainloop()


