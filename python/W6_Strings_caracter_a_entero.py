# Write a function that accepts an alphabetic character and returns the number associated with it from the ASCII table.
#
def funcion_caracter_a_entero(caracter):
    return (ord(caracter))

# OJO SOLO FUNCION!!!
# Main Program #
caracter = str(input("Enter caracter: "))
evalua_funcion_caracter_a_entero = funcion_caracter_a_entero(caracter)
print(evalua_funcion_caracter_a_entero)
