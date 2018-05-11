# File I/O Exercise 1
# 0 puntos posibles (no calificados)
# Write a function that accepts a filename as input argument and reads the file and saves each line of the file as an element in a list (without the new line ("\n")character) and returns the list. Each line of the file has comma separated values: For example if the content of the file looks like this:
#
# Lucas,Turing,22
# Alan,Williams,27
# Layla,Trinh,21
# Brayden,Huang,22
# Oliver,Greek,20
# then your function should return a list such as
# ['Lucas,Turing,22', 'Alan,Williams,27', 'Layla,Trinh,21', 'Brayden,Huang,22', 'Oliver,Greek,20']
# Please read the "File I/O Exercise Notes" before you attempt to write code.
#
# The first few lines of the code is there to help you!
#
def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    #data = file_pointer.readlines()
    data=file_pointer.readlines()
    #print(my)
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    largo=len(data)
    contador=0
    new_list=[]
    while contador < largo:
        cambio=data[contador].replace("\n","")
        new_list.append(cambio)        
        contador=contador+1
    return new_list

# OJO SOLO LA FUNCION!!!   
# archivo.txt, debe contener
# ['Lucas,Turing,22\n','#Alan,Williams,27\n','#Layla,Trinh,21\n','#Brayden,Huang,22\n','#Oliver,Greek,20\n']

file_name='archivo.txt'
evalua_list_from_file = list_from_file(file_name)
print(evalua_list_from_file)