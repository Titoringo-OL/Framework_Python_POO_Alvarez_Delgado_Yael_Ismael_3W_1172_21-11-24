print("Alvarez Delgado Yael Ismael, 1172, 3W")
print(" ")

# Creamos la clase
class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
# Muestra los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad >= 18
# Mostramos todos los datos en pantalla
persona = Persona("Lazito", 25, "12345678A")
persona.mostrar()
print("Es mayor de edad:", persona.esMayorDeEdad())

print(" ")