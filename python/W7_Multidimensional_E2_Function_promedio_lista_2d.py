# Write a function that accepts a 2 Dimensional list of integers and returns the average. Remember that average = (sum_of_all_items) / (total_number_of_items). 
#
def average_of_2d_list(lista):
    contador=0
    for item in lista:
        contador=contador+len(item)
        
    total_sum=0
    for data in lista:
        for list_index in range(0,len(data)):
            total_sum=total_sum+data[list_index]
    average=total_sum/contador
    return average       

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[0, 0, 2, 3], [5, 5, 5, 5], [37, 37, 37, -39]]
evalua_average_of_2d_list = average_of_2d_list(lista)
print(evalua_average_of_2d_list)
