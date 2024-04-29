#lista
def busqueda_bina(lista,valor):
    izquierda = 0
    derecha =len(lista) - 1
    while izquierda<=derecha:
        medio =(izquierda + derecha) //2
        if lista[medio] ==valor:
            return medio
        elif lista [medio]<valor:
            izquierda=medio+1
        else:
            derecha = medio -1
    return -1
lista = [2,3,5,6,7,8,22,34,56,67]
valor_buscar = 56
resultado = busqueda_bina(lista, valor_buscar)
if resultado!= -1:
    print("el valor: ", valor_buscar,"fue encontrado en la posicion: ", resultado)
else:
    "SAL"
#METODO BISECT
import bisect
lista = [2,3,5,6,7,8,22,34,56,67]
resultado = bisect.bisect_left(lista, 56)
#numero n primo o no
def es_primo(num):
    for n in range(2, num):
        if num%n==0:
            return False
    return True
print(es_primo(6))
#append para agregar un elemento a la lista
#extend para agregar una lista de otra
#insert para insertar un elemento en una lista sirve para reemplazar insert(indice,elemento a dar)
#remove para eliminar dandole el valor y no el indice(x)
#clear elimina todo
#count para contar elementos de lista repetibles
#sort para ordenar listas
#ordenar de forma descendente
listas= sorted([2,4,3,7,32,8,65,8,9],reverse=True)
print(listas)
#ordenar de forma ascendente
listas=[2,4,3,7,32,8,65,8,9]
listas.sort()
print(listas)
#in para saber si un elemento esta en lista
print(3 in listas)
#la funcion len muestra la cantidad de datos que hay en la lista
print(len(listas))


    
            