alumno = {
    'Matematicas': 10,
    'Literatura': 8,
    'Arte': 6,
    'Computacion': 7,
    'Ingles': 9
}

valores = [v for _, v in alumno.items()]
average = sum (valores) / len(valores)

print(average) # Promedio de calificaciones
print(max(alumno.items())) # Calificacion mas alta
