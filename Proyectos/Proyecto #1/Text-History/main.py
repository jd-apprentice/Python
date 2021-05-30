import random
import sys
import time
import vlc
from clases import ant
from clases import viajero
from clases import goblin
from playsound import playsound

# Map

inicio = {
    'Ubicacion': 'Casa abandonada',
    'Cordenada': 'A1',
    'Descripcion': 'Te encuentras en la casa abandonada que se menciono al principio, puedes notar su mal estado aunque todavia es util para hacer preparativos'
}

camino = {
    'Ubicacion': 'Sendero de la jungla',
    'Cordenada': 'A2',
    'Descripcion': 'Giras la cabeza a tus alrededores del sendero y encuentras una pequeña mochila con algunos objetos'
}

campamento = {
    'Ubicacion': 'Campamento cercano a la mansion',
    'Cordenada': 'B1',
    'Descripcion': 'Un campamento en establo aceptable, la fogata tiene poca leña y la tienda necesita unos arreglos pero puede servir'
}

mansion = {
    'Ubicacion': 'Mansion plage heart',
    'Cordenada': 'B2',
    'Descripcion': 'Despues de ser destruida por un devastante terremoto, cientos de años despues la mansion sigue abandonada.\nActualmente esta infectada de hormigas enormes cuales no les importa la historia de su lugar.\nLos rumores dicen que Rhogath-Ghesh un reloj legendario esta escondido aqui'
}

lago = {
    'Ubicacion': 'Lago de sevroth',
    'Cordenada': 'C1',
    'Descripcion': 'Pequeño lago a proximidad de la citadel de sevroth'
}

citadel = {
    'Ubicacion': 'Frozen citadel of sevroth',
    'Cordenada': 'C2',
    'Descripcion': 'En lo mas profundo de la jungla alejado de la sociedad se encuentra esta citadel, esta misma infectada de goblins no muy amigables de hecho'
}

# Externo

sound_file = vlc.MediaPlayer("C:\\Users\\Super\\Desktop\\code\\sound\\Elven.mp3")

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

# Variables

start_game, exit, finish_character, dead, win, = False, False, False, False, False
this_character, this_ant, this_goblin, your_choice, select_character, este_enemigo= '', '', '', '', '', ''

# Contadores

count_examinar = 0
count_cordenadas = 0
count_attack = 0
count_objeto = 0
count_vida = 0
count_damage = 0

# Turnos

def mi_turno():
        choose = input(f'Que accion deseas realizar? \n -> Attack \n -> Objeto \n -> ').lower().strip()
        time.sleep(2)
        if choose == 'attack':
            global count_attack
            count_attack += 1
            def attack(enemy):
                if enemy == choice_enemigo:
                    mi_damage(arma_simple)
                    time.sleep(.5)
                    if este_enemigo.vida >0:
                        enemigo_damage()    
            attack(choice_enemigo)
        if choose == 'objeto':
            global count_objeto
            count_objeto += 1
            time.sleep(.5)
            curar_objeto(cura_simple)
            print()
            print(f'{este_enemigo.nombre.lower()} te ataca haciendo {(este_enemigo.ataque - this_character.defensa)} de daño pero te curas {cura_simple} y tienes {this_character.vida} restante')

# Funciones

def battle():
    sound_file = vlc.MediaPlayer('C:\\Users\\Super\\Desktop\\Code\\sound\\battle.mp3')
    sound_file.play()

def mbattle():
    while este_enemigo.vida > 0 and this_character.vida >0:
        mi_turno()
        
    if este_enemigo.vida <0:
        print(f'{este_enemigo.nombre.lower()} fue derrotado! puedes continuar tu camino..')
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
        

# Menu

print()
print('############################## PYTHON ADVENTURE ##############################'.center(200))
print('')
print('###############'.center(200))
print('START'.center(201))
print('EXIT'.center(199))
print('game made by jd.apprentice'.center(200))
print('###############'.center(200))
print()
print('############################## PYTHON ADVENTURE ##############################'.center(200))

