clave = 'alfajor'
respuesta = ''
intentos = 0
intentos_maximos = 3
sin_intentos = False

while respuesta != clave and not sin_intentos:
    if intentos < intentos_maximos:
        respuesta = input('Escribe una clave: ')
        intentos += 1
    else:
        sin_intentos = True

if respuesta == clave:
    print('Clave correcta')

elif sin_intentos == True:
    print(f'Sin intentos, la clave era {clave}')