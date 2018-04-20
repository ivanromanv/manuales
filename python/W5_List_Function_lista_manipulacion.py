# List Manipulation Exercise 2 (Extending a List Without List Functions)
# 0 puntos posibles (no calificados)
# Write a function that accepts two lists A and B and returns a new list which contains all the elements of list A followed by elements of list B. Notice that the behaviour of this function is different from list.extend() method because the list.extend() method extends the list in place, but here you are asked to create a new list and return it. Your function should not return the original lists. For example if the input lists are:
#
# A = ['p', 'q', 6, 'k']
# B = [8, 10]
# Then your function should return a list such as:
# ['p', 'q', 6, 'k', 8, 10]
#
def funcion_lista_manipulacion_SinFunction(A, B):
   list_new=[]
   list_new=A+B
   return list_new
 
# OJO SOLO LA FUNCION!!!   
# Main Program #
A = ['p', 'q', 6, 'k']
B = [8, 10]
evalua_funcion_lista_manipulacion_SinFunction = funcion_lista_manipulacion_SinFunction(A, B)
print(evalua_funcion_lista_manipulacion_SinFunction)
