# Importaciones

import random
import time
import vlc
from time import strftime

# Externo

sound_file = vlc.MediaPlayer("C:\\Users\\Super\\Desktop\\Code\\sound\\Elven.mp3")

# Listas

listaProtagonistas = ['niño','Obama','Profesor','Superdotado','Deforme',
                      'Veneco','Otaku','Argentino promedio','Mono','NPC','Empleado de burger king']
listaCarencias = ['Tu Futuro','La felicidad','Tu iphone','La hermana del verdulero','El maruchan prohibido','Un supermercado','Tu IQ perdido''Tus ganas de vivir',
                  'Un teclado en descuento','Un cupon de zapatos','Un tutorial sin loquendo']
listaBusqueda = ['En uber','En barco','En dragon','En moto','Atravesando rios',
                 'Cruzando altos de san lorenzo','Cruzando la villa 11-14','En micro','En skate','En avion presidencial']
listaObjeto = ['Gatitos','Cuadernos','Joysticks','Espadas','Antorchas',
               'Latas de coca-cola','Llaves rotas','Pastillas de stress','Hechizos que bajan el IQ','Alfajores']
listaPrueba = ['Alberto Fernandez','Lag','Un mago sin mana',
               'Moyano y sus camiones','Titanes muertos','Piratas sin armas','Aliens','Dioses del mc donals','Estafas piramidales','Amway',]
listaReturn = ['Volviendo a tu hogar','Triunfando','Derrotado',
               'Haciendote amigo del enemigo','Descubriendo que el camino de tu vida no era este']

# Funciones

def showOpening():
    print()
    time.sleep(1)
    print('PRIMERA PARTE - "TU HISTORIA" '.center(150))
    time.sleep(10)
    print()
    print()
    print()
    print()
    print('bienvenido a una nueva historia donde muchas cosas pueden pasar'.center(150))
    time.sleep(3)
    print('primero te advierto aqui no decides que o quien eres'.center(150))
    time.sleep(3)
    print('en esta historia podes ser un niño, enano, elfo, robot, un grupo de baile y muchas cosas mas!'.center(150))
    time.sleep(3)
    print('esta historia puede terminar bien o mal, todo depende de tu suerte'.center(150))
    time.sleep(3)
    print('tu solo vienes por lo que deseas, haras lo que sea posible, por cualquier medio y lugar no importa si es bueno o malo'.center(150))
    time.sleep(3)
    print('ahora avancemos con la historia y sabremos quienes eres'.center(150))
    time.sleep(3)
    print()

def WhatYouAre():
    print()
    time.sleep(1)
    print('SEGUNDA PARTE - "¿QUIEN ERES?"'.center(150))
    time.sleep(10)
    print(f'{strftime("%Y-%m-%d %H:%M:%S")}'.center(150))
    time.sleep(3)
    print('alguien nacio.. esa persona hoy sera algo que quizas no se sienta identificado..'.center(150))
    time.sleep(3)
    print('pero en el destino de la vida, nadie elige quien es, ni de donde viene..'.center(150))
    time.sleep(2)
    print('.'.center(150))
    time.sleep(2)
    print('.'.center(150))
    time.sleep(2)
    print('.'.center(150))
    YouAre = random.choice(listaProtagonistas)
    print(f'entre todas las cosas del universo, entre todas las razas personas y creaciones divinas, hoy te toca ser...'.center(150))
    time.sleep(2)
    print(f'¡Un {YouAre.lower()}!'.center(150))


def YourWish():
    WhatYouWant = random.choice(listaCarencias)
    time.sleep(2)
    print(f'en esta historia vas a estar buscando...\n¡{WhatYouWant.lower()}!')
    time.sleep(3)
    print(f'te deseo mucha suerte buscando {WhatYouWant.lower()} la necesitaras...')
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")


def YourJourney():
    TravelBy = random.choice(listaBusqueda)
    print(f'comenzando el dia vas a dirigirte hacia tu objetivo\n¡{TravelBy.lower()}!')
    time.sleep(3)
    print(f'no creo que sea facil, pero si yo pude programar esto vos podes tambien')
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")


def youFound():
    EpicItem = random.choice(listaObjeto)
    print(f'durante tu aventura encuentras\n¡{EpicItem.lower()}!')
    time.sleep(2)
    print(f'decides guardar tus {EpicItem.lower()}')
    time.sleep(2)
    print("puede que esto sea util de alguna forma...?")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")


def yourTest():
    EpicTest = random.choice(listaPrueba)
    print(f'llegando casi al final de tu camino te encuentras con una gran prueba... esta es\n¡{EpicTest.lower()}!')
    time.sleep(2)
    print(f'estas listo para derrotar ¿¡{EpicTest.lower()}!?')
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")


def yourBack():
    VictoryorDefeat = random.choice(listaReturn)
    print(f'despues de tu interminable lucha, tu intento por conseguir tu objetivo hace que termines... \n¡{VictoryorDefeat.lower()}!')
    if VictoryorDefeat == "Derrotado":
        time.sleep(2)
        print("Escuchame pichon al menos lo intentaste...")
    elif VictoryorDefeat == "Volviendo a tu hogar":
        time.sleep(2)
        print("Mira sos bastante paja la verdad para irte despues de todo esto...")
    elif VictoryorDefeat == "Triunfando":
        time.sleep(2)
        print("¡Felicidades por triunfar con tu objetivo!, si te sentis generoso podes comprarme una big mac")
    elif VictoryorDefeat == "Haciendote amigo del enemigo":
        time.sleep(2)
        print("Que hiciste chinchulin.. Me parece que sos medio vende patria vos")
    elif VictoryorDefeat == "Descubriendo que el camino de tu vida no era este":
        time.sleep(2)
        print("Suele pasar mucho... la vida continua...")

# Code

playAgain = 'si'
while playAgain == 'si' or playAgain == 's':
    sound_file.play()
    showOpening()
    WhatYouAre()
    YourWish()
    YourJourney()
    youFound()
    yourTest()
    yourBack()

    print('Queres escuchar otra historia? (si o no)')
    sound_file.stop()
    playAgain = input()
