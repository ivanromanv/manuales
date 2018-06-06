# Recursive Functions Exercise 5 (Sum of a Nested List)
# 0 puntos posibles (no calificados)
# Write a function named nested_list_sum that receives a nested list of integers as parameter and calculates and returns the total sum of the integers in the list using recursion. Keep in mind that the inner elements may be integers or other nested lists themselves. 
#
# For example, when your function is called as:
#
# nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]])
# Then, your function should return the total sum as
# 10
#
def nested_list_sum (n):
    my_sum = 0
    for element in n:
        if type(element) != type([]):
            my_sum += element
        else :
            my_sum += nested_list_sum(element)
    return my_sum
    
# OJO SOLO LA FUNCION!!!   
# Main
n = ([1, -1, [2, -2], [3, -3, [4, -4], 10]])

evalua_nested_list_sum  = nested_list_sum (n)
print(evalua_nested_list_sum )