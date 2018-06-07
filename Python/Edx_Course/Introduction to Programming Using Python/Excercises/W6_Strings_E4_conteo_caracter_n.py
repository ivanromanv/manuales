# Write a function that takes a list of words as an input argument and returns True if the list is sorted and returns False otherwise.
#
def funcion_conteo_caracter_n(input_string, n):
    n = n.lower()
    input_string = input_string.lower()
    contador=0
    for x in input_string:
        if x==n:
            contador = contador + 1
    return contador

# OJO SOLO FUNCION!!!
# Main Program #
input_string = "Mi hijo Bruno es bueno"
n = "e"
evalua_funcion_conteo_caracter_n = funcion_conteo_caracter_n(input_string, n)
print(evalua_funcion_conteo_caracter_n)
