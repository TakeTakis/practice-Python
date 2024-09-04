"""
Parrte 1 - Ejercicio 1
Crea un array o arreglo unidimensional donde le 
indiques el tamaño por teclado y crear una función
que rellene el array o arreglo con los múltiplos
 de un número pedido por teclado. Por ejemplo, si
  defino un array de tamaño 5 y elijo un 3 en la 
  función, el array contendrá 3, 6, 9, 12, 15. 
  Muestralos por pantalla usando otra función distinta.

"""

arraycita = []
arraycitaleng = int(input("Ingese el tamanio del array-> "))
num = int(input("Ingese el multiplo que quiere mostrar-> "))

def funcioncita():
  for i in range(1,arraycitaleng+1):
    arraycita.append(i*num)

def mostrararray():
  for i in range(arraycitaleng):
    print(arraycita[i])

def mostrararray2():
    print(arraycita)


funcioncita()
mostrararray2()
