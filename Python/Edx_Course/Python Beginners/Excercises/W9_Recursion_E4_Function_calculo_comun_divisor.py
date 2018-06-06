# Recursive Functions Exercise 4 (GCD)
# 0 puntos posibles (no calificados)
# Write a function named calculate_gcd that receives two positive integers a and b as parameter and returns their greatest common divisor (GCD) using recursion. 
#
# For example, when your function is called as:
#
# calculate_gcd(10, 15)
# Your function should return:
# 5
#
def calculate_gcd(a,b):
    if b == 0:
        return a
    else:
        return calculate_gcd(b, a%b)
    
# OJO SOLO LA FUNCION!!!   
# Main
a = 3
b = 4
evalua_calculate_gcd = calculate_gcd(a,b)
print(evalua_calculate_gcd)