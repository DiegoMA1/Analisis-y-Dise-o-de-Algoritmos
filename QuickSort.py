#codigo de la pagina web: https://www.geeksforgeeks.org/quick-sort/

# el codigo toma el pivote directamente del final del arreglo y compara los numeros
#el metodo partition es para checar cual sera el siguiente pivote al comparar el nu. izquierdo y num. derecho
#los menores los situa del lado izquierdo y los mayores del derecho
def partition(a1,low,high): # a1 es el arreglo, low es el indice mas bajo y high el mas alto
    i = ( low-1 )#indice del elemento mas pequeño
    pivot = a1[high]# asigna el pivote
    for j in range(low , high):
        if   a1[j] <= pivot: #if para saber si el elemento a comprobar es <= al pivote
            i = i+1 #incrementa el indice para el numero izquierdo
            a1[i],a1[j] = a1[j],a1[i]#ai[i] = num. izquierdo, a[j] = num. derecha
    a1[i+1],a1[high] = a1[high],a1[i+1]
    return ( i+1 )

def quickSort(a1,low,high):
    if low < high:
        pi = partition(a1,low,high)
        quickSort(a1, low, pi-1) #para checar num.derecha
        quickSort(a1, pi+1, high) #para checar num. izquierda

lista=[]
a1=[]
data=input("Ingresa arreglo: \n")
lista=data.split(",")
a1=list(map(int,lista))
n = len(a1)
quickSort(a1,0,n-1)
print ("arreglo ordenado: \n", a1)
