
class CajeroAutomatico:
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
        print("Opción no válida. Por favor, seleccione una opción válida.") 

#Verificar si un número es primo
def primo (num):
    contador = 2
    resultado = True     
    while (contador <= num/2 and resultado):         
        resultado = num % contador != 0
        contador+= 1
    return resultado
#Verificar si un número es par o impar
def par (num):
    return num%2==0
#Obtener la media de una serie de números
def media(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma/len(lista)

def generar_lista():
    cantidad = (int(input("Ingrese cuantos valores desea ingresar: ")))
    lista =[]
    for i in range(cantidad):
        lista.append(int(input("Ingrese el valor: ")))
    return lista
#Verificar si una palabra contiene la letra x o z
def palabra ():
    palabra = (input("ingrese una palabra: "))
    
    return palabra.count ("x") != 0 or palabra.count ("z") != 0
    
continuar="si"
while continuar=="si":
    operacion=str(input("ingresa el proceso que deseas realizar (primo) (par) (media) (palabra)"))
    if operacion=="primo":
        print(primo(int(input("Ingrese el número: "))))
    elif operacion=="par":
        print(par(int(input("Ingrese el número: "))))
    elif operacion=="media":
        print(media(generar_lista()))
    elif operacion=="palabra":
        print(palabra())
    else:   
       print("ingreso una operacion no valida")
    continuar=str(input("Deseas repetir el proceso? Ingresa (no) para cerrar el ciclo y (si) para repetir el proceso "))
#loteria
import random
numeros_loteria = set()
while len(numeros_loteria)<=0:
    numero = random.randint(2,31)
    numeros_loteria.add(numero)
usuario = int(input("ingrese un numero del 2 al 31: "))
if numeros_loteria == usuario:
    print ("usted gano con el numero", usuario)
    print("el numero ganador es: ", numeros_loteria)
else:
    print("Yaper")
    print("el numero ganador es: ", numeros_loteria)
    
