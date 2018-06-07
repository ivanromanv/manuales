# Write a function which accepts an input list of numbers and returns a list which includes only the even numbers in the input list. If there are no even numbers in the input numbers then your function should return an empty list.
def suma_lista(lista):
   contador = 0
   nueva_lista = []
   for x in lista:
      entero = x%2
      if entero == 0:
         nueva_lista.extend([x])
         contador = contador + 1
         if contador == 0:
            nueva_lista = []
   return nueva_lista

# Main Program #
lista = [1,2,3,4,5,9]
nueva_lista = suma_lista(lista)
print(nueva_lista)
