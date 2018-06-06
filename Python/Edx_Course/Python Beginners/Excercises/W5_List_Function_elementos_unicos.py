# Write a function that accepts two lists both of which consists of integers and returns the total sum of all the odd integers from both lists.
#
# Funcion recibe lista completa y elimina numeros repetidos
def funcion_lista_elementos_unicos(input_list):
   new_list=[]
   for i in input_list:
      if i not in new_list:
         new_list.append(i)
   return new_list
 
# OJO SOLO LA FUNCION!!!
# Main Program #
input_list = [2, 1, 7, 6, 5, 3, 4, 3, 2, 1]
evalua_funcion_lista_elementos_unicos = funcion_lista_elementos_unicos(input_list)
print(evalua_funcion_lista_elementos_unicos)
