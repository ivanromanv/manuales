# Write a function that accepts an input string consisting of alphabetic characters and removes all the leading whitespace of the string and returns it without using .strip(). For example if:
#
# input_string = "    Hello  "
# then your function should return a string such as:
# output_string = "Hello  "
#
def funcion_lider_espacio_blanco(caracteres):
    resume=caracteres.replace(" ","")
    return resume

# OJO SOLO FUNCION!!!
# Main Program #
caracteres = str(input("Enter string: "))
evalua_funcion_lider_espacio_blanco = funcion_lider_espacio_blanco(caracteres)
print(evalua_funcion_lider_espacio_blanco)
