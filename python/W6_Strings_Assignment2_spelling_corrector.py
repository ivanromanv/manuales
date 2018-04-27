# Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence (string) and the second argument is a list of words (correct_spells). Your function should check each word in the input string against all the words in the correct_spells list and return a string such that:
#
# If a word in the original sentence matches exactly with a word in the correct_spells then the word is not modified and it should be directly copied to the output string.
# if a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single character, then that word should be replaced by the correct word in the correct_spelled list.
# If neither of the two previous conditions is true, then the word in the original string should not be modified and should be directly copied to the output string.
# Notes:
# Do not spell check one or two letter words (copy them directly to the output string).
# In case of a tie use the first word from the correct_spelled list.
# Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
# All characters in the output string should all be in lower case letters.
# Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
# Remove extra spaces between the words.
# Remove spaces at the start and end of the output string.
# Examples:
# Sentence (str)	        correct_spells (list)	                    Function return (str)
# Thes is the Firs cas	        ['that','first','case','car']	            thes is the first case
# programing is fan and eesy    ['programming','this','fun','easy','book']  programming is fun and easy
# Thes is vary essy	        ['this', 'is', 'very', 'very', 'easy']	    this is very easy
# Wee lpve Pythen	        ['we', 'Live', 'In', 'Python']	            we live python
# Notice:
# In the first example 'thes' is not replaced with anything.
# In the first example both 'case' and 'car' could replace the 'cas' in the original sentence, but 'case' is selected because it was encountered first.
# Please notice that this assignment is only an exercise and a real spell checker requires more functionalities.
# Hint: You should use the functions that you developed in part 1 and part 2 to help you solve this problem.
#
# REVISANDO FUNCIONES
# find_mismatch
# First string	Second String	Function return
# dog	        Dog	        0
# Hello There	helloothere	1
# Python	Java	        2
# sin	        sink	        3 (note not the same length)
#
# single_insert_or_delete
# First string	Second String	Function return
# Python	Java	        2
# book          boot	        2
# sin           sink	        1 (Inserting a single character at the end)
# dog           Dog	        0
# poke	        spoke	        1 (Inserting a single character at the start)
# poker	        poke	        1 (Deleting a single character from the end)
# programing	programming	1 (Inserting a single character)
#
def spelling_corrector(s1,s2):
    s1=s1.lower()
    espacio=" "
    s2=espacio.join(s2)
    s2=s2.lower()
    s1=s1.split()
    s2=s2.split()
    print(s1)
    print(s2)
    print("===============================================")
    acum=[]
    for x in s2:
        if x not in acum:
            acum.append(x)
    s2=acum
    correccion=[]

    for x in range(len(s1)):
        for y in range(len(s2)):
            evalua_single_insert_or_delete = single_insert_or_delete(s1[x], s2[y])
            evalua_find_mismatch = find_mismatch(s1[x], s2[y])
            print("indice",x,"cad_1=", s1[x], "cad_2=",s2[y],"error",evalua_find_mismatch,"InsDel",evalua_single_insert_or_delete)
            print(s1,s2)
            if evalua_find_mismatch==0 and evalua_single_insert_or_delete==0:
#                print("indice",x,"cad_1=", s1[x], "cad_2=",s2[y],"error",evalua_find_mismatch,"InsDel",evalua_single_insert_or_delete)
                correccion.append(s1[x])
                break
# 1 diferente 1 caracter, mismo tamaño
# 2 diferentes x caracter, diferente tamaño
# 3 diferentes total

# 1 eliminar 1 inicio o final
# 2 insertar 1 inicio o final
# 3 diferentes total, diferencia mas de 2 caracteres 
            if evalua_find_mismatch==1 and evalua_single_insert_or_delete==3:
#                print("indice",x,"cad_1=", s1[x], "cad_2=",s2[y],"Error",evalua_find_mismatch,"InsDel",evalua_single_insert_or_delete)
                correccion.append(s2[y])
#                s1.replace((s1[x]),"")
                continue
            if evalua_find_mismatch==2 and evalua_single_insert_or_delete==1:
#                print("indice",x,"cad_1=", s1[x], "cad_2=",s2[y],"Error",evalua_find_mismatch,"InsDel",evalua_single_insert_or_delete)
                correccion.append(s2[y])
#                s1.replace((s1[x]),"")
                continue
            if evalua_find_mismatch==2 and evalua_single_insert_or_delete==2:
#                print("indice",x,"cad_1=", s1[x], "cad_2=",s2[y],"Error",evalua_find_mismatch,"InsDel",evalua_single_insert_or_delete)
                correccion.append(s2[y])
#                s1.replace((s1[x]),"")
                continue
#            if evalua_find_mismatch==3 and evalua_single_insert_or_delete==3:
#                print("indice",x,"cad_1=", s1[x], "cad_2=",s2[y],"Error",evalua_find_mismatch,"InsDel",evalua_single_insert_or_delete)
#                correccion.append(s2[y])
                continue

#NO existe s1 en s2
#            for x in range(len(s1)):
#                if s1[x]!=s2[x]:
#                    print("indice",x,"cad_1=", s1[x], "cad_2=",s2[x])
#                    correccion.append(s1[x])
#                    break

#            if len(s1[x])<=2:
#                correccion.append(s1[x])
    espacio=" "
    correccion=espacio.join(correccion)
    print("texto final=>",correccion)

def find_mismatch (s1,s2):
# 0 igual
# 1 diferente 1 caracter, mismo tamaño
# 2 diferente2 x caracter, diferente tamaño    
# 3 diferentes total
    #Return 2
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    #Return 0 / 1
    number_of_mismatches=0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            number_of_mismatches=number_of_mismatches+1
            if number_of_mismatches>1:
                return 3
    return number_of_mismatches

def single_insert_or_delete(s1, s2):
# 0 igual
# 1 eliminar 1 inicio o final
# 2 insertar 1 inicio o final
# 3 diferentes total, diferencia mas de 2 caracteres    
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
s1 = "programing is fan and eesy"
s2 = ['programming','this','fun','easy','book']
evalua_spelling_corrector  = spelling_corrector(s1,s2)
print(evalua_spelling_corrector)
