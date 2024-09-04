"""
Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente 
sin usar la función (min) y escriba en pantalla. 
Luego programáticamente calcule el promedio de notas 
descontando la nota eliminada.
"""


A = [20, 15, 12, 11, 8, 1, 4]
var  = A[1]
acum = 0


for i in A:
    if i<var:
        var = i

A.remove(var)



for i in A:
    acum+=i

print ("El promedio mas bajo es: "+ str(var))
print (A)
print (acum)
print ("Prom = "+str(acum/len(A)))

