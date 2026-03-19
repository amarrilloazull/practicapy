# Creamos lista 1
frutas = ["manzana", "banano"]
# El método append nos es útil para agregar elementos a una lista en este caso YA establecida
# Lista.append(elemento)
frutas.append("naranja")
print(frutas) # Imprimos la lista 


# Creamos lista 2
numeros = [1, 2, 3]

# Añadimos dos números a lista
numeros.append([5, 6])
print(numeros) # Imprimimos la lista


# Creamos lista 3
autos = ["Ford", "Mazda"]
autos.append("Renault")
print(", ".join(autos)) # Podemos usar el .join para mostrar la lista sin los corchetes. ", ".join(lista a evaluar). En este caso la , es para que se imprima de esta manera después del elemento de la lista


# Creamos lista 4
comida = ["hamburguesa", "pepito"]
comida.append("sombrero")
print(*comida) # También podemos usar el "desempaquetador" pero es un poco más feo, muestra la lista solamente sin los corchetes y sin comas
