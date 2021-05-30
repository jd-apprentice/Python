palabra = input('Escribi una palabra: ').lower()
vocales = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in palabra:
    if char in vocales:
        count += 1

print(f'El numero de vocales es {count}')