class InvertirPalabra():
    def pedirPalabra(self, palabra):
        self.palabra = palabra
        return palabra 

    
    def palabraInver(self):
        self.palabraInvertida = self.palabra[::-1]
        print(self.palabraInvertida)

palabra = InvertirPalabra()
palabra.pedirPalabra(input("Ingrese la palabra a invertir: "))
palabra.palabraInver()
