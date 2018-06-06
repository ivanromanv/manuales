# Write a function that accepts a list of integers and returns the average. Assume that the input list contains only numbers. Do NOT use the built-in sum() function.
#
def funcion_promedio_lista(lista_entrada):
   numero=0
   suma=0
   resultado=0
   for x in lista_entrada:
      numero = numero + 1
      suma = suma + x
   promedio = suma / numero
   return int(promedio)

# OJO SOLO FUNCION!!!
# Main Program #
lista_entrada=[1,2,3,4,5]
evalua_funcion_promedio_lista = funcion_promedio_lista(lista_entrada)
print(evalua_funcion_promedio_lista)
