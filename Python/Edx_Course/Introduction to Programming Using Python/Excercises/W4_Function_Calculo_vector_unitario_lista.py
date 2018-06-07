# Write a function that finds the magnitude of a given 3-dimensional vector. The magnitude of a vector is the square root of sum of squares of all the components of the vector.
# magnitude=\sqrt{x^2+y^2+z^2})
# Your input for this function will be a (vector with x,y,z components) a list containing 3 integers i.e, [x,y,z]. For example if the input list is:
# vector = [2, 3, -4]
# Then you should return the magnitude (as a floating point number) of this vector:
# 5.385164807134504
def magnitud_vector_unitario_lista(lista):
   for x in lista:
      if x == lista[0]:
         valor_x = x**2
      elif x == lista[1]:
         valor_y = x**2
      elif x == lista[2]:
         valor_z = x**2
   resultado = (valor_x + valor_y + valor_z) **(1/2)

   nueva_lista = []
   valor_x = lista[0]/resultado
   nueva_lista.append(valor_x)
   valor_y = lista[1]/resultado
   nueva_lista.append(valor_y)
   valor_z = lista[2]/resultado
   nueva_lista.append(valor_z)

   return nueva_lista

# Main Program #
lista = [2,3,-4]
evalua_magnitud_vector_unitario = magnitud_vector_unitario_lista(lista)
print(evalua_magnitud_vector_unitario)
