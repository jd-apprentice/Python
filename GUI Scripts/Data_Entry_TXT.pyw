import PySimpleGUI as sg

# Funciones
 
def save():
    if event == 'Save':
        formulario = open(values['-ARCHIVO-'] + '.txt', 'a')
        formulario.write(values['-NOMBRE-'] + '\n')
        formulario.write(values['-APELLIDO-'] + '\n')
        formulario.write(values['-DIRECCION-']+ '\n')
        formulario.write(values['-TELEFONO-']+ '\n')
        formulario.write(values['-DNI-']+ '\n')
        formulario.write('\n')
        formulario.close()

        sg.Popup('Los datos fueron guardados en el TXT llamado: ', values['-ARCHIVO-'])

    else:
        pass

# Layout

layout = [[sg.Text('Llena los datos con lo indicado en cada uno')],
          [sg.Text('Nombre', size=(10, 1)), sg.InputText(key='-NOMBRE-')],
          [sg.Text('Apellido', size=(10, 1)), sg.InputText(key='-APELLIDO-')],
          [sg.Text('Direccion', size=(10, 1)), sg.InputText(key='-DIRECCION-')],
          [sg.Text('Telefono', size=(10, 1)), sg.InputText(key='-TELEFONO-')],
          [sg.Text('DNI', size=(10, 1)), sg.InputText(key='-DNI-')],
          [sg.Text('TXT Nombre', size=(10, 1)), sg.InputText(key='-ARCHIVO-')],
          [sg.Button('Save'), sg.Button('Cancel')]]

# Titulo

window = sg.Window('Data Entry TXT', layout=layout)

# Bucle

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    else:
        save()
