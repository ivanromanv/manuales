# Write a function that accepts a 2-dimensional list of integers, and returns a sorted (ascending order) 1-Dimensional list containing all the integers from the original 2-dimensional list.
#
def list_covert_2d_to_1d_list(lista):
    new_list = []
    
    for data in lista:
        new_list=new_list+data
    new_list.sort()
    return new_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[0, 2, 4, 6, 8, 10], [11, 18, 19, 110, 111, 112]]
evalua_list_covert_2d_to_1d_list = list_covert_2d_to_1d_list(lista)
print(evalua_list_covert_2d_to_1d_list)
