from tkinter import *
import bbdd
import sys
from tkinter import messagebox
import entradas
import crud

def conectar():
    bbdd.conectar()

def salir():
    valor = messagebox.askquestion('Salir', 'Desea salir de la aplicacion?')
    if valor == 'yes':
        sys.exit()

def crearMenu(root):
    barraMenu = Menu(root)
    root.config(menu = barraMenu, width = 300, height = 300)

    bbddMenu = Menu(barraMenu, tearoff = 0)
    bbddMenu.add_command(label = 'Conectar', command = conectar)
    bbddMenu.add_command(label = 'Salir', command = salir)

    borrarMenu = Menu(barraMenu, tearoff = 0)
    borrarMenu.add_command(label = 'Vaciar todo', command = entradas.vaciar)

    crudMenu = Menu(barraMenu, tearoff = 0)
    crudMenu.add_command(label = 'Crear', command = crud.crear)
    crudMenu.add_command(label = 'Leer', command = crud.leer)
    crudMenu.add_command(label = 'Actualizar', command = crud.actualizar)
    crudMenu.add_command(label = 'Eliminar', command = crud.eliminiar)

    ayudaMenu = Menu(barraMenu, tearoff = 0)
    ayudaMenu.add_command(label = 'Licencia')
    ayudaMenu.add_command(label = 'Acerca de...')

    barraMenu.add_cascade(label = 'Base de Datos', menu = bbddMenu)
    barraMenu.add_cascade(label = 'Vaciar campos', menu = borrarMenu)
    barraMenu.add_cascade(label = 'CRUD', menu = crudMenu)
    barraMenu.add_cascade(label = 'Ayuda', menu = ayudaMenu)

class darFormato:
    def __init__(self,root):
        self.root = root
        crearMenu(root)
