# Write a function that accepts two lists both of which contain integers and returns a new list which contains all the elements from both lists sorted in descending order. Your new list should include duplicate elements if they exist. Do NOT use the built in sort() or sorted() methods.
#
def funcion_lista_count_item_SinFunction(list_item, item):
   contador=0
   for numero in list_item:
      if numero==item:
         contador=contador+1
   return contador
 
# OJO SOLO LA FUNCION!!!
# Main Program #
list_item = [10, 9, 9, 'hola', 7, 7, 3, 6, 5, 5, 4, 3, 3, 2, 2, 1, 1,'hola',7]
item = 7
evalua_funcion_lista_count_item_SinFunction = funcion_lista_count_item_SinFunction(list_item, item)
print(evalua_funcion_lista_count_item_SinFunction)
