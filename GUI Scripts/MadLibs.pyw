from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

# window

main = Tk()
main.title('Mad Libs Game')
main.geometry('335x355')

# Funciones

def Nombre():
    Nombre = MDEntry.get()
    return Nombre

def Color_Favorito():
    Color_Favorito = MDEntry2.get()
    return Color_Favorito

def Comida_Favorita():
    Comida_Favorita = MDEntry3.get()
    return Comida_Favorita

def Limite_Nombre(*args):
    valor = MDEntryVar.get()
    if len(valor) > 10:
        MDEntryVar.set(valor[:11])

def Limite_Color(*args):
    valor = MDEntryVar2.get()
    if len(valor) > 10:
        MDEntryVar2.set(valor[:11])

def Limite_Comida(*args):
    valor = MDEntryVar3.get()
    if len(valor) > 10:
        MDEntryVar3.set(valor[:11])

def Get_All():
    Todo = f'''En un dia tan lindo como hoy esta personita llamada/o {Nombre()}\nDecide arrancar su dia de la mejor formacomiendo {Comida_Favorita()}\nPara despues salir vistiendo su mejor prenda color {Color_Favorito()}\n
Hoy va a ser un hermoso dia y espero pongas el mejor de los animos para ello!'''
    return Todo
    
def Send():
    MDLabel5.config(state=NORMAL)
    MDLabel4.config(text='Completo')
    MDLabel5.delete(0.0, 'end')
    MDLabel5.insert(0.0,  Get_All())
    MDLabel5.config(state=DISABLED)

def Clear():

    MDLabel5.config(state=NORMAL)

    clear1 = MDEntryVar.get()
    clear2 = MDEntryVar2.get()
    clear3 = MDEntryVar3.get()

    MDLabel4.config(text='Estado')
    MDLabel5.delete(0.0, 'end')
    MDEntryVar.set(clear1[:0])
    MDEntryVar2.set(clear2[:0])
    MDEntryVar3.set(clear3[:0])

    MDLabel5.config(state=DISABLED)

# Label

MDLabel = Label(main, text='Nombre')
MDLabel.place(x= 10, y= 10)

MDEntryVar = StringVar()
MDEntryVar.trace('w', Limite_Nombre)
MDEntry = Entry(main, textvariable= MDEntryVar)
MDEntry.place(x= 65, y= 10)

MDLabel2 = Label(main, text='Color')
MDLabel2.place(x=10, y= 40)

MDEntryVar2 = StringVar()
MDEntryVar2.trace('w', Limite_Color)
MDEntry2 = Entry(main, textvariable= MDEntryVar2)
MDEntry2.place(x= 65, y= 40)

MDLabel3 = Label(main, text='Comida')
MDLabel3.place(x= 10, y=70)

MDEntryVar3= StringVar()
MDEntryVar3.trace('w', Limite_Comida)
MDEntry3 = Entry(main, textvariable= MDEntryVar3)
MDEntry3.place(x=65, y=70)

MDButton = Button(main, text='Enviar', command=Send)
MDButton.place(x=10, y=110)

MDButton2 = Button(main, text='Limpiar', command=Clear)
MDButton2.place(x= 110, y= 110)

MDLabel4 = Label(main, text='Estado')
MDLabel4.place(x=205, y=113)

MDLabel5= Text(main, height= 13, width= 40, state=DISABLED)
MDLabel5.place(x=7, y= 140)

# Loop

main.mainloop()
