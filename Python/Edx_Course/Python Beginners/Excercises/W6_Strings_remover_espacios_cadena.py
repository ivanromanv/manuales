# Write a function which accepts an input string and returns a string where the case of the characters are changed, i.e. all the uppercase characters are changed to lower case and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed. Do NOT use the string methods upper(), lower(), or swap(). 
#
def funcion_remover_espacios_cadena(caracteres):
    string=""
    for x in caracteres:
        if x==" ":
            string=''+string
        else:
            string=string+str(x)
    return string
           
# OJO SOLO FUNCION!!!
# Main Program #
caracteres = str(input("Enter string: "))
evalua_funcion_remover_espacios_cadena = funcion_remover_espacios_cadena(caracteres)
print(evalua_funcion_remover_espacios_cadena)
