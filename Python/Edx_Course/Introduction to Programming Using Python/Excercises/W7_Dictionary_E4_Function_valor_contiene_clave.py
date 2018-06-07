# Dictionary Exercise 4 (Value Containing Key)
# 0 puntos posibles (no calificados)
# Write a function named return_keys which accepts a dictionary and an integer as input and returns an ascending sorted list of all the keys whose values contain the input integer. Note that the keys of this dictionary are strings while the values of this dictionary are 1 Dimensional lists of integers. For example if the input dictionary is:
#
# sample_dictionary = {"rabbit" : [1, 2, 3], "kitten" : [2, 2, 6], "lioness": [6, 8, 9]}
# if your function is called as return_keys(sample_dictionary,2) , then your function should return:
# [ "kitten", "rabbit",]
# If the input integer is not found then your function should return an empty list.
#
def return_keys(sample_dictionary, sample_value):
    output_list = []
    keys = sample_dictionary.keys()
    for nombre in keys:
        lista_valor = sample_dictionary[nombre]
        valor_1=lista_valor[0]
        valor_2=lista_valor[1]
        valor_3=lista_valor[2]
        if valor_1==sample_value or valor_2==sample_value or valor_3==sample_value:
            output_list.append(nombre)
    output_list.sort()
    return output_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
sample_value=2
sample_dictionary = {'Crow': [11, 12, 3], 'Chicken': [12, 2, 16], 'Bat': [12, 3, 0], 'Sparrow': [6, 8, 9]}
evalua_return_keys = return_keys(sample_dictionary, sample_value)
print(evalua_return_keys)
