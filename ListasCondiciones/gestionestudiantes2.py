estudiantes = [] # Creamos una lista vacia

cantidad = int(input("¿Cuántos estudiantes desea promediar?: ")) # Mostramos el mensaje que iterara a los estudiantes a ingresar

for i in range(cantidad): # Iteramos sobre el rango establecido en "cantidad"
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ") 
    
    numero_notas = int(input(f"¿Cuántas notas tiene {nombre}?: ")) # Segunda iteración. Cantidad de veces que veces que va a pedir nota a X estudiante
    notas_lista = [] # Creamos la segunda lista vacia

    for j in range(numero_notas): # Ciclo for que itera sobre la cantidad de notas que se piden ingresar
        while True: # Ciclo while que nos controla el flujo de la nota ingresada. Si no se cumple se rompe el programa pero vuelve a pedir la nota 
            nota = float(input(f"Ingrese nota {j+1}: "))
        
            if nota < 0.0 or nota <= 5.0:
                notas_lista.append(nota) # Se pasan las notas de "nota" a la segunda lista que creamos anteriormente 
                break 
            else:
                print("Nota inválida. Intente de nuevo")
                

    estudiantes.append({"nombre": nombre, "notas": notas_lista}) # Añadimos a la primer lista vacia dos elementos. Lo definiría como la variable + un identificador, es lo que permitirá llamarlo más abajo


print("\n Resultados \n")
for estudiante in estudiantes:
    promedio = sum(estudiante["notas"]) / len(estudiante["notas"]) # Sumamos cada nota de la iteración estudiante que itera sobre estudiantes. Se divide por lo que devuelve el "len", que es es la cantidad de notas ingresadas por cada estudiante

    if promedio >= 3.0:
        print(f"{estudiante['nombre']} - Promedio: {promedio:.2f}. Aprobado") # Se muestran los mensajes de aprobación + desaprobación + 2 decimales

    else:
        print(f"{estudiante['nombre']} - Promedio: {promedio:.2f}. Desaprobado")
