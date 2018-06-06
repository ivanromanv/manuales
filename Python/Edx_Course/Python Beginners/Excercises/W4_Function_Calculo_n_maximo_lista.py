# Write a function which accepts an input list of numbers and returns the largest number in the list (Do not use python's built-in max() function).
#
def funcion_n_maximo_lista(lista):
   nueva_lista = lista[0]
   for x in lista:
      if x > nueva_lista:
         nueva_lista = x
   return int(nueva_lista)

# OJO SOLO FUNCION!!!
# Main Program #
lista=[5,2,3,6,7,11,4,76]
evalua_funcion_n_maximo_lista = funcion_n_maximo_lista(lista)
print(evalua_funcion_n_maximo_lista)
