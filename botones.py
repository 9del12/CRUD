from tkinter import *

def crearBotones(frame2):
        
        botonCreate = Button(frame2, text = 'Create')
        botonCreate.grid(row = 2, column = 0, sticky = 'e', padx = 10, pady = 20)

        botonRead = Button(frame2, text = 'Read')
        botonRead.grid(row = 2, column = 1, sticky = 'e', padx = 10, pady = 20)

        botonUpdate = Button(frame2, text = 'Update')
        botonUpdate.grid(row = 2, column = 2, sticky = 'e', padx = 10, pady = 20)

        botonDelete = Button(frame2, text = 'Delete')
        botonDelete.grid(row = 2, column = 3, sticky = 'e', padx = 10, pady = 20)

class darFormato:
    def __init__(self, frame2):
        self.frame2 = frame2
        crearBotones(self.frame2)
    
    
