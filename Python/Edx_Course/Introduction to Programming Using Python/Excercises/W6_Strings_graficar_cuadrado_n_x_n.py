# Write a program that asks the user for an input 'n' and prints a square of n by n asterisks "*". For example if the user enters 5 then the output should look like the following: Note that there should be no spaces between the asterisks
#
# *****
# *****
# *****
# *****
# *****
#
def funcion_llenar_grafico_numero_nxn(number):
   inicio=(0)
   while inicio <= number:
      inicio = inicio + 1
      if inicio == number:
          for x in range(number):
              print(inicio*str("*"))

# Main Program #
number = int(input("Enter number: "))
evalua_funcion_llenar_grafico_numero_nxn = funcion_llenar_grafico_numero_nxn(number)
#print(evalua_funcion_llenar_grafico_numero_nxn)
