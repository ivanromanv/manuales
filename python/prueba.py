# First string	Second String	Function return
# Python	Java	        2
# book          boot	        2
# sin           sink	       * 1 (Inserting a single character at the end)
# dog           Dog	       * 0
# poke	        spoke	       * 1 (Inserting a single character at the start)
# poker	        poke	       * 1 (Deleting a single character from the end)
# programing	programming	1 (Inserting a single character)

# RESOLUCION DEL INSTRUCTOR
def single_insert_or_delete(s1, s2):
    s1=s1.lower()
    s2=s2.lower()

    #Return 0
    if s1==s2:
        return 0
    #Return 3
#    if abs(len(s1)-len(s2))!=1:
#        return 3
    #Return 1 / 2

    if len(s1)==len(s2):
        n=0
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                n=n+1
        if n>=2:
            return 3
    return 4
  
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
# 0 igual
# 1 eliminar 1 caracter inicio o final o en medio
# 2 insertar 1 caracter inicio o final o en medio
# 3 diferencia mas de 2 caracteres
# 4 diferencia 1 caracter inicio o final mismo tamaño

s1 = "bott"
s2 = "botx"
evalua_single_insert_or_delete = single_insert_or_delete(s1,s2)
print(evalua_single_insert_or_delete)
