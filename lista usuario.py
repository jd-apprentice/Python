lista = []

while len(lista) < 10:
    numero_ingresado = int(input('Ingrese un numero: '))
    if numero_ingresado > 0:
        lista.append(numero_ingresado)

print(lista)
print(sum(lista)) # Suma de todos los numeros
print(sum(lista) / len(lista)) # Average de la lista
print(max(lista)) # Numero mas alto
print(min(lista)) # Numero mas bajo
