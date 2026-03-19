"""
Ejercicio 4: Control de Computadores de Mantenimiento

Un centro de soporte técnico necesita controlar los computadores que
ingresan a revisión y calcular el valor del diagnóstico según el tiempo.

Crear la clase ComputadorMantenimiento, con:
    - Atributos privados: _codigo, _hora_entrada, _valor_hora.
    - Método registrar_entrada(hora)
    - Método registrar_salida(hora)
    - Método calcular_valor(hora_salida)
    - Método obtener_codigo()

    La aplicación debe:
    - Registrar computadores en mantenimiento
    - Guardarlos en una lista interna
    - Seleccionar un computador para registrar su salida
    - Calcular y mostrar el costo total
    - Validar correctamente las horas
"""

# Tkinter es la librería que permite crear interfaces gráficas en Python.
# messagebox es un módulo dentro de Tkinter que muestra ventanas emergentes de aviso.
import tkinter as tk
from tkinter import messagebox


class Usuario:
    # Esta clase representa al usuario del sistema.
    # Guarda las credenciales de acceso y valida que sean correctas.

    def __init__(self):
        # Los atributos se declaran con doble guión bajo para hacerlos privados.
        # Privado significa que no se pueden leer ni modificar desde fuera de la clase.
        self.__usuario = "programacion"
        self.__password = "programacion"

    def validar(self, usuario_ingresado, password_ingresada):
        # Recibe lo que el usuario escribió en el login y lo compara con las credenciales guardadas.
        # Retorna True si ambos coinciden, False si alguno es incorrecto.
        return usuario_ingresado == self.__usuario and password_ingresada == self.__password


class Login:
    # Esta clase construye la ventana de inicio de sesión.
    # Es la primera pantalla que ve el usuario al ejecutar el programa.

    def __init__(self, ventana):
        # Recibe la ventana principal como parámetro y la configura.
        self.ventana = ventana
        self.ventana.title("Login")
        self.ventana.geometry("350x300")

        # Se crea una instancia de Usuario para usarla en la validación.
        self.usuario = Usuario()

        # Label muestra texto en pantalla. Entry es la caja donde el usuario escribe.
        # pack() coloca cada widget uno debajo del otro. pady agrega espacio vertical.
        tk.Label(ventana, text="User:").pack(anchor="center", pady=(20, 5))
        self.entry_usuario = tk.Entry(ventana)
        self.entry_usuario.pack(anchor="center", pady=8)

        # show="*" hace que cada carácter se muestre como asterisco, ocultando la contraseña.
        tk.Label(ventana, text="Password").pack(anchor="center", pady=(20, 5))
        self.entry_password = tk.Entry(ventana, show="*")
        self.entry_password.pack(anchor="center", pady=8)

        # El parámetro command le dice a Tkinter qué método ejecutar cuando se haga clic en el botón.
        tk.Button(ventana, text="Log in", command=self.validar).pack(anchor="center", pady=15)

    def validar(self):
        # Lee lo que el usuario escribió en cada campo con .get().
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        # Delega la validación a la clase Usuario.
        # Si las credenciales son correctas, abre la ventana del sistema principal.
        # Si son incorrectas, muestra un mensaje de error.
        if self.usuario.validar(usuario, password):
            messagebox.showinfo("Acceso", "Welcome to system")
            # Toplevel abre una ventana secundaria encima de la actual.
            ingreso_ventana = tk.Toplevel(self.ventana, class_="VTk")
            Ingreso(ingreso_ventana)
        else:
            messagebox.showerror("Error", "User or password incorrect")


class ComputadorMantenimiento:
    # Esta clase representa un computador que ingresa a mantenimiento.
    # Guarda su código, las horas de entrada y salida, y el valor por hora del servicio.

    def __init__(self, codigo):
        # Atributos privados del computador.
        # __hora_entrada y __hora_salida inician en None porque aún no se conocen al crear el objeto.
        # Se asignan después mediante los métodos registrar_entrada y registrar_salida.
        self.__codigo = codigo
        self.__hora_entrada = None
        self.__hora_salida = None
        self.__valor_hora = 5000

    def registrar_entrada(self, hora):
        # Guarda la hora en que el computador ingresó a mantenimiento.
        self.__hora_entrada = hora

    def registrar_salida(self, hora):
        # Guarda la hora en que el computador salió de mantenimiento.
        self.__hora_salida = hora

    def calcular_valor(self):
        # Calcula el costo total del servicio multiplicando las horas trabajadas por el valor por hora.
        # abs() garantiza que el resultado sea positivo sin importar el orden de las horas.
        # Si alguna de las horas no ha sido registrada, retorna un mensaje de aviso.
        if self.__hora_salida is not None and self.__hora_entrada is not None:
            return abs((self.__hora_salida - self.__hora_entrada) * self.__valor_hora)
        else:
            return "Enter an entry time and an exit time"

    def obtener_codigo(self):
        # Retorna el código del computador.
        # Al ser __codigo privado, este método es la única forma de consultarlo desde fuera.
        return self.__codigo

    def obtener_codigo_entrada(self):
        # Retorna la hora de entrada registrada del computador.
        return self.__hora_entrada

    def obtener_codigo_salida(self):
        # Retorna la hora de salida registrada del computador.
        return self.__hora_salida


