# Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the maximum value of each column. Assume that the length of columns is consistent in each row.
#
def list_max_value_columns_2d_list(lista):
    cols = len(lista[0])
    new_list = []
    
    for c in range(cols):
        column_max = 0
        for row in lista:
            if row[c] > column_max:
                column_max = row[c]
        new_list.append(column_max)
    return new_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[1, 1, 1, 12], [10, 2, 2, 2], [3, 3, 20, 3], [4, 40, 4, 4]]
evalua_list_max_value_columns_2d_list = list_max_value_columns_2d_list(lista)
print(evalua_list_max_value_columns_2d_list)
