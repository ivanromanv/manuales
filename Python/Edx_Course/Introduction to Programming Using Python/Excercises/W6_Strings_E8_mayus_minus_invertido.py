# Write a function which accepts an input string and returns a reverse of the input string while the case for every single character is reversed. The input string for this function would be a sentence (words separated by spaces) consisting of alphabetic characters. For example if:
#
# input_string = "Hello Python World"
# then the function should return a string such as:
# "DLROw NOHTYp OLLEh"
#
def funcion_mayus_minus_reverse_string(input_string):
    output_string=""
    for caracter in input_string:
        if caracter.islower():
            new_char = caracter.upper()
        else:
            new_char = caracter.lower()
        output_string=new_char+output_string
    return output_string

# OJO SOLO FUNCION!!!
# Main Program #
input_string = "mi Hijo BRUNO es un chico Bueno"
evalua_funcion_mayus_minus_reverse_string = funcion_mayus_minus_reverse_string(input_string)
print(evalua_funcion_mayus_minus_reverse_string)
