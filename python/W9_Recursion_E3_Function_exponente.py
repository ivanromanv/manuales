# Recursive Functions Exercise 3 (Exponent)
# 0 puntos posibles (no calificados)
# Write a function named calculate_exponent that receives two positive integers a and b as parameter and calculates and returns a to the power of b using recursion. For example, when your function is called as:
#
# calculate_exponent(5, 3)
# Then, your function should return:
# 125
#
def calculate_exponent(a,b):
    if b == 0:
        return 1
    else:
        return a * calculate_exponent(a, b-1)
    
# OJO SOLO LA FUNCION!!!   
# Main
a = 5
b = 5
evalua_calculate_exponent = calculate_exponent(a,b)
print(evalua_calculate_exponent)