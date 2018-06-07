# Write a function which accepts an input list of numbers and returns the smallest number in the list (Do not use python's built-in min() function).
def numero_lista(lista):
   nueva_lista = lista[0]
   for x in lista:
      if x < nueva_lista :
         nueva_lista = x
   return nueva_lista

# Main Program #
lista = [98,16,4,10,2,3,4,5,9]
nueva_lista = numero_lista(lista)
print(nueva_lista)
