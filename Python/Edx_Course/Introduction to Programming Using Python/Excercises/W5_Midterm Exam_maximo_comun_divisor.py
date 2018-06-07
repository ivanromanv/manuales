#  Write a function named unique_common that accepts two lists both of which contain integers as parameters and returns a sorted list (ascending order) which contains unique common elements from both the lists. If there are no common elements between the two lists, then your function should return the keyword None
#
# For example, if two of the lists received by the function are:
#
#  Write a function named find_gcd that accepts a list of positive integers and returns their greatest common divisor (GCD). Your function should return 1 as the GCD if there are no common factors between the integers. Here are some examples:
#
# if the list was
#
# [12, 24, 6, 18]
#
# then your function should return the GCD:
#
# 6
#
# if the list was
#
# [3, 5, 9, 11, 13]
#
# then your function should return their GCD:
#
# 1
###########################
# RESPUESTA DEL INSTRUCTOR
###########################
def find_gcd(some_list):
    result = some_list[0]
    for i in range(1, len(some_list)):
        result = my_gcd(result, some_list[i])
    return result
  
def my_gcd(a,b):
    while b:
        a, b = b, a%b
    return a

# OJO SOLO LA FUNCION!!!
# Main Program #
some_list = [12, 24, 6, 18]
evalua_find_gcd = find_gcd(some_list) 
print(evalua_find_gcd)

