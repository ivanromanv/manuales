# Write a function which accepts an input string and returns a string where the case of the characters are changed, i.e. all the uppercase characters are changed to lower case and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed. Do NOT use the string methods upper(), lower(), or swap(). 
#
#Version 1
def funcion_reverse_string_1(input_string):
    output_string=""
    for caracter in input_string:
        output_string=caracter+output_string
    return output_string

#Version 2
def funcion_reverse_string_2(input_string):
    output_string=""
    for caracter in range(len(input_string)-1,-1,-1):
        output_string=output_string+input_string[caracter]
    return output_string
           
# OJO SOLO FUNCION!!!
# Main Program #
input_string = str(input("Enter string: "))
evalua_funcion_reverse_string_1 = funcion_reverse_string_1(input_string)
evalua_funcion_reverse_string_2 = funcion_reverse_string_2(input_string)
print("Version-1",evalua_funcion_reverse_string_1)
print("Version-2",evalua_funcion_reverse_string_2)

