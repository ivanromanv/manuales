# Write a function that will receive a 2D list of integers. The function should return the count of how many rows of the list have even sums and the count of how many rows have odd sums. For example if the even count was 2, and odd count was 4 your function should return them in a list like this: [2, 4].
#
def list_count_even_odd_2d_list(lista):
    valor_lista=0
    new_list=[]
    final_list=[]
    par=0
    impar=0
    
    for data in lista:
        for list_index in range(0,len(data)):
            valor_lista=valor_lista+data[list_index]
        new_list.append(valor_lista)
        valor_lista=0
        
    for valor in new_list:
        if valor%2 ==0:
            par=par+1
        else:
            impar=impar+1
    final_list.append(par)
    final_list.append(impar)
    return final_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
lista = [[0, 0, 2, 3], [5, 5, 5, 5], [37, 37, 37, -39]]
evalua_list_count_even_odd_2d_list = list_count_even_odd_2d_list(lista)
print(evalua_list_count_even_odd_2d_list)
