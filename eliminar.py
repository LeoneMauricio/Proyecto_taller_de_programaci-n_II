from tkinter import *
from tkinter import messagebox
from db import eliminar

def ventana_eliminar():
    ventana = Tk()
    ventana.title("Eliminar productos")
    ventana.geometry("500x500")
    titulo = Label(
        ventana,
        text = "Eliminar los Productos",
        font = ("Arial",18, "bold")
    )
    titulo.pack()
    label_id = Label(ventana, text="ID")
    label_id.pack()
    entrada_id = Entry(ventana)
    entrada_id.pack()
    def eliminado():
        try:
            id = int(entrada_id.get())
            if id <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese numero mayores a 0", parent=ventana)
            return
        confirmar = messagebox.askyesno("Confirmar", "Desea eliminar este producto", parent=ventana)
        if confirmar:
            fila = eliminar(id)
            messagebox.showinfo("Correcto", "Producto eliminado", parent=ventana)
            ventana.destroy()
        else:
            messagebox.showwarning("Atencion", "No existe ese id", parent=ventana)
    boton_eliminar = Button(
        ventana,
        text= "Eliminar",
        command =eliminado
    )
    boton_eliminar.pack(pady=5)
    
