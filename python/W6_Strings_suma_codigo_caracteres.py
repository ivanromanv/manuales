#Write a function that accepts an alphabetic string and returns an integer which is the sum of all the UTF-8 codes of the character in that string. For example if the input string is "hello" then your function should return 532
#
def funcion_suma_codigo_caracteres(caracteres):
    suma=0
    for x in caracteres:
        suma=suma+int(ord(x))
    return suma

# OJO SOLO FUNCION!!!
# Main Program #
caracteres = str(input("Enter characters: "))
evalua_funcion_suma_codigo_caracteres = funcion_suma_codigo_caracteres(caracteres)
print(evalua_funcion_suma_codigo_caracteres)
