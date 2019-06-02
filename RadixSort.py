#   Diego Moreno
#   Victor Coeto

#codigo de la pagina: https://www.geeksforgeeks.org/radix-sort/

def countingSort(a1, exp1):
    n = len(a1)
    output = [0] * (n) #elementos que tendra ordenados a1
    count = [0] * (10) # se inicializa en 0 por la base que es 10

    for i in range(0, n):#se inicializa el arreglo countingSort para poder sumarlo
        index = (a1[i]//exp1) #hace que se tenga el indice a partir de la division exp1
        count[ (index)%10 ] += 1 #se toma que la posicion de count tenga la posicion actual del digito en el arreglo output base 10

    for i in range(1,10):#se suman los valores para sacar los indices en los que se va a acomodar el arreglo a1
        count[i] += count[i-1]#se crea el arreglo count a partir de las veces que tiene algun numero del 0-9
    i = n-1
    while i>=0:
        index = (a1[i]//exp1)
        output[ count[ (index)%10 ] - 1] = a1[i]#se copia en arreglo a1 a output para que esten ordenados
        count[ (index)%10 ] -= 1
        i -= 1
    i = 0

    for i in range(0,len(a1)): # se toma el arreglo output para saber la ubicacion del inidce en el arreglo a1 a traves de el countingSort
        a1[i] = output[i]#se termina de asignar a a1

def radixSort(a1):
    max1 = max(a1) #encuentra el numero con la maxima cantidad de digitos
    exp = 1
    while max1//exp > 0: #se hace un floor para mantener la cantidad en enteros
        countingSort(a1,exp)# el metodo countingSort se hace para cada digito se acomode a traves de sumas y lo pueda arregla dentro de radixSort
        exp *= 10
lista=[]
a1=[]
data=input("ingresa el arreglo")
lista=data.split(",")
a1=list(map(int,lista))
radixSort(a1)
print("arreglo ordenado",a1)
