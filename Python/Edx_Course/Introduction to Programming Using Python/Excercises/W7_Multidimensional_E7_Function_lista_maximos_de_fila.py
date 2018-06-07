# Write a function that will receive a 2D list of integers. The function should return the count of how many rows of the list have even sums and the count of how many rows have odd sums. For example if the even count was 2, and odd count was 4 your function should return them in a list like this: [2, 4].
#
def list_max_value_rows_2d_list(lista):
    new_list=[]
    max_valor=0
    
    for data in lista:
        max_valor=max(data)
        new_list.append(max_valor)
    return new_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
evalua_list_max_value_rows_2d_list = list_max_value_rows_2d_list(lista)
print(evalua_list_max_value_rows_2d_list)
