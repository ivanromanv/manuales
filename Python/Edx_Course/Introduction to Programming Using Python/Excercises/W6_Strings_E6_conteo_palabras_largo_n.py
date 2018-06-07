# Write a function which returns the number of words in the input string which have more than 4 characters. Assume that the input string consists of alphabetic characters separated by spaces and capitalization does not matter i.e. an upper case character should be treated the same as a lower case character.
#
def funcion_conteo_palabras_largo(input_string):
    input_string = input_string.lower()
    input_string = input_string.split()
    contador=0
    for x in input_string:
        if len(x)>4:
            contador = contador + 1
    return contador

# OJO SOLO FUNCION!!!
# Main Program #
input_string = "mi hijo bruno es un niño bueno"
evalua_funcion_conteo_palabras_largo = funcion_conteo_palabras_largo(input_string)
print(evalua_funcion_conteo_palabras_largo)
