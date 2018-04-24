# Write a function that takes a string consisting of alphabetic characters as input argument and returns True if the string is a palindrome. A palindrome is a string which is the same backward or forward. Note that capitalization does not matter here i.e. a lower case character can be considered the same as an upper case character.
#
#
def funcion_reverse_string(input_string):
    input_string = input_string.lower()
    output_string=""
    for caracter in input_string:
        output_string=caracter+output_string
    if input_string==output_string:
        return True
    else:
        return False
  
# OJO SOLO FUNCION!!!
# Main Program #
input_string = str(input("Enter string: "))
evalua_funcion_reverse_string = funcion_reverse_string(input_string)
print(evalua_funcion_reverse_string)
