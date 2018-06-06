# Write a function that accepts a 2-dimensional list of integers, and sorts (descending order) all the elements inside each row and returns the sorted 2-dimensional list.
#
def list_sort_rows_2d_list(lista):
    new_list = []
    
    for data in lista:
        data.sort()
        data.reverse()
        new_list.append(data)
    new_list.sort()
    return new_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[0, 2, 4, 6, 8, 10], [11, 18, 19, 110, 111, 112]]
evalua_list_sort_rows_2d_list = list_sort_rows_2d_list(lista)
print(evalua_list_sort_rows_2d_list)
