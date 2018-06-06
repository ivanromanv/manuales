#  Write a function named unique_common that accepts two lists both of which contain integers as parameters and returns a sorted list (ascending order) which contains unique common elements from both the lists. If there are no common elements between the two lists, then your function should return the keyword None
#
# For example, if two of the lists received by the function are:
#
# ([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7])
#
# You can see that elements 5, -7, and 8 are common in both the first list and the second list and that the element 8 occurs twice in both lists. Now you should return a sorted list (ascending order) of unique common elements like this:
#
# [-7, 5, 8]
#
# if the two lists received by the function are:
#
# ([5, 6, 7, 0], [3, 2, 3, 2])
#
# Since, there are no common elements between the two lists, your function should return the keyword
#
#None
#
# compara los elementos entre a y b
def unique_common(a, b):
   lista_extendida=[]
   for x in a:
      if x in b:
         lista_extendida.append(x)
   evalua_funcion_lista_depurada = funcion_lista_depurada(lista_extendida)
   if evalua_funcion_lista_depurada!=[]:
      return evalua_funcion_lista_depurada

# Funcion recibe lista completa y elimina numeros repetidos
def funcion_lista_depurada(lista_extendida):
   lista_final = []
   for i in lista_extendida:
      if i not in lista_final:
         lista_final.append(i)
         lista_final.sort()
   registros = int(len(lista_final))  
   #return lista_final, registros
   return lista_final
         
# OJO SOLO LA FUNCION!!!
# Main Program #
a = [1,2,3,4,5,6,5,7,8,9,-1]
b = [4,9,10,12,-1,5,13,1]
evalua_unique_common  = unique_common(a, b) 
print(evalua_unique_common)
