import sys
import random

# class Rectangulo:

#     def __init__(self, longitud, ancho):
#         self.longitud = longitud
#         self.ancho = ancho

#     def Calculo(self):

#         try:
#             area = self.longitud * self.ancho
#         except NameError:
#             print('Eso no es un numero')
#             sys.exit()
#         except TypeError:
#             print('Eso no es un numero')
#             sys.exit()
#         else:
#             return area

# Rectangulo_1 = Rectangulo('a', 'a')
# area = Rectangulo_1.Calculo()
# print(f'El area del triangulo es {area}')

class Vehiculo:

    def __init__(self, asientos = 6):
        self.asientos = asientos

class Minibus(Vehiculo):
    def __init__(self):
        super().__init__(self)
        self.ocupados = []

    def Capacidad(self, mas_asientos):
        self.asientos = mas_asientos

    def Pasajeros(self, pasajero):
        if self.Disponible():
            if pasajero in self.ocupados:
                print(f'{pasajero} Ya estaba dentro!, asignando nuevo lugar',end= "")
                self.ocupados.append(f'\nPasajero {str(random.randint(0, 60))}')
            else:
                self.ocupados.append(pasajero)

    def Disponible(self):
        asientos = self.asientos - len(self.ocupados)
        return asientos

class Pasajero():
    def __init__(self, nombre):
        self.nombre = nombre


auto = Vehiculo()
# print()
# print(f'La cantidad de asientos que tiene el auto es: {auto.asientos}\n')

minibus = Minibus()
minibus.Capacidad(50)
# print(f'La cantidad de asientos en el minibus es: {minibus.asientos}\n')

try:
    cant_suben = int(input('Cuantos se suben al minibus?: '))
except ValueError:
    print('Esos no son numeros')
    sys.exit()

if cant_suben > 50:
    print('Sobrepasa la capacidad!')
    sys.exit()
elif cant_suben == 0:
    print('Nadie se subio al minibus')
    sys.exit()

else:
    for i in range(0, cant_suben):
        pasajero = Pasajero(f'\nPasajero {random.randint(0, 60)}')
        minibus.Pasajeros(pasajero.nombre)

lista = (''.join(minibus.ocupados))

print(f'\nLa lista de pasajeros que subieron al minibus es: {lista}')
