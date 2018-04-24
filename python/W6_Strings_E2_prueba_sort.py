# Write a function that takes a list of words as an input argument and returns True if the list is sorted and returns False otherwise.
#
def funcion_palabras_ordenadas(input_list):
    output_list = []
    for x in input_list:
        output_list.append(x)
    output_list.sort()
#    print(input_list, output_list) 
    if input_list==output_list:
        return True
    else:
        return False
  
# OJO SOLO FUNCION!!!
# Main Program #
#input_list = ['Ivan','Flor','Bruno','Samuel']
input_list = ['Bruno','Flor','Ivan','Samuel']
evalua_funcion_palabras_ordenadas = funcion_palabras_ordenadas(input_list)
print(evalua_funcion_palabras_ordenadas)
