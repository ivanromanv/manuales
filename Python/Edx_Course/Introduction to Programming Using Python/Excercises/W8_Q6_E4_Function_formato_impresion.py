# Quiz 6, Part 4
# 0.0/20.0 puntos (calificados)
# Write a function named formatted_print that receives a dictionary as argument. The keys of the dictionary will be the names of the students and the values of the dictionary will be their average scores. Your function should print this information exactly as specified below : 
#
# For example if the dictionary received by the function is
#
# {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900} 
# Then your function should print:
# alex       90.55
# eva        88.50
# tim        65.90
# john       34.48
# Note:
# The names have to be accommodated within 10 spaces and they are left justified.
# The scores are floats and they should be right justified in 6 spaces with two digits after the decimal point.
# All this information has to be sorted (descending order) by the scores of the students. Notice how alex has the highest score and appears first and john has the lowest score and appears last.
#
def formatted_print(my_dictionary):
    new_list=[]
    #convertir diccionario a lista
    for datos in (my_dictionary.items()):
        new_list.append(datos)
    #Ordenar lista por segundo termino llamado segundo_key
    new_list = sorted(new_list, key=segundo_key, reverse=True)
    for lista in new_list:
        format_print="{0:<10s}{1:>6.2f}".format(lista[0],lista[1])
        print(format_print)

def segundo_key(elemento):
    return elemento[1]
        
# OJO SOLO LA FUNCION!!!   
# Main Program #
    
my_dictionary={'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}    
evalua_formatted_print = formatted_print(my_dictionary)
print(evalua_formatted_print)