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
        elif opcion in [1, 2, 3, 4]:
            numeros = []
            resultado = None 

            for i in range(2):
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
            
            if opcion == 1:
                resultado = suma(numeros[0], numeros[1])
            elif opcion == 2:
                resultado = resta(numeros[0], numeros[1])  
            elif opcion == 3:
                resultado = multiplicacion(numeros[0], numeros[1])
            elif opcion == 4:
                resultado = division(numeros[0], numeros[1])
            
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida. Intente de nuevo.")


calculadora()
