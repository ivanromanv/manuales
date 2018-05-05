# Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the sum of each row. You can assume that the number of columns in each row is the same.
#
def sum_list_rows_2d_list(lista):
    valor_lista=0
    new_list=[]
    for data in lista:
        for list_index in range(0,len(data)):
            valor_lista=valor_lista+data[list_index]
        new_list.append(valor_lista)
        valor_lista=0
    return new_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
evalua_sum_list_rows_2d_list = sum_list_rows_2d_list(lista)
print(evalua_sum_list_rows_2d_list)
