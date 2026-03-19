class Celular:
    def __init__(self, modelo, marca): # Método especial (constructor) que se ejecuta automáticamente al instanciar un objeto de la clase
        # Su propósito es inicializar los atributos del objeto, asignando valores iniciales o configurando el estado del objeto para que este listo
        self.modelo = modelo
        self.marca = marca

   
celular = Celular("14 Pro Max", "Apple")
print(celular.modelo)



