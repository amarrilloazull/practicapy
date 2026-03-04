estudiantes = [
        {"nombre": "Santiago", "notas": [2.0, 3.0, 4.5, 5.0]},
        {"nombre": "Jorge", "notas": [5.0, 1.0, 3.4, 1.9]}
        ]

for estudiante in estudiantes:
    totalNotas = sum(estudiante["notas"])
    promedio = totalNotas / 4
    
    if promedio >= 3.0:
        print(f"{estudiante['nombre']} - promedio: {promedio}. Has aprobado") # Concatenación usando f-strings (mucho mejor al imprimirlo)

    else:
        print(f"{estudiante['nombre']} - promedio: {promedio:.2f}. Has reprobado") # Formateamos como se muestra el promedio. Se mostrará con 2 decimales

 
