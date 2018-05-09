# Write a function that takes an integer as input argument and returns the integer using words. For example if the input is 4721 then the function should return the string "four seven two one". Note that there should be only one space between the words and they should be all lowercased in the string that you return.
#
def number_to_words(input_integer):
    #convertir a string
    string_input=str(input_integer)
    #convertir a lista
    string_list =list(string_input)
    dictionary={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
    conversion=""
    for numero in string_list:
        conversion=conversion+dictionary[numero] + " "
    conversion = conversion.rstrip(" ")
    return conversion

# OJO SOLO LA FUNCION!!!   
# Main Program #
input_integer = 5124
evalua_number_to_words = number_to_words(input_integer)
print(evalua_number_to_words)
