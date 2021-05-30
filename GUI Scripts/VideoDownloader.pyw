'''
Quite simple python video downloader for youtube, with usage of pytube module and PySimpleGui
Features

* Highest resolution avalible option
* Video and audio separately
* MP4
* Files on the same folder as script
* Status refresh on complete
* Manually update incomplete status after finish
'''

from pytube import YouTube
import PySimpleGUI as sg

# Layout

layout = [
    [sg.Text('Estado de la descarga: '),
     sg.Text(size=(20,1), key='-VENTANA-')],
    [sg.Text('Ingresa tu URL: ')],
    [sg.I('', key='-URL-')],
    [sg.B('Descargar'),sg.B('Solo audio'),sg.B('Solo video'), sg.B('Refrescar'), sg.B('Salir')]
]

# Window Title

window = sg.Window('YouTube Downloader', layout, finalize=True)

# Text before downloading

window['-VENTANA-'].update('Incompleto')

# Loop

while True:

    event, values = window.read()

    text = values['-URL-'].rstrip()

    if event in (sg.WIN_CLOSED, 'Salir'):
        break

    # button to refresh 'Status' of the download
    
    elif event == 'Refrescar': 
        window['-VENTANA-'].update('Incompleto')
        window['-URL-'].update('')

    elif event == 'Solo video':
                
                yt = YouTube(text)
                yt.streams\
                    .filter(file_extension='mp4')\
                    .order_by('resolution')\
                    .desc()\
                    .first()\
                    .download()
                window['-VENTANA-'].update('Completo')
    
    elif event == 'Solo audio':

                yt = YouTube(text)
                yt.streams\
                    .filter(progressive=True)\
                    .first()\
                    .download()
                window['-VENTANA-'].update('Completo')

    elif event == 'Descargar':

                yt = YouTube(text)
                yt.streams\
                    .filter(file_extension='mp4')\
                    .get_highest_resolution()\
                    .download()
                window['-VENTANA-'].update('Completo')

window.close()
