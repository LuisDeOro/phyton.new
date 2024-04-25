#operaciones aritmeticas
inicio = "bienvenidos"
nombre = input(" cual es tu nombre: ")
print("´Hola ",nombre," realizaremos una suma`")
numero_uno = int(input("escribe el primer numero: "))
numero_dos = int(input("escribe el segundo numero: "))
resultado = (numero_uno+numero_dos)
print("el resultado de la suma es: ",numero_uno,"+",numero_dos,"=",resultado)
if resultado<23:
    print("no sirve")
print("si sirve")   
#meses del año
meses = str(input("ingrese el mes que quieres: de (enero, febrero, marzo, abril, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre): "))
if meses ==("enero"):
    print("este mes tiene 31 dias")
elif meses ==("febrero"):
    print("este mes tiene 29 dias")
elif meses ==("marzo"):
    print("este mes tiene 31 dias")
elif meses ==("abril"):
    print("este mes tiene 30 dias")
elif meses ==("mayo"):
    print("este mes tiene 31 dias")
elif meses ==("junio"):
    print("este mes tiene 31 dias")
elif meses ==("julio"):
    print("este mes tiene 31 dias")
elif meses ==("agosto"):
    print("este mes tiene 31 dias")
elif meses ==("septiembre"):
    print("este mes tiene 30 dias")
elif meses ==("octubre"):
    print("este mes tiene 31 dias")
elif meses ==("noviembre"):
    print("este mes tiene 30 dias")
elif meses ==("diciembre"):
    print("este mes tiene 31 dias")
else:
    print("ingrese un valor valido")
print("gracias socio")
#bucle while
#bucle for