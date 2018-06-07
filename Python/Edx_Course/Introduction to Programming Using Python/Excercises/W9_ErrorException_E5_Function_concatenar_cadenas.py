# Errors and Exceptions Exercise 5
# 0 puntos posibles (no calificados)
# You are trying to concatenate two strings and you need to write a function to perform the task. The function takes two arguments. You do not know the type of the first argument in advance but the second argument is certainly a string. Write a function that takes an unknown input and a string as input and tries to handle the error when you try to concatenate this unknown input to the string using the try..except..else clause. The unknown input could be either an integer or a string or a float. If the concatenation fails your function should return the value None (exactly without the quotes), If successful your function should return the resulting string.
# 
def concatenar_cadenas(cadena_a, cadena_b):
    try:
        new_chain = cadena_a+cadena_b
    except Exception:
        return None
    else:
        return new_chain
    
# OJO SOLO LA FUNCION!!!   
# Main
cadena_a = 1222
cadena_b = " para juntar dos cadenas"
evalua_concatenar_cadenas = concatenar_cadenas(cadena_a, cadena_b)
print(evalua_concatenar_cadenas)