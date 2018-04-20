# Write a function that accepts two input lists and returns a new list which contains only the unique elements from both lists.
#
# Funcion recibe lista completa y elimina numeros repetidos
def funcion_lista_elementos_reversa(input_list):
   lista=(len(input_list)+3)
   new_list=input_list[-1:-lista:-1]
   return new_list
 
# OJO SOLO LA FUNCION!!!
# Main Program #
input_list = [ 5, 4, 3, 2, 1]
evalua_funcion_lista_elementos_reversa = funcion_lista_elementos_reversa(input_list)
print(evalua_funcion_lista_elementos_reversa)
