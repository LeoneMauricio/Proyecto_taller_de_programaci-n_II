from tkinter import *
from tkinter import messagebox
from db import actualizar, obtener_por_id

def ventana_actualizar():
    ventana = Tk()
    ventana.title("Actualizar productos")
    ventana.geometry("500x500")
    titulo = Label(
        ventana,
        text = "Actualizar Productos",
        font = ("Arial",18, "bold")
    )
    titulo.pack()
    label_id = Label(ventana, text="ID")
    label_id.pack()
    entrada_id = Entry(ventana)
    entrada_id.pack()
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
    
    def buscar_producto():
        producto = obtener_por_id(entrada_id.get())
        
        if not producto:
            messagebox.showwarning(
                "Atención",
                "No existe un producto con ese ID", parent=ventana)
            return
        
        entrada_nombre.delete(0, "end")
        entrada_descripcion.delete(0, "end")
        entrada_precio.delete(0, "end")

        entrada_nombre.insert(0, producto[1])
        entrada_descripcion.insert(0, producto[2])
        entrada_precio.insert(0, producto[3])
        
    botonInfo = Button(
            ventana,
            text="Mostrar info",
            command= buscar_producto
        )
    botonInfo.pack(pady=5)


    def modificar():
        id_par = entrada_id.get()
        nom = entrada_nombre.get()
        des = entrada_descripcion.get()
        prec = entrada_precio.get()

        try:
            id_producto = int(id_par)
        except ValueError:
            messagebox.showerror("Error","El ID debe ser un número entero", parent=ventana)
            return

        try:
            prec = float(prec)
            if prec <= 0:
                messagebox.showwarning("Atencion","Los precios deben ser positivos", parent=ventana)
                return
        except ValueError:
            messagebox.showerror("Error","Debe ingresar numeros",parent=ventana)
        else:
            actualizar(nom,des,prec,id_producto)
            #messagebox.showinfo("Correcto","Producto Acualizado", parent=ventana)
        
    botonActualizar = Button(
        ventana,
        text="Actualizar",
        command= modificar
        )
    botonActualizar.pack(pady=5)
    
    
    
    
    ventana.mainloop()