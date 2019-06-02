#Diego Moreno
#Victor Coeto
#Algoritmo obtenido de https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort

def intercambio(i, j):
    a1[i], a1[j] = a1[j], a1[i]

def heapify(end,i):
    #Usamos l para almacenar
    l=2 * i + 1 #Calculamos el indice del elemento izquierdo
    r=2 * i + 2 #Calculamos el indice del elemento derecho
    max=i
    if l < end and a1[i] < a1[l]: #Verificamos si el nodo izquierdo es mayor
        max = l #Si es mayor, guardamos el indice en donde se encuentra
    if r < end and a1[max] < a1[r]: #Verificamos si el nodo derecho es mayor
        max = r #Si es mayor, guardamos el indice en donde se encuentra
    if max != i: #Si el indice guardado es diferente al indice de la raiz, entonces hacemos el intercambio
        intercambio(i, max)
        heapify(end, max) #Despues de hacer el intercambio, volvemos a heapify el arreglo

def heap_sort(a1):
    end = len(a1)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        intercambio(i, 0)
        heapify(i, 0)

lista=[]
a1=[]
data=input("Input the array\n")
lista=data.split(",")
a1=list(map(int,lista))
heap_sort(a1)
print ("Arreglo ordenado: \n", a1)
