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
# 0 igual
# 1 eliminar 1 inicio o final
# 2 insertar 1 inicio o final
# 3 diferentes total, diferencia mas de 2 caracteres
def single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()

    #Return 0
    if s1==s2:
        return 0
    #Return 3
    if abs(len(s1)-len(s2))!=1:
        return 3
    #Return 1 / 2
    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 3
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 2
                else:
                    return 3
        return 2
# OJO SOLO LA FUNCION!!!   
# Main Program #
# Python	  Java	         2
# Hello There	  helloothere	 1
# sin	          sink	         2 (note not the same length)
# dog	          Dog	         0
# Ruby            Java           2
s1 = "book"
s2 = "booka2"
evalua_single_insert_or_delete = single_insert_or_delete(s1,s2)
print(evalua_single_insert_or_delete)
