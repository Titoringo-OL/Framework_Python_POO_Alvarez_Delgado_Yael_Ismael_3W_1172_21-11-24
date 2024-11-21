print("Alvarez Delgado Yael Ismael, 1172, 3W")
print(" ")

# Creamos la clase
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad
# Definimos ingresar
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
# Definimos retirar
    def retirar(self, cantidad):
        self.cantidad -= cantidad
# Definimos mostrar
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

# Creamos la clase para una cuenta joven
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
# Verifica que el titular se encuentre en la edad correcta
    def esTitularValido(self):
        return 18 <= self.cantidad < 25
# Si no se encuentra en la edad el titular no sera valido
    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero: el titular ya esta viejito.")
# Muestra todos los datos
    def mostrar(self):
        print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")

# Cuenta del titular
cuenta_joven = CuentaJoven("Lazito", cantidad=20, bonificacion=10)
cuenta_joven.mostrar()
# Se ingresan y se retiran cantidades en la cuenta
cuenta_joven.ingresar(100)
cuenta_joven.mostrar()

cuenta_joven.retirar(50)
cuenta_joven.mostrar()

cuenta_joven.cantidad = 30  
cuenta_joven.retirar(50)

print(" ")