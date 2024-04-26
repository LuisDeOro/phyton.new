#ejercisio1
contraseña_uno = input("escribe una contraseña: solo letras")
texto = ("_______________________")
confirmacion = input("vuelva a introducir su contraseña: ")
if confirmacion==contraseña_uno:
    print("su contraseña es correcta")
else:
    print("su contraseña es incorrecta")
nombre = (input("cual es tu nombre: "))
sexo = (input("cual es tu sexo: femenino o masculino: "))
cadena = (nombre[0:1])
if (cadena<"m" and sexo==("femenino")) or (cadena>="m" and sexo ==("masculino") ):
    print("pertenece al grupo A")
else:
    print("pertenece al grupo B")
#ejercisio6
usuario= (input("¿Cual es tu nombre?  "))
edad = int(input("¿Que edad tienes? " ))
print("bienvenido ",usuario, "usted tiene ",edad,"años de edad.")
if edad<4:
    print("bienvenido ",usuario," puede entrar gratis a la sala")
elif edad >= 4 and edad <=18:
    print("bienvenido ",usuario," usted debe pagar 5€ ")
elif (edad >=18):
    print("bienvenido ",usuario," usted debe pagar 10€")
else:
    prin("ingrese un dato valido")
#ejercisio7
nombre2= (input("Cual es su nombre: "))
nombre2 = 0
while nombre2 <= 10:
    print(nombre2)
    nombre2 += 1
nombre2= (input("Cual es su nombre: "))
i =0
while i<=10:
    print(nombre2)
    i +=1
#ejercisio8
edad = int(input("cual es su edad: "))
i=1
while i<=edad:
    print(i, " años de edad")
    i+=1
#ejercisio9
numero = input("ingrese un numero entero")
#ejercisio11
numero_m = int(input("ingrese un numero a multiplicar: "))
for i in range(1,11):
    multiplicacion = i*numero_m
    print(numero_m, " x ", i, " = ",multiplicacion)
#ejercisio13
contraseña_uno = input("escribe una contraseña: solo letras: ")
texto = ("_______________________")
while True:
    confirmacion = input("vuelva a introducir su contrañesa: ")
    if confirmacion==contraseña_uno:
        print("contraseña correcta ")
        print("Acceso a todas las nenas de la zona:)")
        break

