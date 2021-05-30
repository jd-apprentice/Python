from tkinter import *

# Titulo

root = Tk()
root.title("Calculadora Simple")

# Donde se escriben los numeros

espacio = Entry(root, width= 45, borderwidth= 8)
espacio.grid(row = 0, column = 0, columnspan=3, padx = 15, pady= 15)

# Funciones

def b_click(number):
    current = espacio.get()
    espacio.delete(0, END)
    espacio.insert(0, str(current) + str(number))

def b_clear():
    espacio.delete(0, END)

def b_add():
    primer_numero = espacio.get()
    global p_num
    global math
    math = 'sumar'
    p_num = float(primer_numero)
    espacio.delete(0, END)

def b_restar():
    primer_numero = espacio.get()
    global p_num
    global math
    math = 'restar'
    p_num = float(primer_numero)
    espacio.delete(0, END)

def b_multiplicar():
    primer_numero = espacio.get()
    global p_num
    global math
    math = 'multiplicar'
    p_num = float(primer_numero)
    espacio.delete(0, END)

def b_dividir():
    primer_numero = espacio.get()
    global p_num
    global math
    math = 'dividir'
    p_num = float(primer_numero)
    espacio.delete(0, END)

def b_equal():
    segundo_numero = espacio.get()
    espacio.delete(0, END)

    if math == 'sumar':
        espacio.insert(0, p_num + float(segundo_numero))
    if math == 'restar':
        espacio.insert(0, p_num - float(segundo_numero))
    if math == 'multiplicar':
        espacio.insert(0, p_num * float(segundo_numero))  
    if math == 'dividir':
        espacio.insert(0, p_num / float(segundo_numero)) 


# Definir botones

b1 = Button(root, text= '1', padx= 40, pady = 20, command=lambda: b_click(1))
b2 = Button(root, text= '2', padx= 40, pady = 20, command=lambda: b_click(2))
b3 = Button(root, text= '3', padx= 40, pady = 20, command=lambda: b_click(3))
b4 = Button(root, text= '4', padx= 40, pady = 20, command=lambda: b_click(4))
b5 = Button(root, text= '5', padx= 40, pady = 20, command=lambda: b_click(5))
b6 = Button(root, text= '6', padx= 40, pady = 20, command=lambda: b_click(6))
b7 = Button(root, text= '7', padx= 40, pady = 20, command=lambda: b_click(7))
b8 = Button(root, text= '8', padx= 40, pady = 20, command=lambda: b_click(8))
b9 = Button(root, text= '9', padx= 40, pady = 20, command=lambda: b_click(9))
b0 = Button(root, text= '0', padx= 40, pady = 20, command=lambda: b_click(0))
sumar = Button(root, text= '+', padx= 39, pady = 20, command= b_add)
igual = Button(root, text= '=', padx= 91, pady = 20, command= b_equal)
borrar = Button(root, text= 'Clear', padx= 30, pady = 20, command= b_clear)
restar = Button(root, text= '-', padx = 40, pady= 20, command= b_restar)
multiplicar = Button(root, text= '*', padx = 40, pady= 20, command= b_multiplicar)
dividir = Button(root, text= '/', padx = 40, pady= 20, command= b_dividir)

# Botones en la pantalla

b1.grid(row= 3, column= 0)
b2.grid(row= 3, column= 1)
b3.grid(row= 3, column= 2)

b4.grid(row= 2, column= 0)
b5.grid(row= 2, column= 1)
b6.grid(row= 2, column= 2)

b7.grid(row= 1, column= 0)
b8.grid(row= 1, column= 1)
b9.grid(row= 1, column= 2)

b0.grid(row= 4, column= 0)
sumar.grid(row= 4, column= 1)
igual.grid(row= 6, column= 0, columnspan= 2)
restar.grid(row= 4, column= 2)
multiplicar.grid(row =5, column= 0)
dividir.grid(row=5, column =1)
borrar.grid(row= 5, column= 2)

# Loop

root.mainloop()