# Programa que imprime el tamaño de un cuadrado y triángulo usando asteriscos

num = int(input("Ingrese el tamaño de lado del cuadrado: "))
for i in range(num):
    print("* " * num)

altura = int(input("Ingrese la altura del triángulo: "))
for i in range(1, altura + 1):
    print("* " * i)
