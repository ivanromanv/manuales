# Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the sum of each column. Assume that the number of columns in each row is the same.
#
def list_sum_columns_2d_list(lista):
    cols = len(lista[0])
    new_list = []
    for c in range(cols):
        column_sum = 0
        for row in lista:
            column_sum += row[c]
        new_list.append(column_sum)
    return new_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
evalua_list_sum_columns_2d_list = list_sum_columns_2d_list(lista)
print(evalua_list_sum_columns_2d_list)
