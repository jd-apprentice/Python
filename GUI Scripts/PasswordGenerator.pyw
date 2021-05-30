'''

Password Generator with Tkinter

*Max Lenght 30
*Manually copy your password

'''

import string
import random
from tkinter import *

# Window

main = Tk()
main.title('Password Generator')

# Largo de la contraseña

def Contraseña_Largo():
    
    try:
        largo = PgEntry.get()
        return largo
    except ValueError:
        Pgerror.config(text=f'Numeros!')
    except NameError:
        Pgerror.config(text=f'Esos no son numeros')

# Validar contraseña

def Limite_Caracteres(*args):
    valor = PgEntryVar.get()
    if len(valor) > 2:
        PgEntryVar.set(valor[:2])

# Generar contraseña
    
def Generador_Contraseña(largo):

        caracteres = f'{letras}{numeros}{signos}'
        caracteres = list(caracteres)
        random.shuffle(caracteres)

        contraseña_aleatoria = random.choices(caracteres, k=largo)
        contraseña_aleatoria = ''.join(contraseña_aleatoria)
        return contraseña_aleatoria

# Mostrar la contraseña

def Contraseña_Obtenida():

    try:
        contraseña_usuario = Generador_Contraseña(int(Contraseña_Largo()))
        if len(contraseña_usuario) <= 30:
            PgText.delete(0.0, 'end')
            Pgerror.config(text=f'Completo!')
            PgText.insert(0.0, contraseña_usuario)
        else:
            Pgerror.config(text=f'Numero mayor a 30')
    except TypeError:
        Pgerror.config(text=f'Numeros!')
    except NameError:
        Pgerror.config(text=f'Esos no son numeros')

# Variables globales

letras = string.ascii_letters
numeros = string.digits
signos = string.punctuation

# Layout

PgLabel = Label(main, text='Longitud de tu contraseña: ', font=('jost', 12))
PgLabel.grid()

PgEntryVar = StringVar()
PgEntryVar.trace('w', Limite_Caracteres)
PgEntry = Entry(main, width=5,textvariable=PgEntryVar)
PgEntry.grid()

Pgerror = Label(main, text="Status",fg="red",font=("jost",10))
Pgerror.grid()

PgText = Text(main, width= 35,height=1)
PgText.grid()

Pgbottom = Button(main, text='Start',fg='black',font=("jost",13), command=Contraseña_Obtenida)
Pgbottom.grid()

# Loop

main.mainloop()