#Declarar variables

A = [[1,2,3],
    [4,5],
    [6]]

B = [[0,0,0],
    [0,0],
    [0]]

matriz = [ ["","A","B","C"],
["A",2,5,1],
["B",6,5,1],
["C",8,7,9]    ]


#Suma de todos los elementos de una matriz
def sumaelemtos(A):
    sum = 0
    for i in A:
        for j in i:
            sum+=j
    
    return sum
# Res:
# print (sumaelemtos(A))

#Suma de los elementos de una fila de una matriz
def sumafila(A,n):
    sum=0
    for i in A[n]:
        sum+=i
    return sum

# Res:
# n = int(input("ingrese la fila n: "))
# print (sumafila(A,n))

#Suma de los elementos de una columna de una matriz
def sumaColumna(A,m):
    sum = 0
    #Cuantos arreglos tiene A
    for i in range(len(A)):
        try:
            sum+= A[i][m]
        except:
            pass
    return sum


# m = int(input("ingrese la columna m: "))
# print (sumaColumna(A,m))

#Indicador de si hay negativo en una matriz
def hayNega(A):
    x = False

    for i in A:
        for j in i:
            if j < 0:
                x = True

    if x:
        print("Si hay negativos")
    else:
        print("No hay negativos")

#hayNega(A)

#Fila con más ceros
def MasCeros(A):
    sum = 0
    max = 0
    MatrizAux = []
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[i])):
            if A[i][j] == 0:
                sum+=1
        MatrizAux.append(sum)
    
    print (MatrizAux)

    for k in range(len(MatrizAux)):
        if max < MatrizAux[k]:
            max = k

    print ("La fila con mas ceros es: " + str(max))
            
# MasCeros(A)

#La columna con mayor suma de una matriz
def mayor_col(A):
    max = 0
    sum = 0
    mayor_Colum=''
    for i in range(len(A[0])):
        sum = 0
        for j in range(len(A)):
            sum += A[j][i]
        if sum > max:
            max = sum
            mayor_Colum=A[0][i]
    return (mayor_Colum,max)

print (mayor_col(A))

        
