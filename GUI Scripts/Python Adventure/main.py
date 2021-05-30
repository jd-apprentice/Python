import random
import PySimpleGUI as sg
import sys
import time
import vlc
from clases import ant
from clases import viajero
from clases import goblin

# Map

inicio = {
    'Ubicacion': 'Casa abandonada',
    'Cordenada': 'A1',
    'Descripcion': '''Te encuentras en la casa abandonada que se menciono al principio, 
puedes notar su mal estado aunque todavia es util para hacer preparativos
    '''
}

camino = {
    'Ubicacion': 'Sendero de la jungla',
    'Cordenada': 'A2',
    'Descripcion': 'Giras la cabeza a tus alrededores del sendero y encuentras una pequeña mochila con algunos objetos'
}

campamento = {
    'Ubicacion': 'Campamento cercano a la mansion',
    'Cordenada': 'B1',
    'Descripcion': '''Un campamento en establo aceptable,
la fogata tiene poca leña y la tienda necesita unos arreglos pero puede servir'''
}

mansion = {
    'Ubicacion': 'Mansion plage heart',
    'Cordenada': 'B2',
    'Descripcion': '''Despues de ser destruida por un devastante terremoto, 
cientos de años despues la mansion sigue abandonada.
\nActualmente esta infectada de hormigas enormes cuales no les importa la historia de su lugar.
\nLos rumores dicen que Rhogath-Ghesh un reloj legendario esta escondido aqui'''
}

lago = {
    'Ubicacion': 'Lago de sevroth',
    'Cordenada': 'C1',
    'Descripcion': 'Pequeño lago a proximidad de la citadel de sevroth'
}

citadel = {
    'Ubicacion': 'Frozen citadel of sevroth',
    'Cordenada': 'C2',
    'Descripcion': '''En lo mas profundo de la jungla alejado de la sociedad se encuentra esta citadel,
esta misma infectada de goblins no muy amigables de hecho'''
}

# Externo

sound_file = vlc.MediaPlayer("C:\\Users\Super\\Desktop\\out GitHub\\py simple gui\\PySimpleGui\\Python Adventure\\sound\\Elven.mp3")

# Personajes - Clases

viajero1 = viajero('Jonathan', 'Swordman', 200, 10, 35, 5, 10, 10)
viajero2 = viajero('Elena', 'Dancer', 150, 100, 10, 30, 10, 10)
viajero3 = viajero('Samantha', 'Knight', 250, 20, 20, 15, 10, 10)
viajero4 = viajero('Ethan', 'Warrior', 175, 0, 40, 0, 10, 10)

ant1 = ant('Ant Exploradora', 100, 30, 5)
ant2 = ant('Ant Luchador', 120, 30, 10)
ant4 = ant('Rey Ant', 350, 50, 30)

goblin1 = goblin('Goblin Explorador', 100, 30, 5)
goblin2 = goblin('Goblin Luchador', 120, 30, 10)
goblin4 = goblin('Rey Goblin', 350, 45, 30)

# Funciones Personajes

def swordman():

    print('Este aventurero es el swordman: \n')
    print(viajero1.nombre)
    print(viajero1.clase)
    print(viajero1.vida, 'HP')
    print(viajero1.mana, 'Mana')
    print(viajero1.ataque, 'Ataque')
    print(viajero1.magia, 'Magia')
    print(viajero1.defensa, 'Defensa')
    print(viajero1.resistencia_magica, 'Defensa Magica\n')
    print('Este es tu personaje!\n')

def dancer():

    print('Este aventurero es el dancer: \n')
    print(viajero2.nombre)
    print(viajero2.clase)
    print(viajero2.vida, 'HP')
    print(viajero2.mana, 'Mana')
    print(viajero2.ataque, 'Ataque')
    print(viajero2.magia, 'Magia')
    print(viajero2.defensa, 'Defensa')
    print(viajero2.resistencia_magica, 'Defensa Magica\n')
    print('Este es tu personaje!\n')

def knight():

    print('Este aventurero es el knight: \n')
    print(viajero3.nombre)
    print(viajero3.vida, 'HP')
    print(viajero3.mana, 'Mana')
    print(viajero3.ataque, 'Ataque')
    print(viajero3.magia, 'Magia')
    print(viajero3.defensa, 'Defensa')
    print(viajero3.resistencia_magica, 'Defensa Magica')
    print('Este es tu personaje!\n')

