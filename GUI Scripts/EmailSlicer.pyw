'''

Basic email slicer with Tkinter, just trying to learn how to use it

'''

from tkinter import *

#Titulo
root = Tk()
root.title('Email Slicer')

#Funcion
def get_usuario_dominio():
    email = ESentry.get().strip()
    try:
        usuario = email[:email.index("@")]
        dominio = email[email.index("@")+1:]
    except ValueError:
        ESerror.config(text=f'Recorda poner un @')

    else:
        resultado = ESerror.config(text=f'Tu usuario es {usuario} y tu dominio es {dominio}')

#Texto
ESLabel = Label(root,text="Escribe tu Email: ",font=("jost",15))
ESLabel.grid()

#Input
ESentryVar = StringVar()
ESentry = Entry(root, width=50,textvariable=ESentryVar)
ESentry.grid()

#Status
ESerror = Label(root,text="Status",fg="red",font=("jost",11))
ESerror.grid()

#Boton
ESbottom = Button(root, text='Start',fg='black',font=("jost",14), command=get_usuario_dominio)
ESbottom.grid()

#Loop
root.mainloop()
