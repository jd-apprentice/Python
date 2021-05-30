# Importaciones

import vlc, random, time
from time import strftime
from playsound import playsound

# Musica

sound_file = vlc.MediaPlayer("C:\\Users\\Super\\Desktop\\Code\\sound\\Elven.mp3")

# Personas

vidaGolpeado = 100
vida = 100

# Valores

dañoRecibido = random.randint(1,10)
curarVida = random.randint(1,10)

# Objetos

propiasManos = random.randint(5,10)
paloMadera = random.randint(15,35)

# Introduccion

sound_file.play()
print()
print('¡Te recuerdo! para elegir las opciones colocar simplemente la letra en la cual la opcion se encuentra ej a, b, c, etc'.upper())
print()
time.sleep(4)

# Comenzando

print('el dia y hora ' ,strftime("%Y-%m-%d %H:%M:%S"),'una aventura comienza..')
time.sleep(2)
nombre = input('comenzemos por lo aburrido, ¿como te llamas? -> ')
time.sleep(2)
edad = int(input('¿cuantos años tenes? -> '))
time.sleep(2)
print('que onda', nombre, 'tenes', edad, 'años.. y', vida,'de vida, medio un datazo pero por si no te acordabas')
time.sleep(3)

print('dejame comprobar si sos mayor para jugar esta historia')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)

# Code

