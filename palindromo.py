lista_palindromo = []
lista_normal = []
numero_de_palabras = 0

while numero_de_palabras < 5:
    texto = input("Ingrese una palabra: ").lower()
    numero_de_palabras += 1
    rever = texto[::-1]
    if texto == rever:
        lista_palindromo.append(texto)
    else:
        lista_normal.append(texto)

if len(lista_palindromo) == 0:
    print('No ingresaste ninguna palabra palidromo!')
else:
    print(lista_palindromo)