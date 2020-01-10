from tkinter import *

def crearMenu(root):
    barraMenu = Menu(root)
    root.config(menu = barraMenu, width = 300, height = 300)

    bbddMenu = Menu(barraMenu, tearoff = 0)
    bbddMenu.add_command(label = 'Conectar')
    bbddMenu.add_command(label = 'Salir')

    borrarMenu = Menu(barraMenu, tearoff = 0)
    borrarMenu.add_command(label = 'Borrar campos')

    crudMenu = Menu(barraMenu, tearoff = 0)
    crudMenu.add_command(label = 'Crear')
    crudMenu.add_command(label = 'Leer')
    crudMenu.add_command(label = 'Actualizar')
    crudMenu.add_command(label = 'Borrar')

    ayudaMenu = Menu(barraMenu, tearoff = 0)
    ayudaMenu.add_command(label = 'Licencia')
    ayudaMenu.add_command(label = 'Acerca de...')

    barraMenu.add_cascade(label = 'Base de Datos', menu = bbddMenu)
    barraMenu.add_cascade(label = 'Borrar campos', menu = borrarMenu)
    barraMenu.add_cascade(label = 'CRUD', menu = crudMenu)
    barraMenu.add_cascade(label = 'Ayuda', menu = ayudaMenu)

class darFormato:
    def __init__(self,root):
        self.root = root
        crearMenu(root)
