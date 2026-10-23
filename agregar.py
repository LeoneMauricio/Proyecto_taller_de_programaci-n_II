from tkinter import *
from tkinter import messagebox
from db import insertar

def ventana_agregar():
    ventana = Tk()
    ventana.title("Agregar productos")
    ventana.geometry("500x500")
    titulo = Label(
        ventana,
        text = "Agregar tus Productos",
        font = ("Arial",18, "bold")
    )
    titulo.pack()
    label_nombre = Label(ventana, text="Nombre")
    label_nombre.pack()
    entrada_nombre = Entry(ventana)
    entrada_nombre.pack() 
    label_descripcion = Label(ventana, text="Descripcion")
    label_descripcion.pack()
    entrada_descripcion = Entry(ventana)
    entrada_descripcion.pack()
    label_precio = Label(ventana, text="Precio")
    label_precio.pack()
    entrada_precio = Entry(ventana)
    entrada_precio.pack()
    def volver():
        ventana.destroy()
    def guardar():
        nom = entrada_nombre.get()
        des = entrada_descripcion.get()
        prec = entrada_precio.get() 
        if nom == "" or des == "" or prec == "":
            messagebox.showwarning("Atencion","Todos Los campos debes ser completados")
            return
        try:
            prec = float(prec)
            if prec < 1:
                messagebox.showwarning("Atencion","Los precios deben ser positivos", parent=ventana)
                return
        except ValueError:
            messagebox.showerror("Error","Debe ingresar numeros",parent=ventana)
        else:
            insertar(nom,des,prec)
            messagebox.showinfo("Correcto","Producto Agregado", parent=ventana)
        entrada_nombre.delete(0,END)
        entrada_descripcion.delete(0,END)
        entrada_precio.delete(0,END)
    
    boton_agregar = Button(
        ventana,
        text="Agregar",
        command= guardar
    )
    boton_agregar.pack(pady=5)
    boton_volver = Button(
        ventana,
        text="Volver al menu",
        command= volver
    )
    boton_volver.pack(pady=5)
    
    ventana.mainloop()