# Write a function that accepts an input string consisting of alphabetic characters and removes all the trailing whitespace of the string and returns it without using any .strip() method. For example if:
#
# input_string = "  Hello       "
#
# then your function should return an output string such as:
#
# output_string = "  Hello"
#
def funcion_espacio_blanco_izquierda(caracteres):
    my_index = None
    for x in range(0, len(caracteres)):
        if caracteres[x] != " ":
            my_index = x
        elif caracteres[x].isalpha() == True:
            continue
    # recorta espacios a la izquierda y genera nuevo string new_string
    new_string = caracteres[:my_index+1:]
    return new_string

# OJO SOLO FUNCION!!!
# Main Program #
caracteres = str(input("Enter string: "))
evalua_funcion_espacio_blanco_izquierda = funcion_espacio_blanco_izquierda(caracteres)
print(evalua_funcion_espacio_blanco_izquierda)
