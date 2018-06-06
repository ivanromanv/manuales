# Write a function that accepts a dictionary as input and returns a sorted list of all the values in the dictionary. Assume that the values of this dictionary are just integers.
#
def dictionary_sorted_values(dictionary):
    valores = dictionary.values()
    valores = list(valores)
    valores.sort()
    return valores

# OJO SOLO LA FUNCION!!!   
# Main Program #
dictionary = {'James': 19, 'Tina': 35, 'Sam': 17}
evalua_dictionary_sorted_values = dictionary_sorted_values(dictionary)
print(evalua_dictionary_sorted_values)