if edad >= 18:
    print('perfecto', nombre.lower(), 'sos mayor podes jugar esta historia')
    time.sleep(2)
    queresJugar = input('¿queres jugar esta historia? \n a) si \n b) no \n -> ').lower()
    time.sleep(2)

    if queresJugar == 'a':
        print('¡en ese caso bienvenido a la historia interactiva!')
        time.sleep(4)
        primerCamino = input('un dia te dieron ganas de salir de casa y decidiste salir a caminar pero despues de caminar rato largo llegas en frente de un barrio que no conoces y te preguntas: ¿a este punto donde deberia ir? \n a) izquierda \n b) derecha \n -> ').lower()
        time.sleep(1)

        if primerCamino == 'a':
            time.sleep(2)
            vida -= dañoRecibido
            playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\punch.mp3')
            print(f'caminando hacia la izquierda cruzaste un puente pero te topaste con una persona de muy mal humor y esta te golpeo perdiendo {dañoRecibido} de ¡vida!, ahora tenes {vida} de vida')
            time.sleep(2)
            print('recuerda que si tu vida se reduce a 0 puntos perderas el juego')
        elif primerCamino == 'b':
            time.sleep(2)
            print('tomaste el camino tranquilo, cruzaste el puente derecho y nada raro ocurrio continuaras con', vida, 'de vida')

        # Cambio de primerCamino

        primerCamino = input(f'despues de pasar el puente llegaste a un barrio algo peligroso donde la gente no te mira bien, ¿que vas a hacer? \n a) caminar mirando hacia abajo \n b) ignrorar la situacion y actuar normal \n -> ').lower()
        if primerCamino == 'a':
            time.sleep(1)
            print('decides caminar ocultando tu mirada, lo cual parece seguro pero atraes la atencion de alguien \n'
                  'esta persona se te acerca y te decide hablar contigo \n'
                  'persona molesta: que te pasa que vas mirando hacia abajo tan mal educado vas a ser? *tocando tu hombro* \n')
            time.sleep(5)
            queHacer = input('¿que decides hacer o decir? \n a) levantar la mirada y pedir perdon \n b) quitar rapidamente su mano de tu hombro y decirle no me toques \n c) darle un puñetazo -> ').lower()
            if queHacer == 'a':
                time.sleep(2)
                print('la persona molesta hace un gesto de insatisfacción pero decide alejarse, avanzas en tu camino sin ningun problema')
                time.sleep(2)
                print('¡sobreviviste! con', vida, 'vida restante..')
                time.sleep(5)

            elif queHacer == 'b':
                    time.sleep(1)
                    vida -= dañoRecibido
                    playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\punch2.mp3')
                    print('la persona te da un puñetazo por decirle que no lo toques.. pierdes', dañoRecibido, 'de vida.. aun tienes', vida, 'de vida.. pero continuas tu camino')
                    time.sleep(2)
                    print('¡sobreviviste! con', vida, 'vida restante..')
                    time.sleep(5)

            elif queHacer == 'c':
                    time.sleep(1)
                    vidaGolpeado -= propiasManos
                    playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\punch.mp3')
                    print('decides darle un puñetazo en la cara a la otra persona, la persona golpeada recibe', propiasManos, 'aun tiene', vidaGolpeado, 'de vida')
                    time.sleep(3)
                    print('esta persona reacciona mal tras tu puñetazo y decide iniciar una ¡pelea contigo!')
                    time.sleep(3)
                    # Pelea

                    playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\punches.mp3')
                    print(nombre, 'lanza 3 puñetazos causando', propiasManos*3, 'de ¡daño!')
                    vidaGolpeado -= propiasManos*3
                    time.sleep(3)
                    print('la persona golpeada aun tiene', vidaGolpeado, 'de ¡vida!')
                    time.sleep(3)
                    playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\punch2.mp3')
                    print('la persona golpeada decime tomar un palo de madera y golpearte con el!')
                    time.sleep(3)
                    vida -= paloMadera
                    print('tu vida bajo a', vida,'!')
                    time.sleep(3)
                    queHago = input('notando su presencia con un palo decides.. \n a) salir corriendo \n b) pedir disculpas e intentar calmarlo \n c) seguir peleando \n -> ').lower()
                    time.sleep(5)

                    if queHago == 'a':
                        vida -= dañoRecibido
                        print('decides salir corriendo...')
                        playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\run.mp3')
                        print('al alejarte lo suficiente decides tomar un respiro... te excediste demasiado perdiendo', dañoRecibido, 'de vida.. aun tienes', vida, 'vida restante')
                        time.sleep(4)
                        print('estas a salvo.. \n¡sobreviviste! con', vida, 'vida restante..')
                        time.sleep(5)
                    elif queHago == 'b':
                        print('pedir disculpas parece que no a funcionado.. la otra persona sigue muy molesta y se lanza violentamente hacia a ti para golpearte con su palo hasta matarte..')
                        time.sleep(2)
                        playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\dead.mp3')
                        time.sleep(2)
                        print('haz muerto...')
                        time.sleep(5)
                    elif queHago == 'c':
                        playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\attack.mp3')
                        print('no tienes mucha oportunidad contra la persona enojada y su palo de madera.. decides darles algunos puñetazos mas pero caes inconciente tras recibir otro golpe con el palo..')
                        time.sleep(3)
                        print('perdiste..')
                        time.sleep(5)

        if primerCamino == 'b':
            time.sleep(2)
            realizarCompra = input('caminas tranquilamente ignorando la situacion que te rodea, casi saliendo del barrio vez un negocio con articulos en oferta, deseas pasar a comprar algo? \n a) si \n b) no \n -> ').lower()
            if realizarCompra == 'a':
                vida += curarVida
                time.sleep(2)
                playsound('C:\\Users\\Super\\Desktop\\Code\\sound\\drink.mp3')
                print('decides comprar una gaseosa y tomarla.. recuperas', curarVida, 'de ¡vida!')
                time.sleep(1)
                print('ahora tienes', vida, 'de ¡vida!')
                time.sleep(2)
                print('a continuacion sales del barrio.. \n ¡sobreviviste! con', vida, 'vida restante..')
                time.sleep(5)
            elif realizarCompra == 'b':
                print('decides seguir tu camino sin problemas, saliendo del barrio seguramente')
                time.sleep(2)
                print('¡sobreviviste! con', vida, 'vida restante..')
                time.sleep(5)


    else:
        print('nos vemos chinchulin')

elif edad < 18:
    print('no tenes la edad para jugar, tomatela guachin')