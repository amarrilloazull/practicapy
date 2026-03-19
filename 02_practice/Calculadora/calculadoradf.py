def suma(a, b):
    return a + b

def resta(a, b):
    return a - b 

def multiplicacion(a, b):
    return a * b 

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


def mostrar_menu():
    print("""
    ==== Calculadora ====
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir del programa
    """)

def calculadora():
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            print("Has salido de la calculadora. ¡Hasta luego!")
            break
        elif opcion == 1:
            num1 = float(input("Ingrese el número 1: "))
            num2 = float(input("Ingrese el número 2: "))

            resultado = suma(num1, num2)

            print(f"Resultado: {resultado}")

        elif opcion == 2:
            num1 = float(input("Ingrese el número 1: "))
            num2 = float(input("Ingrse el número 2: "))

            resultado = resta(num1, num2)

            print(f"Resultado: {resultado}")

        elif opcion == 3:
            num1 = float(input("Ingrese el número 1: "))
            num2 = float(input("Ingrese el número 2: "))

            resultado = multiplicacion(num1, num2)

            print(f"Resultado: {resultado}")

        elif opcion == 4:
            num1 = float(input("Ingrese el número 1: "))
            num2 = float(input("Ingrese el número 2: "))

            resultado = division(num1 ,num2)

            print(f"Resultado: {resultado}")   
            
        else:
            print("Opción no valida. Intente de nuevo.")



calculadora()
