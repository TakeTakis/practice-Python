"""
Crea dos arrays o arreglos unidimensional 
es que tengan el mismo tamaño 
(lo pedirá por teclado), en uno de ellos 
almacenarás nombres de personas como 
cadenas, en el otro array o arreglo ira 
almacenando la longitud de los nombres.
"""

tam = int(input("dame el tamanio-> "))
A = [] 
B = [] 

def RellenarNom():
    for i in range (tam):
        A.append(input("pon un nombre"))

def RellenarLengs():
    for i in range (tam):
        B.append(len(A[i]))


RellenarNom()
RellenarLengs()

print (A)
print (B)