time.sleep(1)

sound_file.play()
while start_game == False:
    your_choice = input('¿Que quieres hacer? -> ').lower()
    print()
    if your_choice == 'exit':
        sys.exit()
    elif your_choice == 'start':
        start_game = True

# Seleccionar personaje

while not finish_character:

    select_character = input('Selecciona tu personaje \n "swordman" \n "dancer" \n "knight" \n "warrior" \n -> ').lower().strip()

    if select_character == 'swordman':
        print('Este aventurero es el swordman: \n')
        print(viajero1.nombre)
        print(viajero1.clase)
        print(viajero1.vida, 'HP')
        print(viajero1.mana, 'Mana')
        print(viajero1.ataque, 'Ataque')
        print(viajero1.magia, 'Magia')
        print(viajero1.defensa, 'Defensa')
        print(viajero1.resistencia_magica, 'Defensa Magica')
        print()
        your_choice = input('¿Quieres usar este personaje?: \n -> ').lower().strip()
        if your_choice == 'si':
            time.sleep(1)
            finish_character = True
            this_character = viajero1

    elif select_character == 'dancer':
        print('Este aventurero es el dancer: \n')
        print(viajero2.nombre)
        print(viajero2.clase)
        print(viajero2.vida, 'HP')
        print(viajero2.mana, 'Mana')
        print(viajero2.ataque, 'Ataque')
        print(viajero2.magia, 'Magia')
        print(viajero2.defensa, 'Defensa')
        print(viajero2.resistencia_magica, 'Defensa Magica')
        print()
        your_choice = input('¿Quieres usar este personaje?: \n -> ').lower().strip()
        if your_choice == 'si':
            time.sleep(1)
            finish_character = True
            this_character = viajero2

    elif select_character == 'knight':
        print('Este aventurero es el knight: \n')
        print(viajero3.nombre)
        print(viajero3.clase)
        print(viajero3.vida, 'HP')
        print(viajero3.mana, 'Mana')
        print(viajero3.ataque, 'Ataque')
        print(viajero3.magia, 'Magia')
        print(viajero3.defensa, 'Defensa')
        print(viajero3.resistencia_magica, 'Defensa Magica')
        print()
        your_choice = input('¿Quieres usar este personaje?: \n -> ').lower().strip()
        if your_choice == 'si':
            time.sleep(1)
            finish_character = True
            this_character = viajero3

    elif select_character == 'warrior':
        print('Este aventurero es el warrior: \n')
        print(viajero4.nombre)
        print(viajero4.clase)
        print(viajero4.vida, 'HP')
        print(viajero4.mana, 'Mana')
        print(viajero4.ataque, 'Ataque')
        print(viajero4.magia, 'Magia')
        print(viajero4.defensa, 'Defensa')
        print(viajero4.resistencia_magica, 'Defensa Magica')
        print()
        your_choice = input('¿Quieres usar este personaje?: \n -> ').lower().strip()
        if your_choice == 'si':
            time.sleep(1)
            finish_character = True
            this_character = viajero4

 
# Juego

