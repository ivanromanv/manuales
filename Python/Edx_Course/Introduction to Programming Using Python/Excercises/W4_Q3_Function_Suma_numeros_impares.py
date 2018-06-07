# Write a function that accepts a list of integers as parameter. Your function should return the sum of all the odd numbers in the list. If there are no odd numbers in the list, your function should return 0 as the sum. 
#
# Remember that you are not asked to print anything. So, your function should just return the sum of all the odd numbers in the list. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.
#
def funcion_suma_numeros_impares_lista(lista):
   suma=int(0)
   for x in lista:
      if x%2 != 0:
         suma = suma + x
   return suma

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [2,4,6]
evalua_funcion_suma_numeros_impares_lista = funcion_suma_numeros_impares_lista(lista)
print(evalua_funcion_suma_numeros_impares_lista)
