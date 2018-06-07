# Write a function which accepts a 2D list of numbers and returns the sum of all the number in the list You can assume that the number of columns in each row is the same. (Do not use python's built-in sum() function). 
#
def sum_of_2d_list(lista):
    total_sum=0
    for data in lista:
        for list_index in range(0,len(data)):
            total_sum=total_sum+data[list_index]
    return total_sum        

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[1,2,3,4],[4,3,2,1]]
evalua_sum_of_2d_list = sum_of_2d_list(lista)
print(evalua_sum_of_2d_list)
