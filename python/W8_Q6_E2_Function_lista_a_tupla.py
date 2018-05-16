# Quiz 6, Part 2
# 0.0/20.0 puntos (calificados)
# Write a function named list_to_tuples that receives a two dimensional list of strings as parameter and returns a tuple of tuples where the content of each inner list is reversed as shown below: For example if the two dimensional list received by the function is
#
# [['mean', 'really', 'is', 'jean'], ['world', 'my', 'rocks', 'python']]
# Then, your function should return a tuple of tuples as shown below:
# (('jean', 'is', 'really', 'mean'), ('python', 'rocks', 'my', 'world'))
#
def list_to_tuples(MY_LIST):
    new_list=[]
    for items in MY_LIST:
        items=reversed(items)
        items=tuple(items)
        new_list.append(items)
    new_list=tuple(new_list)
    return(new_list)
    
# OJO SOLO LA FUNCION!!!   
# Main Program #
MY_LIST = [['mean', 'really', 'is', 'jean'], ['world', 'my', 'rocks', 'python']]
evalua_list_to_tuples = list_to_tuples(MY_LIST)
print(evalua_list_to_tuples)