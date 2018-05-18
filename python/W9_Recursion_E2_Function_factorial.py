# Recursive Functions Exercise 1 (Fibonacci Numbers)
# 0 puntos posibles (no calificados)
# Write a function named calculate_fibonacci that receives a positive integer 'n' as parameter and calculates and returns the nth fibonacci number using recursion. 
#
# Notes
#
# Recursive Functions Exercise 2 (Factorial)
# 0 puntos posibles (no calificados)
# Write a function named calculate_factorial that receives a positive integer 'n' as parameter and calculates and returns the factorial of n using recursion. 
#
# Notes 
#
# Factorial is the product of an integer with all the integers below it. For example, the factorial of 5 is 5*4*3*2*1 = 120. Note that the factorial of both 0 and 1 is 1. For example, when your function is called as:
#
# calculate_factorial(10)
# Then, your function should return the number:
# 3628800
#
def calculate_factorial(n):
    if n < 1:
        return 1
    else:
        return n * calculate_factorial(n-1)
    
# OJO SOLO LA FUNCION!!!   
# Main
n = 10
evalua_calculate_factorial = calculate_factorial(n)
print(evalua_calculate_factorial)