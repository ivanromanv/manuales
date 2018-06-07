# Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. For example if the user enters 6 then the output should be:
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
#
def funcion_llenar_grafico_numero(number):
   inicio=(0)
   conversion=str()
   
   while inicio <= number-1:
      inicio = inicio + 1
      conversion=str(conversion)+str('*')
      print(conversion)

   while inicio >= number:
      number = number - 1
      conversion = conversion[0:number]
      print(conversion)
      if number == 1:
         break

# Main Program #
number = int(input("Enter number: "))
evalua_funcion_llenar_grafico_numero = funcion_llenar_grafico_numero(number)
#print(evalua_funcion_llenar_grafico_numero)
