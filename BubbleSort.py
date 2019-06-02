#Diego Moreno
#Victor Coeto
#Algoritmo obtenido de https://www.geeksforgeeks.org/python-program-for-bubble-sort/


def bubbleSort(a1):
    n = len(a1)

    # Pasamos por el arreglo n veces
    for i in range(n):
        for j in range(0, n-i-1):
            # Empezamos nuestro ciclo desde 0 hasta n-i-1
            #Usamos n-i-1 por que en cada iteración del ciclo anterior encontramos
            #el mayor número del arreglo y esto nos ayuda a no moverlo despues de que lo encontramos
            # Cambiamos los elementos si el anterior es mayor
            if a1[j] > a1[j+1] :
                a1[j], a1[j+1] = a1[j+1], a1[j]

lista=[]
a1=[]
data=input("Ingrese el arreglo\n")
lista=data.split(",")
a1=list(map(int,lista))
bubbleSort(a1)

print ("Arreglo ordenado: \n",a1)
