#   Write a function that accepts an input string consisting of alphabetic characters and removes all the leading whitespace of the string and returns it without using .strip(). For example if:
#
# input_string = "    Hello  "
# then your function should return a string such as:
# output_string = "Hello  "
#
def funcion_espacio_blanco_derecha(caracteres):
    my_index = None
    for x in range(0, len(caracteres)):
        if caracteres[x] != " ":
            my_index = x
            break
    # recorta espacios a la derecha y genera nuevo string new_string
    new_string = caracteres[my_index::]
    return new_string

# OJO SOLO FUNCION!!!
# Main Program #
caracteres = str(input("Enter string: "))
evalua_funcion_espacio_blanco_derecha = funcion_espacio_blanco_derecha(caracteres)
print(evalua_funcion_espacio_blanco_derecha)
