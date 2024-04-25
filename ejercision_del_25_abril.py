#ejercisio2
ejercisio = "ejercisio 1"
inicio = "Bienvenid@"
nombre =(input("cual es su nombre: "))
print("Hola ",nombre," realizaremos una division: ")
numero_uno = int(input("ingrese el primer numero: "))
numero_dos = int(input("ingrese el segundo numero: "))
division = None
if numero_dos==0:
    print("error no se puede dividir con el numero 0")
else:
    division = (numero_uno/numero_dos)
    print("El resultado de la division es: ",numero_uno,"/",numero_dos,"=",division)
print("gracias")
#ejercisio3 escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numero = int(input("ingrese un numero: "))
if numero%2==0:
    print("el numero es par")
else:
    print("el numero es impar")
print("gracias")
#ejercisio4 
edad_usuario = int(input("ingrese su edad: "))
ingresos = int(input("ingrese sus ganancias: "))
if edad_usuario>=16 and ingresos>=1000:
    print("usted debe tributar")
else:
    print("usted no puede tributar")
print("gracias")
#ejercisio5
alumn = (input("ingrese un nombre: "))
sexo = (input("cual es su sexo"))
sub_cadena = alumn[0]
if sub_cadena==("a","b","c","d","e","f","g","h","i","j","k","l") and sexo ==("femenino"):
    print("pertenece a bucaramanda")
else:
    print("socio")
    