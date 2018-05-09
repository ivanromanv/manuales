# Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.
#
def dictionary_sorted_keys(dictionary):
    claves = dictionary.keys()
    claves = list(claves)
    claves.sort()
    return claves

# OJO SOLO LA FUNCION!!!   
# Main Program #
dictionary = {'cars': 1, 'bikes': 0, 'trucks': 2}
evalua_dictionary_sorted_keys = dictionary_sorted_keys(dictionary)
print(evalua_dictionary_sorted_keys)
