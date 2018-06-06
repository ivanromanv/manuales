# Write a function that takes a string consisting of alphabetic characters as input argument and returns the lower case of the most common character. Ignore white spaces i.e. Do not count any white space as a character. Note that capitalization does not matter here i.e. that a lower case character is equal to a upper case character. In case of a tie between certain characters return the last character that has the most count
#
def funcion_conteo_caracter_comun(input_string):
    input_string = input_string.lower()
    input_string = input_string.replace(" ","")
    sample_character = None
    sample_maximum_count = 0
    for x in input_string:
        cont_letra = input_string.count(x)
        if cont_letra >= sample_maximum_count:
            sample_maximum_count = cont_letra
            sample_character = x
    return sample_character

# OJO SOLO FUNCION!!!
# Main Program #
input_string = "mi hijo bruno es un niño bueno"
evalua_funcion_conteo_caracter_comun = funcion_conteo_caracter_comun(input_string)
print(evalua_funcion_conteo_caracter_comun)
