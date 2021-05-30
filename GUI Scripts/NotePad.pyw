from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import clipboard

# Window

main = Tk()
main.title('NotePad')

# Variables

AskSave = Toplevel()
AskSave.withdraw()

# Funciones

def SobreMi():
    AboutMe = Toplevel()
    AboutMe.title('Acerca de NotePad')

    Text = Label(AboutMe, text='NotePad realizado por jd_apprentice', font=('jost', 11))
    Text2 = Label(AboutMe, text='Todos los derechos reservados')
    Text.pack()
    Text2.pack()
    
def Copiar():
    Copiar = NText.get(1.0, 'end-1c')
    Copy = clipboard.copy(Copiar)

def Pegar():
    Paste = NText.insert(1.0, clipboard.paste())
    
def Nuevo():

    def Cerrar():
        AskSave.withdraw()
        NText.delete(0.0, 'end-1c')

    def Guardar_Nuevo():
        Guardar_Como()
        NText.delete(0.0, 'end-1c')
    
    # Layout AskSave
    global AskSave
    AskSave = Toplevel()
    AskSave.title('NotePad')
    AskSave.geometry('250x80')
    Text = Label(AskSave, text='¿Quieres guardar los cambios?', font=('jost', 13))
    Text.grid()
    Guardar = Button(AskSave, text='Guardar', command=Guardar_Nuevo)
    Guardar.place(x=10, y=45)
    NoGuardar = Button(AskSave, text='No Guardar', command=Cerrar)
    NoGuardar.place(x= 80, y=45)

def Guardar_Como():
    Type = [('Todos los archivos', '*.*'),
    ('Archivo Python', '*.py'),
    ('Documento de texto', '*.txt')]
    Archivo = asksaveasfile(mode= 'w', filetypes= Type, defaultextension= Type)
    Guardar = NText.get(1.0, 'end-1c')
    Archivo.write(Guardar)
    global AskSave
    AskSave.withdraw()

def Abrir():
    Delete = NText.delete(0.0, 'end-1c')
    OpenFile = filedialog.askopenfile(mode='r')
    Conseguir = OpenFile.read()
    Texto = NText.insert(1.0, Conseguir)

# Layout

MMain = Menu(main)
FMain = Menu(MMain, tearoff=0)
FMain.add_command(label='Nuevo', command=Nuevo)
FMain.add_command(label='Abrir', command=Abrir)
FMain.add_command(label='Guardar como', command=Guardar_Como)

MMain.add_cascade(label='Archivo', menu=FMain)

FMain2 = Menu(MMain, tearoff=0)
FMain2.add_command(label='Copiar', command=Copiar)
FMain2.add_command(label='Pegar', command=Pegar)

MMain.add_cascade(label='Edicion', menu=FMain2)

FMain3 = Menu(MMain, tearoff=0)
FMain3.add_command(label='Sobre mi', command=SobreMi)

MMain.add_cascade(label='Ayuda', menu=FMain3)

NText = Text(main, font=('Ebrima', 11))
NText.grid()

main.config(menu=MMain)
main.mainloop()