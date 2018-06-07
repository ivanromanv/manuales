# Write a function that receives a positive integer as function parameter and returns True if the integer is a perfect number, False otherwise. A perfect number is a number whose sum of the all the divisors (excluding itself) is equal to itself. For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6. Therefore, 6 is a perfect number. 
#
# Remember, that you are not asked to print anything. So, your function should return either True or False. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.
#
def funcion_numero_perfecto(numero):
   suma=(0)
   for x in range(1,numero):
      if numero % x == 0:
         suma = suma + x
   if suma == numero:
      return True
   else:
      return False

# OJO SOLO LA FUNCION!!!   
# Main Program #
numero = int(input("Enter the number: "))
evalua_funcion_numero_perfecto = funcion_numero_perfecto(numero)
print(evalua_funcion_numero_perfecto)
