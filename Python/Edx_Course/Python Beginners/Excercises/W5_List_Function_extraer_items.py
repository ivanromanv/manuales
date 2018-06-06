# Write a function that accepts a list and return a new list which contains all but the first and last elements of the original list.
#
def funcion_lista_count_item_SinFunction(list_item):
   end_list=(len(list_item)-1)
   list_new=list_item[1:end_list]
   return list_new
 
# OJO SOLO LA FUNCION!!!
# Main Program #
list_item = ['hola', 7, 6, 5, 4, 3, 2, 1,'hola',0]
evalua_funcion_lista_count_item_SinFunction = funcion_lista_count_item_SinFunction(list_item)
print(evalua_funcion_lista_count_item_SinFunction)
