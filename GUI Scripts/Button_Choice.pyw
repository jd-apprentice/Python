from tkinter import *
from tkinter import ttk

# Window

main = Tk()
main.title('Button Choice')

# Funciones

def limpiar():
    BTText.config(state=NORMAL)
    BTText.delete(0.0, 'end')
    BTText.config(state=DISABLED)

def get_current():
    numero = BTCombo.current()
    if numero == 0:
        get_hello_python()
    elif numero == 1:
        get_hello_java()
    else:
        get_hello_c()
        
def get_hello_python():
    BTText.config(state=NORMAL)
    BTText.delete(0.0, 'end')
    BTText.insert(0.0, '''print('Hello, World!')''')
    BTText.config(state=DISABLED)

def get_hello_java():
    BTText.config(state=NORMAL)
    BTText.delete(0.0, 'end')
    BTText.insert(0.0, '''class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
  }
''')
    BTText.config(state=DISABLED)

def get_hello_c():
    BTText.config(state=NORMAL)
    BTText.delete(0.0, 'end')
    BTText.insert(0.0, '''#include <stdio.h>
int main() {
   printf("Hello, World!");
   return 0;
}''')
    BTText.config(state=DISABLED)

# Variables

choices = ['Python', 'Java', 'C']

# Layout

BTLabel = Label(main, text= 'Hello, World!', font=('jost', 12))
BTLabel.grid()

BTCombo = ttk.Combobox(main, values= choices, state='readonly')
BTCombo.grid()

BTButton = Button(main, text='Mostrar', bg='gold', command=get_current)
BTButton.grid()

BTText = Text(main, width= 45, height=8, state=DISABLED)
BTText.grid()

BTButton2 = Button(main, text='Limpiar', bg='gold', command=limpiar)
BTButton2.grid()

# Loop

main.mainloop()
