# Crear una cuenta bancaria

import os 

# Requerimos de dos clases una para crear al clinete y otra que cuente con los balances de la cuenta
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Se crea una segunda clase donde heredamos de persona
class Cliente(Persona):

    def __init__(self, nombre, apellido, no_cuenta, balance = 0): # Declaramos 0 al balance, siempre empiezan vacias las cuentas
        super().__init__(nombre, apellido)
        self.no_cuenta = no_cuenta
        self.balance = balance

    # Se muestra el balance de la cuenta y datos del cliente
    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nCuenta: {self.no_cuenta}\nSaldo: ${self.balance}'

    # Metodo para ingresar la cantidad a depositar
    def depositar(self, total_deposito):
        self.balance += total_deposito
        print(f"Deposito aceptado")

    # Creamos funcion para retirar dinero
    def retirar(self, total_retiro):
        # Aceptar retiro si tiene fondos
        if self.balance >= total_retiro:
            self.balance -= total_retiro
            print("¡Retiro exitoso!")
        # No cuentas con fondos
        else:
            print("¡Saldo insufucente!")


# Creamos una funcion para crear al cliente
def crear_cliente():
    os.system('cls')
    nombre_cliente = input("Ingresa tu nombre: ")
    apellido_cl = input("Ingresa tu apellido: ")
    no_cuenta = int(input("Ingresa tu numero de cuenta: "))

    cliente = Cliente(nombre_cliente, apellido_cl, no_cuenta)
    return cliente


def inicio():

    mi_cliente = crear_cliente()
    print(mi_cliente) # Muestra lo que tenemos dentro de la clase Cliente
    
    opcion = 0

    while opcion != 'S':
        print("")
        print('Menu:\n(D) - Depositar \n(R) - Retirar \n(S) - Salir')
        opcion = input()
        os.system('cls')

        if opcion == 'D':
            monto_deposito = float(input("Monto a depositar: "))
            mi_cliente.depositar(monto_deposito)
        elif opcion == 'R':
            monto_retirar = float(input("Monto a retirar: "))
            mi_cliente.retirar(monto_retirar)
        print(mi_cliente)

    print("::: Gracias por operar en banco Python :::")

inicio()