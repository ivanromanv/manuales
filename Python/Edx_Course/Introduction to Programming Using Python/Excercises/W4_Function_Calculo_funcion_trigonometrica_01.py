# Write a function that accepts a number x and evaluates the following expression:
# y=sin(x) - cos(x) + sin(x)cos(x)
# and returns the value of y. (Hint: Use math module)
#
from math import sin, cos

def funcion_trigonometrica(valor):
   y = sin(valor) - cos(valor) + sin(valor)*cos(valor)
   return y

# Main Program #
evalua_funcion_trigonometrica = funcion_trigonometrica(2)
print(evalua_funcion_trigonometrica)

