# Write a function that accepts two positive integers a and b and returns a list of all the even numbers between a and b (including a and not including b).
#
def funcion_lista_numeros_pares(number_one, number_two):
   my_index=int(0)
   contador=int(0)
   lista_pares=[]
   for numero in range(number_one,number_two+1):
      if lista_pares==[]:
         lista_pares.append(number_one)
      elif numero%2 == 0:
         contador=contador+1
         lista_pares.append(numero)
         my_index = lista_pares.index(numero)
   if contador==my_index:
      lista_pares.pop(my_index)
   return lista_pares
 
# OJO SOLO LA FUNCION!!!   
# Main Program #
number_one = int(input("Enter the firts number: "))
number_two = int(input("Enter the second number: "))

evalua_funcion_lista_numeros_pares = funcion_lista_numeros_pares(number_one, number_two)
print(evalua_funcion_lista_numeros_pares)
