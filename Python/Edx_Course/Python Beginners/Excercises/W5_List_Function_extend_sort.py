# Write a function that accepts two lists both of which contain integers and returns a new list which contains all the elements from both lists sorted in descending order. Your new list should include duplicate elements if they exist. Do NOT use the built in sort() or sorted() methods.
#
def funcion_lista_sort_order_SinFunction(list_A, list_B):
   list_new=list_A+list_B
   for contador in range(len(list_new)-1,0,-1):
      for i in range(contador):
         # Cambiar > por < para mayor o menor
         if list_new[i]<list_new[i+1]:
            temp = list_new[i]
            list_new[i] = list_new[i+1]
            list_new[i+1] = temp   
   return list_new
 
# OJO SOLO LA FUNCION!!!
# Main Program #
list_A = [5,6,3,4,8,10,1,7,2,9]
list_B = [1,3,5,7,9,2,]
evalua_funcion_lista_sort_order_SinFunction = funcion_lista_sort_order_SinFunction(list_A, list_B)
print(evalua_funcion_lista_sort_order_SinFunction)
