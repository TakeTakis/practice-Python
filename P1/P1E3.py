"""
Dado el siguiente arreglo de números:
[1, 5, 8, 3, 30, 9, 13]
Imprimir en pantalla programáticamente los números impares mayores a 3.
"""
#Array empienzan en 1 y no en 0, no como en java
A = [1, 5, 8, 3, 30, 9, 13]

for i in A:
    if i%2==1 and i>3:
         print (str(i) + " , ")

