# Calculadora

num1 = float(input('Escribi tu primer numero: '))   
num2 = float(input('Escribi tu segundo numero: '))
accion = input('Escribi tu operacion: ')

if accion == '+':
    resultado = num1 + num2
    print(resultado)

if accion == '-':
    resultado = num1 - num2
    print(resultado)

if accion == '/':
    resultado = num1 / num2
    print(resultado)

if accion == '*':
    resultado = num1 * num2
    print(resultado)

else:
    print('Datos invalidos')