def warrior():

    print('Este aventurero es el warrior: \n')
    print(viajero4.nombre)
    print(viajero4.vida, 'HP')
    print(viajero4.mana, 'Mana')
    print(viajero4.ataque, 'Ataque')
    print(viajero4.magia, 'Magia')
    print(viajero4.defensa, 'Defensa')
    print(viajero4.resistencia_magica, 'Defensa Magica')
    print('Este es tu personaje!\n')

# Variables

start_game = False
finish_character = False
dead = False
win = False

count_start = False
siguiente_area = False

this_character = None
this_ant = None
this_goblin = None
this_road = None
your_choice = None
select_character = None
este_enemigo = None

# Contadores

count_examinar = 0
count_cordenadas = 0
count_attack = 0
count_objeto = 0
count_vida = 0
count_damage = 0
count_pantalla = 0
fail_start = 0

# Contadores Ventanas

count_win1 = 0
count_win2 = 0
count_win3 = 0
count_win4 = 0
count_win5 = 0

# Turnos

def mi_turno():
        print('Que accion deseas realizar? \n -> Attack \n -> Objeto \n -> ')
        window, event, values = sg.read_all_windows()
        if event == 'ATTACK':
            global count_attack
            count_attack += 1
            def attack(enemy):
                if enemy == choice_enemigo:
                    mi_damage(arma_simple)
                    time.sleep(.5)
                    if este_enemigo.vida >0:
                        enemigo_damage()    
            attack(choice_enemigo)
        if event == 'OBJETO':
            global count_objeto
            count_objeto += 1
            time.sleep(.5)
            curar_objeto(cura_simple)
            print()
            print(f'{este_enemigo.nombre.lower()} te ataca haciendo {(este_enemigo.ataque - this_character.defensa)} de daño pero te curas {cura_simple} y tienes {this_character.vida} restante')

# Funciones

def battle():
    sound_file = vlc.MediaPlayer('C:\\Users\Super\\Desktop\\out GitHub\\py simple gui\\PySimpleGui\\Python Adventure\\sound\\battle.mp3')
    sound_file.play()

def mbattle():
    while este_enemigo.vida > 0 and this_character.vida >0:
        mi_turno()
        
    if este_enemigo.vida <0:
        print(f'{este_enemigo.nombre.lower()} fue derrotado! puedes continuar tu camino..')
        sound_file.stop()
        time.sleep(2)
        print()   

def text():
    print(f'Avanzando hacia el siguiente camino te encuentras con.. {este_enemigo.nombre.lower()} y este inicia un combate!')
    print()
    time.sleep(3)

# Armas

arma_simple = random.randint(5,15)
arma_hierro = random.randint(10,20)
arma_epic = random.randint(15,30)

# Objeto

cura_simple = random.randint(5,15)
cura_normal = random.randint(10,20)
cura_fuerte = random.randint(15,30)

# Daños mundo

damage_simple = random.randint(5,15)
damage_normal = random.randint(10,20)
damage_fuerte = random.randint(15,30)

# Descripcion

def descripcion_inicio():
        print(inicio['Descripcion'])

def descripcion_camino():
        print(camino['Descripcion'])

def descripcion_campamento():
        print(campamento['Descripcion'])

def descripcion_mansion():
        print(mansion['Descripcion'])

def descripcion_lago():
        print(lago['Descripcion'])

def descripcion_citadel():
        print(citadel['Descripcion'])

# Eventos de mundo

def damage_mundo(damage):
    this_character.vida -= damage
    
def curar_objeto(comida):
    enemigo_damage()
    this_character.vida += comida

def curarse_nocombat(comida):
    this_character.vida += comida

    
# Ataque

def mi_damage(arma):
    este_enemigo.vida -= (this_character.ataque + arma) - (este_enemigo.defensa)
    print(f'{this_character.nombre.lower()} ataca a {este_enemigo.nombre.lower()} haciendo {(this_character.ataque + arma) - este_enemigo.defensa} de daño')
    print()
    print(f'{este_enemigo.nombre} HP {este_enemigo.vida}')
    time.sleep(2)

def enemigo_damage():
    this_character.vida -= (este_enemigo.ataque - this_character.defensa)
    print(f'despues de tu accion es turno de {este_enemigo.nombre.lower()} esta te ataca haciendo {este_enemigo.ataque - this_character.defensa} de daño')
    print()
    print(f'{this_character.nombre} HP {this_character.vida}')
    print()
    time.sleep(2) 

# Color Tema 

sg.theme('Darkblack') 

# Layout

