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
def find_mismatch(s1,s2):
    long_s1 = len(s1)
    long_s2 = len(s2)
    print(long_s1,long_s2)
    if long_s1==long_s2:
        evalua_find_mismatch_compara = find_mismatch_compara(s1,s2)

def find_mismatch_compara(s1,s2):   
    print(s1)
    print(s2)
    for item1 in s1:
        for item2 in s2:
            if item1==item2:
                print(item1,"es igual a",item2)
    return 0

def find_mismatch_longitud(s1,s2):   
    for item1 in s1:
        for item2 in s2:
            if item1==item2:
                print(item1,"es igual a",item2)
    return 1

# OJO SOLO LA FUNCION!!!   
# Main Program #
s1 = ['Python','Hello There','sin','dog']
s2 = ['Java','helloothere','sink','Dog']
evalua_find_mismatch = find_mismatch(s1,s2)
print(evalua_find_mismatch)