class Ingreso:
    # Esta clase construye la ventana principal del sistema de mantenimiento.
    # Permite registrar computadores, asignarles horas y calcular el costo del servicio.

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Enter computer")

        # Lista interna donde se guardan todos los objetos ComputadorMantenimiento registrados.
        self.lista_computadores = []

        # Campo para ingresar el código del computador.
        tk.Label(ventana, text="Code computer:").pack()
        self.entry_codigo = tk.Entry(ventana)
        self.entry_codigo.pack()

        # Botón que llama al método registro al hacer clic.
        tk.Button(ventana, text="Enter", command=self.registro).pack()

        # Listbox muestra los códigos de los computadores registrados.
        # Al hacer clic en uno, se activa el evento ListboxSelect que llama a al_seleccionar.
        tk.Label(ventana, text="Registered computers:").pack()
        self.listbox = tk.Listbox(ventana)
        self.listbox.bind("<<ListboxSelect>>", self.al_seleccionar)
        self.listbox.pack()

        # Spinbox permite elegir la hora de entrada con flechas, limitado entre 0 y 23.
        tk.Label(ventana, text="Check-in time:").pack()
        self.entry_hora_entrada = tk.Spinbox(ventana, from_=0, to=23)
        self.entry_hora_entrada.pack()

        tk.Button(ventana, text="Check", command=self.registroE).pack()

        # Spinbox para la hora de salida, con el mismo rango de 0 a 23.
        tk.Label(ventana, text="Departure time:").pack()
        self.entry_hora_salida = tk.Spinbox(ventana, from_=0, to=23)
        self.entry_hora_salida.pack()

        tk.Button(ventana, text="Departure", command=self.registroS).pack()

        tk.Button(ventana, text="Calculate value", command=self.calcular_valor).pack()

    def registro(self):
        # Lee el código escrito por el usuario.
        # Valida que el campo no esté vacío antes de continuar.
        # Crea un objeto ComputadorMantenimiento, lo agrega a la lista interna
        # y muestra su código en la Listbox. Luego limpia el campo de texto.
        codigo = self.entry_codigo.get()
        
        if not codigo:
            messagebox.showerror("Error", "Enter a computer code")
            return
        computador = ComputadorMantenimiento(codigo)
        self.lista_computadores.append(computador)
        self.listbox.insert(tk.END, codigo)
        self.entry_codigo.delete(0, tk.END)

    def registroE(self):
        # Registra la hora de entrada del computador seleccionado en la Listbox.
        # curselection() retorna el índice del elemento seleccionado.
        # Si no hay selección, muestra un aviso. Si la hora no es número, captura el error.
        try:
            indice = self.listbox.curselection()
            
            if not indice:
                messagebox.showerror("Error", "Select a computer from the list")
            
            else:
                computador = self.lista_computadores[indice[0]]
                entrada_registro = int(self.entry_hora_entrada.get())
                computador.registrar_entrada(entrada_registro)
        
        except ValueError:
            messagebox.showerror("Error", "Times must be numbers")

    def registroS(self):
        # Registra la hora de salida del computador seleccionado en la Listbox.
        # Sigue el mismo patrón que registroE pero para la hora de salida.
        try:
            indice = self.listbox.curselection()
            
            if not indice:
                messagebox.showerror("Error", "Select a computer from the list")
            
            else:
                computador = self.lista_computadores[indice[0]]
                salida_registro = int(self.entry_hora_salida.get())
                computador.registrar_salida(salida_registro)
        except:
            messagebox.showerror("Error", "Times must be numbers")

    def calcular_valor(self):
        # Calcula y muestra el costo total del computador seleccionado.
        # Primero verifica que haya computadores en la lista.
        # Luego verifica que haya uno seleccionado en la Listbox.
        # El resultado se formatea con puntos como separador de miles.
        
        if not self.lista_computadores:
            messagebox.showerror("Error", "No computers registered")
        
        else:
            indice = self.listbox.curselection()
            
            if not indice:
                messagebox.showerror("Error", "Select a computer from the list")
            
            else:
                computador = self.lista_computadores[indice[0]]
                resultado = computador.calcular_valor()
                messagebox.showinfo("Total cost", f"{resultado:,}".replace(",", "."))

    def al_seleccionar(self, event):
        # Se ejecuta automáticamente cuando el usuario hace clic en un elemento de la Listbox.
        # Obtiene el computador correspondiente y actualiza los Spinbox con sus horas guardadas.
        # Si una hora aún no fue registrada, muestra 0 por defecto.
        indice = self.listbox.curselection()
        
        computador = self.lista_computadores[indice[0]]
        self.entry_hora_entrada.delete(0, tk.END)
        self.entry_hora_entrada.insert(0, str(computador.obtener_codigo_entrada() or 0))
        
        self.entry_hora_salida.delete(0, tk.END)
        self.entry_hora_salida.insert(0, str(computador.obtener_codigo_salida() or 0))



# Punto de entrada del programa
# tk.Tk() crea la ventana principal. Login la configura con sus widgets
# mainloop() mantiene la ventana abierta esperando eventos 

ventana = tk.Tk(className="VTk")
Login(ventana)
ventana.mainloop()





