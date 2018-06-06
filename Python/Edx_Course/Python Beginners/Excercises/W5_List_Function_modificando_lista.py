# Write a function that accepts a list that contains positive integers and returns a new list which contains all the elements from original list but adds 1 to those elements which are odd. For example if :
#
# input_list = [12, 3, 4, 5, 6]
# Then your function should return a list such as:
# [12, 4, 4, 6, 6]
def funcion_lista_modificada(input_list):
   new_list=[]
   for numero in input_list:
      if numero%2==0:
         new_list.append(numero)
      else:
         new_list.append(numero+1)
   return new_list
 
# OJO SOLO LA FUNCION!!!
# Main Program #
input_list = [7, 6, 5, 4, 3, 2, 1]
evalua_funcion_lista_modificada = funcion_lista_modificada(input_list)
print(evalua_funcion_lista_modificada)
