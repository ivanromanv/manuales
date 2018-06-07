# Write a program using while loops that asks the user for a positive integer 'n' and prints a triangle using numbers from 1 to 'n'. For example if the user enters 6 then the output should be like this :
#
# (There should be no spaces between the numbers)
#
# 1
# 22
# 333
# 4444
# 55555
# 666666
#
def funcion_llenar_grafico_numero(number):
   inicio=(0)
   while inicio <= number-1:
      inicio = inicio + 1
      print(inicio*str(inicio))

# Main Program #
number = int(input("Enter number: "))
evalua_funcion_llenar_grafico_numero = funcion_llenar_grafico_numero(number)
#print(evalua_funcion_llenar_grafico_numero)