while not dead:
    sound_file.stop()
    sound_file = vlc.MediaPlayer('C:\\Users\\Super\\Desktop\\Code\\sound\\Relaxing.mp3')
    sound_file.play()

    # Pantalla de carga

    print()
    print('########## ESTO ES UNA PANTALLA DE CARGA ##########')
    print('           Explicacion de jugabilidad              ')
    print('Tus opciones para las preguntas "que deseas hacer" ')
    print('Estas son:\n"Examinar": Inspecciona el lugar donde te encuentras dandote una leve explicacion\n"Cordenadas" te muestra en que cordenada estas\n"Avanzar": Vas hacia la siguiente cordenada')
    print('Las cordenadas te moves de A1 -> A2 o A2 -> B1/C1')
    print('Espero las instrucciones hayan sido algo claras disfruta el juego!')
    time.sleep(2)

    # Inicio

    print()
    print('Comenzando la historia te encuentras en una', (inicio['Ubicacion'].lower()))
    print()
    time.sleep(2)
    siguiente_area = False

    # Primera Accion

    while siguiente_area == False:
        what_to_do = input('Que deseas hacer? -> ').lower()
        if what_to_do == 'examinar':
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
                time.sleep(1)
                 
            elif count_examinar >= 1:
                print()
                print('Ya examinaste este lugar!')
                time.sleep(1)
            
        if what_to_do == 'cordenadas':
            print()
            print(inicio['Cordenada'])
            print('Si avanzas vas hacia delante llegaras al', camino['Ubicacion'].lower())
            print()
            time.sleep(2)
        if what_to_do == 'avanzar':
            print('Te diriges hacia el', camino['Ubicacion'].lower())
            time.sleep(2)
            print()
            siguiente_area = True

    siguiente_area = False

    # Pelea

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

    # 2 Caminos

    sound_file.stop()
    sound_file = vlc.MediaPlayer('C:\\Users\\Super\\Desktop\\Code\\sound\\Relaxing.mp3')
    sound_file.play()

    while siguiente_area == False:
        this_road = ''
        what_to_do = input('Que deseas hacer? -> ').lower().strip()
        if what_to_do == 'examinar':
            time.sleep(1)
            if count_vida <= 0:
                count_examinar += 1
                count_vida += 1
                descripcion_camino()
                curarse_nocombat(cura_normal)
                print()
                print(f'Encontraste una manzana en la mochila.. decides comer la manzana esta te cura {cura_normal} ahora tienes {this_character.vida} HP')
                time.sleep(1)
            elif count_vida >= 1:
                print()
                print('Ya examinaste este lugar!')
                time.sleep(1)

        if what_to_do == 'cordenadas':
            print()
            print(camino['Cordenada'])
            print('si avanzas vas hacia delante puedes llegar a distintos lugares\n',campamento['Ubicacion'].lower(),'\n',lago['Ubicacion'].lower())
            print()
            time.sleep(2)
        if what_to_do == 'avanzar':
            chose = input('Donde quieres ir? b1 o c1 \n -> ').lower().strip()
            if chose == 'b1':
                print('Te diriges hacia el', campamento['Ubicacion'].lower())
                time.sleep(1)
                print()
                siguiente_area = True
                this_road = campamento
            if chose == 'c1':
                print('Te diriges hacia el', lago['Ubicacion'].lower())
                time.sleep(1)
                print()
                siguiente_area = True
                this_road = lago

    siguiente_area = False

# Pelea 2

    sound_file.stop()
    battle()

    choice_enemigo = ['this_ant', 'this_goblin']
    este_enemigo = random.choice(choice_enemigo)
    
    if este_enemigo == 'this_ant':
        este_enemigo = ant2
    else:
        este_enemigo = goblin2
    
    text()
    
    mbattle()  

    while siguiente_area == False:
        what_to_do = input('Que deseas hacer? -> ').lower().strip()
        if what_to_do == 'examinar':
            count_examinar += 1
            print(this_road['Descripcion'])
            print(f'Parece que te gusta mucho inspeccionar las cosas.. tu contador de examinar dice que vas {count_examinar} de veces')
            print()
            time.sleep(2)
        if what_to_do == 'cordenadas':
            print(this_road['Cordenada'])
            print()
            time.sleep(2)
        if what_to_do == 'avanzar':
            if this_road == campamento:
                print('Te dirigues hacia la', mansion['Ubicacion'].lower())
                print()
                siguiente_area = True
            elif this_road == lago:
                print('Te dirigues hacia la', citadel['Ubicacion'].lower())
                print()
                siguiente_area = True

    print('Hasta aca llega la historia! muchas gracias por probar mi historia interactiva proximamente continuara teniendo mas enemigos, un jefe final y otras cosas')
    time.sleep(10)
    break