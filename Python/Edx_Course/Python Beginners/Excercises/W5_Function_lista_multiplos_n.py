# Write a function that accepts a positive integer k and returns a list that contains the first five multiples of k. The multiples should be calculated starting from 1 to 5 (including both 1 and 5). For example the first five multiples of 3 are 3, 6, 9, 12, and 15
#
def funcion_lista_multiplos_n(number):
   lista_multiplos=[]
   contador = number*5
   for numero in range(number,contador+1,number):
      lista_multiplos.append(int(numero))
   return lista_multiplos
 
# OJO SOLO LA FUNCION!!!   
# Main Program #
number = int(input("Enter the number: "))
evalua_funcion_lista_multiplos_n = funcion_lista_multiplos_n(number)
print(evalua_funcion_lista_multiplos_n)
