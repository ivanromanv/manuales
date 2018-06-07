# Final Exam, Part 5 (Create a two dimensional list)
# 0.0/20.0 puntos (calificados)
#
# Write a function named "MY_2D_LIST" that receives a positive integer n (n >= 1) as parameter and returns a 2 dimensional list of numbers with n rows as shown below:
#
# For example, if the function is called as
#
# MY_2D_LIST(8)
#
# then your function should return
#
# [[1],
# [1, 1],
# [1, 2, 1],
# [1, 3, 3, 1],
# [1, 4, 6, 4, 1],
# [1, 5, 10, 10, 5, 1],
# [1, 6, 15, 20, 15, 6, 1],
# [1, 7, 21, 35, 35, 21, 7, 1]]
#
# Notes:
#
# The first list has 1 element, the second list has 2 elements, the third list has 3 elements and so on.
# The first and the last element of each list are always 1.
# The value of other elements in each list is the sum of the elements from the previous list with the same index and the index before. For example, the value of the element with index 2 in the list with index 5 is 10 which is equal to the sum of the values of the elements from previoius list with index 2 and index 1.
# This is called Pascal's Triangle
#
def MY_2D_LIST(n):
    pascal_triangle=[]
    # Caso base 
    if n == 0: 
        return [] 
    if n == 1: 
        return [[1]] 
    # Mediante recursividad
    pascal_triangle = MY_2D_LIST(n-1) 
    this_list = [1] 
    for i in range(1, n-1): 
        this_list.append(pascal_triangle[n-2][i-1] + pascal_triangle[n-2][i]) 
    this_list.append(1) 
    pascal_triangle.append(this_list) 
    return pascal_triangle

# OJO SOLO LA FUNCION!!!   
# Main
n = 8

evalua_MY_2D_LIST = MY_2D_LIST(n)
print(evalua_MY_2D_LIST)