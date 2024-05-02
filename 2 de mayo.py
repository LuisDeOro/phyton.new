
""" class CajeroAutomatico:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Depósito de", cantidad, "realizado.")
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print("Retiro de", cantidad, "realizado.")
        else:
            print("Saldo insuficiente.")
    
    def consultar_saldo(self):
        print("Su saldo actual es:", self.saldo)

# Crear una instancia del cajero con un saldo inicial de 1000
cajero = CajeroAutomatico(1000)

# Menú de opciones
while True:
    print("\n1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        cajero.consultar_saldo()
    elif opcion == '2':
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cajero.depositar(cantidad)
    elif opcion == '3':
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cajero.retirar(cantidad)
    elif opcion == '4':
        print("¡Gracias por utilizar nuestro cajero!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.") """
#clase 2 de mayo
