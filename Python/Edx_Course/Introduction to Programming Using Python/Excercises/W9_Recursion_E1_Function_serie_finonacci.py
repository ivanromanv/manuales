# Recursive Functions Exercise 1 (Fibonacci Numbers)
# 0 puntos posibles (no calificados)
# Write a function named calculate_fibonacci that receives a positive integer 'n' as parameter and calculates and returns the nth fibonacci number using recursion. 
#
# Notes
#
# Fibonacci numbers are the numbers in the sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
# The 0th Fibonacci number is 0, the 1st Fibonacci number is 1.
# All other numbers are sum of the previous two numbers.
# For example, when your function is called as:
# calculate_fibonacci(10)
# Then, your function should return the 10th fibonacci number:
# 55
#
def calculate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
# OJO SOLO LA FUNCION!!!   
# Main
n = 10
evalua_calculate_fibonacci = calculate_fibonacci(n)
print(evalua_calculate_fibonacci)