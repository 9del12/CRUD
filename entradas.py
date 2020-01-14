from tkinter import *

def crearEntradas(frame):
    global miId
    miId = StringVar()
    global miNombre
    miNombre = StringVar()
    global miApellido
    miApellido = StringVar()
    global miUser
    miUser = StringVar()
    global miPass
    miPass = StringVar()

    global cuadroId
    cuadroId = Entry(frame, textvariable = miId, state = DISABLED)
    cuadroId.grid(row = 0, column = 1, padx  = 10, pady = 10)

    cuadroNombre = Entry(frame, textvariable = miNombre)
    cuadroNombre.grid(row = 1, column = 1, padx  = 10, pady = 10)

    cuadroApellido = Entry(frame, textvariable = miApellido)
    cuadroApellido.grid(row = 2, column = 1, padx  = 10, pady = 10)

    cuadroUser = Entry(frame, textvariable = miUser)
    cuadroUser.grid(row = 3, column = 1, padx  = 10, pady = 10)
    cuadroUser.config(fg = 'red')

    cuadroPass = Entry(frame, textvariable = miPass)
    cuadroPass.grid(row = 4, column = 1, padx  = 10, pady = 10)
    cuadroPass.config(show = '*')

    global textoComentario
    textoComentario = Text(frame, width = 16, height = 5)
    textoComentario.grid(row = 5, column = 1, padx  = 10, pady = 10)
    scrollVert = Scrollbar(frame, command = textoComentario.yview)
    scrollVert.grid(row = 5, column = 2, sticky = 'nsew')
    textoComentario.config(yscrollcommand = scrollVert.set)

    botonCreate = Button(frame, text = 'Habilitar', command = estadoId)
    botonCreate.grid(row = 0, column = 3, sticky = 'e', padx = 10, pady = 20)

def vaciar():
    miNombre.set('')
    miApellido.set('')
    miUser.set('')
    miPass.set('')
    miId.set('')
    textoComentario.delete(1.0, END)
    cuadroId.config(state = DISABLED)

def estadoId():
    cuadroId.config(state = NORMAL)

def getEntradas():
    datos = [
        miNombre.get(),
        miApellido.get(),
        miUser.get(),
        miPass.get(),
        textoComentario.get(0.0, END)
    ]
    return datos


def getId():
    return miId.get()


def setDatos(elUsuario):
    for dato in elUsuario:
        miNombre.set(dato[1])
        miApellido.set(dato[2])
        miUser.set(dato[3])
        miPass.set(dato[4])
        textoComentario.insert(1.0, dato[5])

class darFormato:
    def __init__(self, frame):
        self.frame = frame
        crearEntradas(frame)
        

