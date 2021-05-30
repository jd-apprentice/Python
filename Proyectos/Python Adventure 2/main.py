from classes.game import Personaje, Ubicacion
from classes.habilidades import Skills
from classes.magia import Magic
from tkinter import ttk
import sys
import tkinter


# Variables

jugando = True

# Creando habilidades

Golpetazo = Skills('Golpetazo', 'Un golpe poco mas fuerte que el normal', 10, 20)
Cortada = Skills('Cortada', 'Una cortada rapida con ambas manos', 5, 15)

# Creando magia ofensiva

Bola_Fuego = Magic('Bola de Fuego', 'Una simple bola de fuego', 5, 15)
Tornado = Magic('Tornado', 'Un tornado que arraza todo', 15, 30)

personaje_skills = [Golpetazo, Cortada]
personaje_magia = [Bola_Fuego, Tornado]

enemigo_skills = [Cortada]
enemigo_magia = [Bola_Fuego]

# Creando Ubicaciones

Campamento = Ubicacion('Campamento', 'A1', 'Tu campamento inicial cerca de un rio, este cuenta con equipamento necesario para acampar')
Rio = Ubicacion('Rio', 'A2', 'Rio cercano al campamento, diriguiendose a la Mansion plage heart')

# Creando personajes

warrior = Personaje('Jonathan', 200, 40, 30, 15, personaje_skills, [])
adventurer = Personaje('Gustavo', 125, 50, 15, 10, personaje_skills, [])
wizard = Personaje('Martin', 100, 100, 10, 10, [], personaje_magia)

# Creando enemigos

orco = Personaje('Orgo Guerrero', 150, 20, 15, 10, enemigo_skills, [])
troll = Personaje('Troll Mago', 125, 80, 10, 10, [], enemigo_magia)
asesino = Personaje('????', 300, 50, 20, 20, enemigo_skills, enemigo_magia)
