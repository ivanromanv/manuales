# Write a function that accepts a 2D list of integers and returns the maximum EVEN value for the entire list. You can assume that the number of columns in each row is the same. Your function should return None if the list is empty or all the numbers in the 2D list are odd. Do NOT use python's built in max() function.
#
def max_even_2d_list(lista):
    par_max=0
    for data in lista:
        for list_index in range(0,len(data)):
            if data[list_index]%2 == 0:
                if data[list_index]>=par_max:
                    par_max=data[list_index]
    return par_max       

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[121, -18, 20, 13, -44], [199, -12, -6, 13, -44]]
evalua_max_even_2d_list = max_even_2d_list(lista)
print(evalua_max_even_2d_list)
