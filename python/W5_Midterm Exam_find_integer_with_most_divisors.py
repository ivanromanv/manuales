# Write a function named list_of_primes that accepts a positive integer n and returns a sorted list (ascending order) of all the prime numbers between 2 and n (including 2 but not including n)
#
def find_integer_with_most_divisors(input_list):
   new_list=[]
   for numero in input_list:
      evalua_funcion_lista_divisores_n = funcion_lista_divisores_n(int(numero))
      new_list.append(evalua_funcion_lista_divisores_n)
   #print(new_list)
   evalua_compara_numero_maximo_divisor = compara_numero_maximo_divisor(new_list)
   return evalua_compara_numero_maximo_divisor

def compara_numero_maximo_divisor(new_list):
   indice_list=[]
   for x in new_list:
      indice_list.append(x[0])
      num_max=max(indice_list)

   for x in indice_list:
      if x==num_max:
         indice=indice_list.index(x)
         break
   final_number = new_list[indice]
   #print(int(final_number[1]))
   numero_final = (int(final_number[1]))
   return numero_final

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
input_list = [12, 24, 6, 18]
evalua_find_integer_with_most_divisors = find_integer_with_most_divisors (input_list)
print(evalua_find_integer_with_most_divisors)
