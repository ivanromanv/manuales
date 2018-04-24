# Write a function that takes a list of words as an input argument and returns True if the list is sorted and returns False otherwise.
#
def funcion_conteo_vocales(input_string):
    input_string = input_string.lower()
    vocales = ['a','e','i','o','u']
    contador=0
    for x in input_string:
        for y in vocales:
            if x==y:
                contador = contador + 1
    return contador

# OJO SOLO FUNCION!!!
# Main Program #
input_string = "Mi hijo Bruno es bueno"
evalua_funcion_conteo_vocales = funcion_conteo_vocales(input_string)
print(evalua_funcion_conteo_vocales)
