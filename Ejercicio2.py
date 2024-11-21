print("Alvarez Delgado Yael Ismael, 1172, 3W")
print(" ")

# Creamos la clase
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        if not titular:
            raise ValueError("El titular es obligatorio.")
        self.titular = titular
        self.cantidad = cantidad
# Se muestra el titular y la cantidad
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")
# Verifica que la cantidad sea mayor que 0
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
# Definimos retirar la cantidad
    def retirar(self, cantidad):
        self.cantidad -= cantidad

# Cuenta del titular
cuenta = Cuenta("Lazito")
cuenta.mostrar()
# Se ingresan y se retiran cantidades a la cuenta
cuenta.ingresar(300)
cuenta.mostrar()

cuenta.retirar(100)
cuenta.mostrar()

cuenta.retirar(500) 
cuenta.mostrar()

print(" ")