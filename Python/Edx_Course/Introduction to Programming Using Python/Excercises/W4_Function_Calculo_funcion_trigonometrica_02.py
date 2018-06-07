# Write a function that accepts a number x and evaluates the following expression:
# y=sin(x) - cos(x) + sin(x)cos(x)
# and returns the value of y. (Hint: Use math module)
#
from math import cos, sqrt

def funcion_trigonometrica(valor):
   y = abs(valor**3) + cos(sqrt(3*valor)) 
   return y

# Main Program #
evalua_funcion_trigonometrica = funcion_trigonometrica(3)
print(evalua_funcion_trigonometrica)

