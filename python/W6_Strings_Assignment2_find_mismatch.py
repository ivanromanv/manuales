# Write a function named find_mismatch that accepts two strings as input arguments and returns:
#
# 0 if the two strings match exactly.
# 1 if the two strings have the same length and mismatch in only one character.
# 2 if the two strings do not have the same length or mismatch in two or more characters.
# Capital letters are considered the same as lower case letters. Here are some examples:
# First string	  Second String	 Function return
# Python	  Java	         2
# Hello There	  helloothere	 1
# sin	          sink	         2 (note not the same length)
# dog	          Dog	         0
#
# RESOLUCION DEL INSTRUCTOR
# def _instructor_function (s1,s2):
#    if len(s1) != len(s2):
#        return 2
#    s1=s1.lower()
#    s2=s2.lower()
#    number_of_mismatches=0
#    for index in range(len(s1)):
#        if s1[index] != s2[index]:
#            number_of_mismatches=number_of_mismatches+1
#            if number_of_mismatches>1:
#                return 2
#    return number_of_mismatches
#
def find_mismatch(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    
    #Return 0
    if s1==s2:
        return 0
    #Return 1
    elif len(s1)==len(s2) and coincidencia(s1, s2)==False:
        return 1
    #Return 2
    elif len(s1)==len(s2) or len(s1)!=len(s2):
        if coincidencia(s1, s2)==True:
            return 2
        if coincidencia(s1, s2)==False:
            return 2

def coincidencia(s1,s2):
    contador_neq=0
    contador_eeq=0
    for x in s1:
        for y in s2:
            if x!=y:
                contador_neq=contador_neq+1
#                print("Igual longitud Retorna 1",x,"no es igual a",y, contador_neq)
            else:
                contador_eeq=contador_eeq+1
#                print("Igual longitud Retorna 1",x,"es igual a",y, contador_eeq)
    if contador_neq==len(s1)*len(s2):
#        print("NO coindice con ningun caracter", contador_neq)
        return True
    elif (len(s1)*len(s2))-contador_neq >= 2:
#        print("Coindice 2 o mas caracteres", contador_eeq, (len(s1)*len(s2))-contador_neq)
        return False

# OJO SOLO LA FUNCION!!!   
# Main Program #
# Python	  Java	         2
# Hello There	  helloothere	 1
# sin	          sink	         2 (note not the same length)
# dog	          Dog	         0
# Ruby            Java           2
s1 = "Ruby"
s2 = "Java"

evalua_find_mismatch = find_mismatch(s1,s2)
print(evalua_find_mismatch)
