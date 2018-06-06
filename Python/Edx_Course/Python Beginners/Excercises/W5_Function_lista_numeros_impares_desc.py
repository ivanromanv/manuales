# Write a function that accepts two positive integers a and b (a is smaller than b)and returns a list that contains all the odd numbers between a and b (including a and including b if applicable) in descending order.
#
def funcion_lista_numeros_impares_desc(number_one, number_two):
   my_index=int(0)
   contador=int(0)
   lista_impares=[]
   for numero in range(number_one,number_two+1):
      if numero%2 != 0:
         contador=contador+2
         lista_impares.append(numero)
         my_index = lista_impares.index(numero)
   lista_impares.reverse()
   return lista_impares
 
# OJO SOLO LA FUNCION!!!   
# Main Program #
number_one = int(input("Enter the firts number: "))
number_two = int(input("Enter the second number: "))
evalua_funcion_lista_numeros_impares_desc = funcion_lista_numeros_impares_desc(number_one, number_two)
print(evalua_funcion_lista_numeros_impares_desc)
