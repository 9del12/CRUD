from tkinter import *

def crearLabels(frame):
        idLabel = Label(frame, text = 'Id(Automático):')
        idLabel.grid(row = 0, column = 0, sticky = 'e', padx = 10, pady = 10)

        nombreLabel = Label(frame, text = 'Nombre:')
        nombreLabel.grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 10)

        apellidoLabel = Label(frame, text = 'Apellido:')
        apellidoLabel.grid(row = 2, column = 0, sticky = 'e', padx = 10, pady = 10)

        userLabel = Label(frame, text = 'User:')
        userLabel.grid(row = 3, column = 0, sticky = 'e', padx = 10, pady = 10)

        passLabel = Label(frame, text = 'Password:')
        passLabel.grid(row = 4, column = 0, sticky = 'e', padx = 10, pady = 10)

        comentLabel = Label(frame, text = 'Comentarios:')
        comentLabel.grid(row = 5, column = 0, sticky = 'e', padx = 10, pady = 10)

class darFormato:
    def __init__(self, frame):
        self.frame = frame
        crearLabels(frame)
