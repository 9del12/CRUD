from tkinter import *
import bbdd
from tkinter import messagebox
import entradas
import sqlite3

def crearRegistro():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()
    datos = entradas.getEntradas()

    miCursor.execute('INSERT INTO DATOS_USUARIOS(NOMBRE, APELLIDO, USER, PASS, COMENTARIOS) VALUES(?, ?, ?, ?, ?)', datos)

    miConexion.commit()

    messagebox.showinfo('Base de Datos', 'Registro insertado con éxito')

def leerRegistro():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()
    id = entradas.getId()
    
    miCursor.execute('SELECT * FROM DATOS_USUARIOS WHERE ID = ' + id)

    elUsuario = miCursor.fetchall()
    
    entradas.setDatos(elUsuario)

def actualizarRegistro():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()
    datos = entradas.getEntradas()
    id = entradas.getId()
    
    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE='"+ datos[0] + "', APELLIDO = '" + datos[1] + "', USER = '" + datos[2] + "', PASS = '" + datos[3] + "', COMENTARIOS = '" + datos[4] + "' WHERE ID = " + id)

    miConexion.commit()

    messagebox.showinfo('Base de Datos', 'Registro actualizado con éxito')

def eliminarRegistro():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()
    datos = entradas.getEntradas()
    id = entradas.getId()
    
    miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID = " + id)

    miConexion.commit()

    messagebox.showinfo('Base de Datos', 'Registro eliminado con éxito')

    entradas.vaciar()

class crear:
    def __init__(self):
        crearRegistro()

class leer:
    def __init__(self):
        leerRegistro()

class actualizar:
    def __init__(self):
        actualizarRegistro()

class eliminiar:
    def __init__(self):
        eliminarRegistro()

    
     
