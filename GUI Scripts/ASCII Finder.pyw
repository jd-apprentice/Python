import PySimpleGUI as sg

#Type one letter and receive an ASCII value of it

sg.theme('DarkBlack')

layout = [
    [sg.T('Escribi un caracter: '), sg.InputText()],
    [sg.B('Enviar'), sg.B('Salir')] 
    ]

window = sg.Window('ASCII Finder', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Salir':
        break
    try:
        mapeado = print(' '.join(map(str, values[0])))
        sg.popup(f'Tu caracter fue {values[0]}\ny el valor ASCII es {ord(values[0])}')
    except TypeError:
        sg.popup('¡Error! tiene que ser un solo caracter')
