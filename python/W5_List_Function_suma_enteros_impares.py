# Write a function that accepts two lists both of which consists of integers and returns the total sum of all the odd integers from both lists.
#
def funcion_lista_suma_enteros_impares(list_A, list_B):
   new_list=list_A+list_B
   suma=0
   for numero in new_list:
      if numero%2!=0:
         suma = suma + numero
   return suma
 
# OJO SOLO LA FUNCION!!!
# Main Program #
list_A = [7, 6, 5, 4, 3, 2, 1]
list_B = [1, 6, 9, 7, 3, 2, 11]
evalua_funcion_lista_suma_enteros_impares = funcion_lista_suma_enteros_impares(list_A, list_B)
print(evalua_funcion_lista_suma_enteros_impares)
