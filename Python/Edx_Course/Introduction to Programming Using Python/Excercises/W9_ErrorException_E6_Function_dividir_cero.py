# Errors and Exceptions Exercise 6
# 0 puntos posibles (no calificados)
# You are trying to divide two numbers and you need to write a function to perform the task. The function takes two arguments. The first argument is a float but you are unsure about the second argument (there is a chance that the second argument could be a zero). Write a function that takes a float and an unknown input and tries to handle the error when you try to divide the float by the unknown input using the try..except..else clause. The unknown input could be either an integer or a string or a float. If the operation fails your function should return the value None (exactly without the quotes), If successful your function should return the result.
#
def dividir_numeros(value_a, value_b):
    try:
        resultado = (float(value_a)/float(value_b))
    except (ZeroDivisionError, ValueError):
        return None
    else:
        return float(resultado)
    
# OJO SOLO LA FUNCION!!!   
# Main
value_a = 1222
value_b = 0
evalua_dividir_numeros = dividir_numeros(value_a, value_b)
print(evalua_dividir_numeros)