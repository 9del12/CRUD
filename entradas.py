from tkinter import *

def crearEntradas(frame):
    cuadroId = Entry(frame)
    cuadroId.grid(row = 0, column = 1, padx  = 10, pady = 10)

    cuadroNombre = Entry(frame)
    cuadroNombre.grid(row = 1, column = 1, padx  = 10, pady = 10)

    cuadroApellido = Entry(frame)
    cuadroApellido.grid(row = 2, column = 1, padx  = 10, pady = 10)

    cuadroUser = Entry(frame)
    cuadroUser.grid(row = 3, column = 1, padx  = 10, pady = 10)
    cuadroUser.config(fg = 'red')

    cuadroPass = Entry(frame)
    cuadroPass.grid(row = 4, column = 1, padx  = 10, pady = 10)
    cuadroPass.config(show = '*')

    textoComentario = Text(frame, width = 16, height = 5)
    textoComentario.grid(row = 5, column = 1, padx  = 10, pady = 10)
    scrollVert = Scrollbar(frame, command = textoComentario.yview)
    scrollVert.grid(row = 5, column = 2, sticky = 'nsew')
    textoComentario.config(yscrollcommand = scrollVert.set)

class darFormato:
    def __init__(self, frame):
        self.frame = frame
        crearEntradas(frame)
        

