# Write a function that accepts a string of words separated by spaces consisting of alphabetic characters and returns a string such that each word in the input string is reversed while the order of the words in the input string is preserved. The length of the input string must be equal to the length of the output string i.e. there should be no extra trailing or leading spaces in your output string. For example if:
#
# input_string = “this is a sample test”
# then the function should return a string such as:
# "siht si a elpmas tset"
#
def funcion_mayus_minus_reverse_string(input_string):
    output_string=""
    for caracter in input_string:
#        if caracter.islower():
#            new_char = caracter.upper()
#        else:
#            new_char = caracter.lower()
        output_string=caracter+output_string
    #separando
    output_string = output_string.split()
    #invirtiendo
    output_string.reverse()
    #Uniendo
    sign=" "
    final_string=sign.join(output_string)
    return final_string

# OJO SOLO FUNCION!!!
# Main Program #
input_string = "mi Hijo BRUNO es un chico Bueno"
evalua_funcion_mayus_minus_reverse_string = funcion_mayus_minus_reverse_string(input_string)
print(evalua_funcion_mayus_minus_reverse_string)