def make_win1():
    global count_win1
    count_win1 += 1
    layout1 = [[sg.Text('Action Menu', size=(25, 1)), sg.B('START'), sg.B('ATTACK'), sg.B('OBJECT')],
          [sg.Output(size=(80, 20), font=('Georgia 10'))],
          [sg.Multiline(size=(62, 4), enter_submits=True, key='-ACTION-', do_not_clear=False),
           sg.Button('ENVIAR', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('SALIR', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
    return sg.Window('Python Adventure by jd-apprentice', layout1,font=('Georgia', '13' ),default_button_element_size=(20,2), finalize=True)

def make_win2():
    global count_win2
    count_win2 += 1
    layout2 = [[sg.Text('Character Select', size=(40, 1))],
          [sg.Output(size=(65, 15), font=('Verdana 10'))],
            [sg.Button('SWORDMAN', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
            sg.Button('KNIGHT', button_color=(sg.YELLOWS[0], sg.GREENS[0])),
            sg.Button('WARRIOR', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
            sg.Button('DANCER', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
    return sg.Window('Character Select', layout2,font=('Verdana', ' 13' ),default_button_element_size=(13,2), finalize=True)

def make_win3():
    global count_win3
    count_win3 += 1
    layout3 = [[sg.Text('First Road', size=(40, 1))],
          [sg.Output(size=(65, 15), font=('Helvetica 10'))],
           [sg.Button('EXAMINAR', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('CORDENADAS', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('SALIR', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('AVANZAR', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
    return sg.Window('First Road', layout3,font=('Helvetica', ' 13' ),default_button_element_size=(13,2), finalize=True)

def make_win4():
    global count_win4
    count_win4 += 1
    layout4 = [[sg.Text('The path', size=(40, 1))],
          [sg.Output(size=(65, 15), font=('Helvetica 10'))],
           [sg.Button('EXAMINAR', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('CORDENADAS', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('SALIR', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('AVANZAR', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
    return sg.Window('The path', layout4,font=('Georgia', '13' ),default_button_element_size=(13,2), finalize=True)

def make_win5():
    global count_win5
    count_win5 += 1
    layout5 = [[sg.Text('Choose your path', size=(25, 1))],
          [sg.Output(size=(30, 10), font=('Helvetica 10'))],
           [sg.Button('CAMP', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('SALIR', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('LAKE', button_color=(sg.YELLOWS[0], sg.BLUES[0]))]]
    return sg.Window('Choose your path', layout5,font=('Verdana', ' 13' ),default_button_element_size=(13,2), finalize=True)

# Comienza con Window1

window1, window2, window3, window4, window5 = make_win1(), None, None, None, None      

# Juego

while not dead:

    window, event, values = sg.read_all_windows()
    query = values['-ACTION-'].rstrip()

    if event == sg.WIN_CLOSED or event == 'SALIR':
        window.close()
        if window == window2:
            window2 = None
        if window == window3:
            window3 = None
        if window == window4:
            window4 = None
        if window == window5:
            window5 = None
        elif window == window1:     
            break

    if event == 'START':

        start_game = True
        
        while count_start == False:

            sound_file.play()
            print()
            print('############ PYTHON ADVENTURE ############')
            print()
            print('START')
            print('EXIT')
            print('game made by jd.apprentice')
            print()
            print('############ PYTHON ADVENTURE ############')
            print()
            count_start = True 


    # Comandos

    if event == 'ENVIAR' and query == 'exit':
        sys.exit()

    elif event == 'ENVIAR' and query == 'start':

        print('Iniciando juego..')

        while not finish_character and start_game == True:
                
            window2 = make_win2()

            print('Selecciona tu personaje: "swordman" - "dancer"\n')

            window, event, values = sg.read_all_windows()

            if event == 'SWORDMAN':

                swordman()

                finish_character = True
                this_character = viajero1
                time.sleep(4)

            elif event == 'DANCER':

                dancer()

                finish_character = True
                this_character = viajero2
                time.sleep(4)
            
            elif event == 'KNIGHT':

                knight()

                finish_character = True
                this_character = viajero3
                time.sleep(4)

            elif event == 'WARRIOR':

                warrior()

                finish_character = True
                this_character = viajero4
                time.sleep(4)

        # Prelude

        if window == window2:
            window.close()

            while count_pantalla <= 0 and start_game == True:

                sound_file.stop()
                sound_file = vlc.MediaPlayer('C:\\Users\\Super\\Desktop\\Code\\sound\\Relaxing.mp3')
                sound_file.play()

                # Pantalla de carga
                        
                print()
                print('########## ESTO ES UNA PANTALLA DE CARGA ##########')
                print()
                print('           Explicacion de jugabilidad              ')
                print('Tus opciones para las preguntas "que deseas hacer" ')
                print('Estas son:\n"Examinar": Inspecciona el lugar donde te encuentras dandote una leve explicacion\n"Cordenadas" te muestra en que cordenada estas\n"Avanzar": Vas hacia la siguiente cordenada')
                print('Las cordenadas te moves de A1 -> A2 o A2 -> B1/C1')
                print('Espero las instrucciones hayan sido algo claras disfruta el juego!')
                time.sleep(5)

                # Inicio

                print()
                print('Comenzando la historia te encuentras en una', (inicio['Ubicacion'].lower()))
                print()
                time.sleep(1)
                count_pantalla += 1

                # Primera Accion

                while not siguiente_area and start_game == True:

                    if count_win3 > 0:
                        window.close()

                    window3 = make_win3()

                    print('Selecciona tu accion')

                    window, event, values = sg.read_all_windows()

                    if event == 'EXAMINAR':

                        if count_examinar <= 0:
                            print()
                            print('Examinando...')
                            print()
                            descripcion_inicio()
                            time.sleep(2)
                            damage_mundo(damage_simple)
                            count_examinar += 1
                            print()
                            print(f'Entrando a la casa se te cae una madera encima de la cabeza perdiendo {damage_simple} de ¡vida!\nTu personaje aun tiene {this_character.vida}')
                            time.sleep(3)
                                        
                        elif count_examinar >= 1:
                            print()
                            print('Ya examinaste este lugar!')
                            time.sleep(2)
                                
                    elif event == 'CORDENADAS':
                        print()
                        print(inicio['Cordenada'])
                        print('Si avanzas vas hacia delante llegaras al', camino['Ubicacion'].lower())
                        print()
                        time.sleep(2)

                    elif event == 'AVANZAR':
                        print('Te diriges hacia el', camino['Ubicacion'].lower())
                        time.sleep(2)
                        print()
                        siguiente_area = True

                    elif event == 'SALIR':
                        sys.exit()

                if window == window3 or window4:
                    window.close()

                # Pelea
                
                siguiente_area = False

                sound_file.stop()
                battle()

                choice_enemigo = ['this_ant', 'this_goblin']
                este_enemigo = random.choice(choice_enemigo)
                                
                if este_enemigo == 'this_ant':
                    este_enemigo = ant1
                else:
                    este_enemigo = goblin1
                                
                text()
                                
                mbattle()

                sound_file.stop()

        # 2 Caminos
                
            while not siguiente_area and start_game == True and this_road == None:

                if count_win4 > 0:
                    window4.close()

                window4 = make_win4()

                print('Que deseas hacer?')

                window, event, values = sg.read_all_windows()

                if event == 'EXAMINAR':

                    if count_vida <= 0:
                        count_examinar += 1
                        count_vida += 1
                        descripcion_camino()
                        curarse_nocombat(cura_normal)
                        print()
                        print(f'Encontraste una manzana en la mochila.. decides comer la manzana esta te cura {cura_normal} ahora tienes {this_character.vida} HP')
                        time.sleep(3)
                    elif count_vida >= 1:
                        print()
                        print('Ya examinaste este lugar!')
                        time.sleep(1)

                elif event == 'CORDENADAS':

                        print()
                        print(camino['Cordenada'])
                        print('si avanzas vas hacia delante puedes llegar a distintos lugares\n',campamento['Ubicacion'].lower(),'\n',lago['Ubicacion'].lower())
                        print()
                        time.sleep(3)

                elif event == 'SALIR':
                        sys.exit()

                elif event == 'AVANZAR':

                    if count_win5 > 0:
                        window5.close()

                    window5 = make_win5()

                    print('Selecciona tu camino con los botones')

                    window, event, values = sg.read_all_windows()

                    if event == 'CAMP':

                        print('Te diriges hacia el', campamento['Ubicacion'].lower())
                        time.sleep(2)
                        print()
                        siguiente_area = True
                        this_road = campamento

                    elif event == 'LAKE':

                        print('Te diriges hacia el', lago['Ubicacion'].lower())
                        time.sleep(2)
                        print()
                        siguiente_area = True
                        this_road = lago

                    if window == window4 or window5:
                        window5.close()
                        window4.close()
                        
                    # Pelea 2

                    choice_enemigo = ['this_ant', 'this_goblin']

                    este_enemigo = random.choice(choice_enemigo)

                    if este_enemigo == 'this_ant':
                        este_enemigo = ant2
                    else:
                        este_enemigo = goblin2

                    text()

                    mbattle()

                    sound_file.stop()

                    print('Hasta aca llega el juego!')
