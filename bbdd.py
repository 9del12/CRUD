import sqlite3
from tkinter import messagebox

def conectarbbdd():
    try:
        miConexion = sqlite3.connect('Usuarios')

        miCursor = miConexion.cursor()

        miCursor.execute('CREATE TABLE DATOS_USUARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), USER VARCHAR(50), PASS VARCHAR(50), COMENTARIOS VARCHAR(50) )')

        messagebox.showinfo('BBDD', 'Base de datos creada con éxito')

    except:
        messagebox.showwarning('BBDD', 'La base de datos ya existe')


class conectar:
    def __init__(self):
        conectarbbdd()

