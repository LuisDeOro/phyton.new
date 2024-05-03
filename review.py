#ejercisio 1
divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("ingrese una divisa: ")
if divisa in divisas:
    print("el simbolo de la ",divisa, "es ", divisas[divisa])
else:
    print("la divisa no está en el diccionario")
#ejercisio 2
usuario = {}
usuario ["nombre"]= input("ingrese su nombre: ")
usuario ["edad"]= input("ingrese su edad: ")
usuario ["direccion"]= input("ingrese su direccion: ")
usuario ["telefono"]= input("ingrese su telefono: ")
print("El señor(a)",usuario["nombre"], "tiene",usuario["edad"], "años y vive en la direccion", usuario["direccion"],"ademas su telefono es:",usuario ["telefono"])
#ejercisio 3


