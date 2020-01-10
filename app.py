# Aplicacion grafica sencilla que permite realizar operaciones en una base de datos sqlite
from tkinter import *
import interface
import menu
import entradas
import labels
import botones

# Iniciar app
root= Tk()

interface.darFormato(root)

menu.darFormato(root)

frame = Frame(root)
frame.pack()

labels.darFormato(frame)

entradas.darFormato(frame)

frame2 = Frame(root)
frame2.pack()

botones.darFormato(frame2)

# Cerrar app
root.mainloop()