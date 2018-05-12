# Tuples Exercise 2 (Dictionary to Tuple)
# 0 puntos posibles (no calificados)
# Write a function that accepts a dictionary as input and returns a tuple of tuples. That is your first tuple should be the tuple of all the keys, and the second tuple should be tuple of all the values in the dictionary. For example if the input dictionary is:
#
# input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"} 
# then you should return a tuple(tuple of keys, tuple of values) such as:
# ((1, 2, 3, 4), ('a', 'b', 'c', 'd'))
#
def dictionary_to_tuple(input_dictionary):
    keys = tuple(input_dictionary.keys())
    values = tuple(input_dictionary.values())
    return keys, values    
    
# OJO SOLO LA FUNCION!!!   
# Main
input_dictionary  = {1:"a", 2:"b", 3:"c", 4:"d"} 
evalua_dictionary_to_tuple = dictionary_to_tuple(input_dictionary)
print(evalua_dictionary_to_tuple)