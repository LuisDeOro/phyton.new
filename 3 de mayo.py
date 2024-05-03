def merge_Sort(arreglo):
    if len(arreglo)>1:
        mitad = len(arreglo)//2
        izquierda = arreglo[:mitad]
        derecha = arreglo[mitad:]
        merge_Sort(izquierda)
        merge_Sort(derecha)
        i = 0
        j = 0
        k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i]<derecha[j]:
                arreglo[k] = izquierda[i]
                i += 1
            else:
                arreglo[k]= derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            arreglo[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            arreglo[k] = derecha[j]
            j += 1
            k += 1
arreglo = [3,34,23,56,43,75,83,23,1,4]
print("el orden original es: ", arreglo)
merge_Sort(arreglo)
print("el orden con merge sort es: ", arreglo)
arreglo2= [3,2,4,2,5,67,6,9]
mitad2 = len(arreglo2)//2
print(mitad2)
izq = arreglo2[:mitad2]
print(izq)
der = arreglo2[mitad2:]
print(der)      
#rtienda
productos = {
    "menta": 300, "chocorramo":1000, "esfero":2700, "chocolatina": 2500
}
producto = (input("Que desea llevar: "))
cantidad = int(input("ingrese la cantidad: "))
if producto in productos:
    precio= producto[productos]*cantidad
    print("el precio total es: ", precio)
else:
    print("este producto no esta ")
    
