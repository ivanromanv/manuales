# Write a function that accepts a positive integer n and returns the ascii character associated with it.
#
def funcion_entero_a_caracter(number):
    return (chr(number))

# OJO SOLO FUNCION!!!
# Main Program #
number = int(input("Enter number: "))
evalua_funcion_entero_a_caracter = funcion_entero_a_caracter(number)
print(evalua_funcion_entero_a_caracter)
