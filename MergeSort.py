# Diego Moreno
#Victor Coeto
#Algoritmo obtenido de https://www.geeksforgeeks.org/merge-sort/

def mergeSort(a1):
    if len(a1) >1:
        mid = len(a1)//2 #Buscamos la mitad del arreglo
        L = a1[:mid] # Dividimos el arreglo
        R = a1[mid:]
        mergeSort(L) # Ordenamos la primera mitad
        mergeSort(R) # Ordenamos la segunda mitad
        i = j = k = 0
        #Usamos los arreglos L y R para copiar los datos y despues unirlos en el arreglo a1
        #en el orden adecuado
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a1[k] = L[i]
                i+=1
            else:
                a1[k] = R[j]
                j+=1
            k+=1
        #Verificamos si falta algun arreglo por combinar
        while i < len(L):
            a1[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            a1[k] = R[j]
            j+=1
            k+=1
if __name__ == '__main__':
    lista=[]
    a1=[]
    data=input("Ingresa el arreglo")
    lista=data.split(",")
    a1=list(map(int,lista))
    mergeSort(a1)
    print("Arreglo ordenado: \n",a1)
