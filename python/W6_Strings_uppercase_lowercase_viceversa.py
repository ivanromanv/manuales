# Write a function which accepts an input string and returns a string where the case of the characters are changed, i.e. all the uppercase characters are changed to lower case and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed. Do NOT use the string methods upper(), lower(), or swap(). 
#
def funcion_mayuscula_minuscula_viceversa(caracteres):
    my_index = None
    new_string=[]
    for x in range(0, len(caracteres)):
        if caracteres[x].isalpha() == True: #or caracteres[x].isnumeric() == True:
            if caracteres[x].isupper() == True:
#                print("alfanumerico mayuscula",caracteres[x])
                evalua_funcion_buscar_cambiar_caracter = funcion_buscar_cambiar_caracter(caracteres[x])
            else:
#                print("alfanumerico minuscula",caracteres[x])
                evalua_funcion_buscar_cambiar_caracter = funcion_buscar_cambiar_caracter(caracteres[x])
            new_string.append(evalua_funcion_buscar_cambiar_caracter)
        elif caracteres[x].isdigit() == True:
            new_string.append(caracteres[x])
        elif caracteres[x].isalnum() == False:
            new_string.append(caracteres[x])
        elif caracteres[x].isspace() == True:
            new_string.append(caracteres[x])    
    #new_string = caracteres[::]
    sign = ""
    new_string=sign.join(new_string)
    return new_string

def funcion_buscar_cambiar_caracter(caracter):
    cadena_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cadena_lower = 'abcdefghijklmnopqrstuvwxyz'
    for x in range(0, len(cadena_lower)):
        for x in range(0, len(cadena_upper)):
            if cadena_upper[x] == caracter:
#                print("Upper",cadena_upper[x],"indice x",x,"caracter",caracter)
                letra=cadena_lower[x]
            elif cadena_lower[x] == caracter:
#                print("Lower",cadena_lower[x],"indice x",x,"caracter",caracter)
                letra=cadena_upper[x]
    return letra
            
# OJO SOLO FUNCION!!!
# Main Program #
caracteres = str(input("Enter string: "))
evalua_funcion_mayuscula_minuscula_viceversa = funcion_mayuscula_minuscula_viceversa(caracteres)
print(evalua_funcion_mayuscula_minuscula_viceversa)
