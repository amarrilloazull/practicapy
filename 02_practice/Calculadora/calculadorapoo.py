class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b
    
    def multi(self, a, b):
        return a * b
    
    def div(self, a, b):
        while b == 0:
            print("Todo número divido por 0 es indefinido")
            b = float(input("Ingrese un nuevo divisor (diferente a 0): "))

        resultado = a / b
        return resultado
        
    
# Uso de la calculadora

calculadora = Calculadora()
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))


print("Suma: ", calculadora.suma(a, b))
print("Resta: ", calculadora.resta(a, b))
print("Multiplicación: ", calculadora.multi(a, b))
print("División: ", calculadora.div(a, b))

