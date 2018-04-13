# Write a function that accepts two positive integers as function parameters and returns their least common multiple (LCM). The LCM of two integers a and b is the smallest (non zero) positive integer that is divisible by both a and b. For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10. 
#
# Remember that you are not asked to print anything. So, your function should return the LCM and not print it. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.
#
def funcion_minimo_comun_multiplo(numero_a, numero_b):
   lista_a = funcion_mcm_numero(numero_a)
   lista_b = funcion_mcm_numero(numero_b)

   lista_max=[]
   lista_min=[]
   if numero_a > numero_b:
      lista_max = lista_a
      lista_min = lista_b
   else:
      lista_max = lista_b
      lista_min = lista_a

   calculo=int(1)
   for x in lista_max:
      calculo=calculo*x
      nuevo=int(1)
      for y in lista_min:
         if x==y:
#            print("sec",contador,",x:",x,"SI existe en y:",y,"no hace nada!")
            lista_min.remove(y)
         else:
            nuevo=nuevo*y
#            print("sec",contador,",x:",x,"NO existe en y:",y,"nuevo",nuevo)
   evalua_funcion_multiplicar_lista = funcion_multiplicar_lista(lista_min)
   calculo=int(calculo*evalua_funcion_multiplicar_lista)
   return calculo

def funcion_multiplicar_lista(lista_min):
   valor=int(1)
   for x in lista_min:
      valor = valor * x
   return valor

def funcion_mcm_numero(numero):
   #lista_divisibles=[2,3,5,7,11,13,17]
   lista_mcm=[]
   #for x in lista_divisibles:
   for x in range(2,1000):      
      mcm=int(1)
      while numero%x == 0:
         #print(numero,"divisible para ",x)
         print(numero,"divisible para",x,"igual a",int(numero/x))
         numero=int(numero/x)
         lista_mcm.append(x)
   return lista_mcm

# OJO SOLO LA FUNCION!!!   
# Main Program #
numero_a = int(input("Enter the first number: "))
numero_b = int(input("Enter the second number: "))
evalua_funcion_minimo_comun_multiplo = funcion_minimo_comun_multiplo(numero_a, numero_b)
#print(evalua_funcion_minimo_comun_multiplo)
