# Write a function that finds the distance between two points and returns it. The distance between two points with x,y, and z components can be calculated as:
# distance = raiz_2((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2))
# The input for this function will be two 1 Dimensional lists that contain the x,y,z coordinates each. For example if the input lists are:
#
# a = [2, 3, -5] 
# b = [4, -3, 12]
#
# Then your function should return their distance such as:
# 18.138357147217054
# Hint: You may use the math module!
#
from math import sqrt

def funcion_distancia_entre_2_puntos(a,b):
   x2=b[0]
   x1=a[0]
   y2=b[1]
   y1=a[1]
   z2=b[2]
   z1=a[2]
   distance = sqrt( ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2) )
   return distance

# Main Program #
a = [2, 3, -5] 
b = [4, -3, 12]
evalua_funcion_distancia_entre_2_puntos = funcion_distancia_entre_2_puntos(a,b)
print(evalua_funcion_distancia_entre_2_puntos)

