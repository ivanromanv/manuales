#  Write a function named unique_common that accepts two lists both of which contain integers as parameters and returns a sorted list (ascending order) which contains unique common elements from both the lists. If there are no common elements between the two lists, then your function should return the keyword None
#
# For example, if two of the lists received by the function are:
#
#  Write a function named find_gcd that accepts a list of positive integers and returns their greatest common divisor (GCD). Your function should return 1 as the GCD if there are no common factors between the integers. Here are some examples:
#
# if the list was
#
# [12, 24, 6, 18]
#
# then your function should return the GCD:
#
# 6
#
# if the list was
#
# [3, 5, 9, 11, 13]
#
# then your function should return their GCD:
#
# 1
#
def find_gcd(some_list):
   new_list=[]
   for numero in some_list:
      evalua_funcion_lista_divisores_n = funcion_lista_divisores_n(int(numero))
      new_list.append(evalua_funcion_lista_divisores_n)
# Ordena indice del numero menor ingresado
#   reg_list=[]
#   for x in new_list:
#      reg_list.append(len(x))
#   reg_menor=int(min(reg_list))
#   indice_menor=reg_list.index(reg_menor)
   reg_menor=int(min(some_list))
   indice_menor=some_list.index(reg_menor)
# Inserta indice menor para comparacion
   lista_extendida=[]
   for x in new_list:
      #evalua_unique_common = unique_common(new_list[indice_menor], x)
      a = new_list[indice_menor]
      b = x
      for x in a:
         indice=0
         if x in b:
            print(x, "esta en", b)
            indice=int(lista_extendida.index(x))
            lista_extendida.append(x)
#            print("indice",indice)
         else:
            print(x, "no esta en", b)
            #indice=int(lista_extendida.index(x))
            #lista_extendida.remove(x)
#            print("indice",indice)
      print("la lista",lista_extendida)
      
   #   print("menor",new_list[indice_menor],"contra",x)
   #tamano=int(len(evalua_unique_common))
   #evalua_unique_common = evalua_unique_common[tamano-1:tamano]
   #evalua_unique_common=int(evalua_unique_common[0])
   #return evalua_unique_common

# compara los elementos entre a y b
def unique_common(a, b):
   lista_extendida=[]
   for x in a:
      if x in b:
         print(x, "esta en", b)
         lista_extendida.append(x)
      elif x not in b:
         print(x, "no esta en", b)
         #reg_menor=int(min(some_list))
         indice=int(some_list.index(x))
         lista_extendida.pop([indice])
         
#   print(lista_extendida)
#   print(a,b)
   #evalua_funcion_lista_depurada = funcion_lista_depurada(lista_extendida)
   #if evalua_funcion_lista_depurada!=[]:
   #   return evalua_funcion_lista_depurada

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

# Funcion principal que llama a todas en secuencia
def funcion_lista_divisores_n(number):
#   evalua_funcion_lista_divisores = funcion_lista_divisores(number)
#   evalua_funcion_lista_divisores_extensa = funcion_lista_divisores_extensa(lista_divisores, number)
#   evalua_funcion_lista_divisores_depurada = funcion_lista_divisores_depurada(lista_divisores_extensa, number)
#   registros = int(len(lista_divisores_final))
#   return lista_divisores_final, registros

#def funcion_lista_divisores(number):
   number_end = number
   #lista_divisibles=[2,3,5,7,11,13,17]
   lista_divisores=[]
   lista_divisores.append(1)
   #for x in lista_divisibles:
   for x in range(2,1000):
      number_equal=0
      y=1
      while number%x == 0:
         number_equal = number_equal + x
         #print(number,"divisible para",x,"igual a",int(number/x),"comparador",int(number_equal))
         number=int(number/x)
         if x==number_equal:
            lista_divisores.append(x)
            #print(x,number_equal,"=")
         else:
            y=y*x
            lista_divisores.append(x*y)
            #print(x,number_equal,"!=")
   lista_divisores.sort()
   registros = int(len(lista_divisores))
   if number_end!=lista_divisores[registros-1]:
      lista_divisores.append(number_end)
#   return lista_divisores, number_end

# Funcion recibe mcm y calcula valores divisibles al numero n
#def funcion_lista_divisores_extensa(lista_divisores, number):
#   number_end = number
   lista_divisores_extensa=[]
   for x in lista_divisores:
      for y in lista_divisores:
         resultado = x*y
         if number_end >= resultado:
            if number_end%resultado == 0:
               #print(x,"multiplicado por",y,"igual a",int(resultado))
               lista_divisores_extensa.append(resultado)
#   return lista_divisores_extensa, number

# Funcion recibe lista completa y elimina numeros repetidos
#def funcion_lista_divisores_depurada(lista_divisores_extensa, number):
   lista_divisores_final = []
   for i in lista_divisores_extensa:
      if i not in lista_divisores_final:
         lista_divisores_final.append(i)
         lista_divisores_final.sort()
   registros = int(len(lista_divisores_final))
   return lista_divisores_final #, registros
   #return registros, number_end

# OJO SOLO LA FUNCION!!!
# Main Program #
some_list = [2, 3, 4, 5, 6, 7, 8, 45, 68, 34, 23, 124, 66, 12, 360, 24]
evalua_find_gcd = find_gcd(some_list) 
print(evalua_find_gcd)

