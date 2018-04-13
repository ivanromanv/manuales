# Write a function that accepts a positive integer k and returns the ascending sorted list of cube root values of all the numbers from 1 to k (including 1 and not including k). [if k is 1, your program should return an empty list]
#
def funcion_lista_raiz_cubica(number):
   import math
#   my_index=int(0)
#   contador=int(0)
   resultado_sqrt3=float(0)
   lista_sqrt3=[]
   for numero in range(1,number):
      resultado_sqrt3 = numero**(1/3)
      lista_sqrt3.append(resultado_sqrt3)
#      my_index = lista_sqrt.index(numero)
#   lista_sqrt.reverse()
   return lista_sqrt3
 
# OJO SOLO LA FUNCION!!!   
# Main Program #
number = int(input("Enter the number: "))
evalua_funcion_lista_raiz_cubica = funcion_lista_raiz_cubica(number)
print(evalua_funcion_lista_raiz_cubica)
