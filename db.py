import sqlite3
def conexion():
    con = sqlite3.connect("productos.db")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos
(id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
descripcion TEXT NOT NULL,
precio REAL NOT NULL)""")
    con.commit()
    con.close()

def insertar(nombre, descripcion, precio):
    con = conexion()
    cursor = con.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (?, ?, ?)",
                (nombre, descripcion, precio))
    con.commit()
    con.close()

def obtener_todos():
    con = conexion()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    con.close()
    return productos

def eliminar(id):
    con = conexion()
    cursor = con.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    con.commit()
    filas = cursor.rowcount
    con.close()
    return filas

def actualizar(nom, des, prec, id_producto):
    con = conexion()
    cursor = con.cursor()
    cursor.execute("UPDATE productos SET nombre = ?, descripcion = ?, precio = ? WHERE id = ?",
                (nom, des, prec, id_producto))
    con.commit()
    filas = cursor.rowcount
    con.close()
    return filas

def obtener_por_id(id):
    con = conexion()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()
    con.close()
    return producto 
