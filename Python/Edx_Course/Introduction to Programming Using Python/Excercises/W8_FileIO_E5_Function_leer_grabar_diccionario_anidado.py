# File I/O Exercise 5
# 0 puntos posibles (no calificados)
# Write a function that accepts a file name as input argument and constructs and returns a nested dictionary from it. The keys of this dictionary should be last names, and the values should be dictionaries that contain first names as the keys and integer ages as the values. Note that the data may contain multiple people with the same last name, but it will have unique first names. Ignore any lines that start with '#' The file will contain comma separated values (CSV) For example if the contents of the file are:
#
# #first_name,last_name,age
# Matthew,Abbey,65
# Chloe,Orion,49
# Yohaan,Adams,54
# Krishna,Adams,35
# Resa,Orion,86
# Lucas,Abbey,60
# Courtney,Abbey,67
# Joseph,Orion,45
# Mark,Abbey,60
# Eva,Orion,76
# then your function should return a dictionary such as:
# {'Abbey': {'Matthew': 65, 'Courtney': 67, 'Lucas': 60, 'Mark': 60},
#  'Orion': {'Chloe': 49, 'Resa': 86, 'Eva': 76, 'Joseph': 45},
#  'Adams': {'Krishna': 35, 'Yohaan': 54}}
#
def construct_dictionary_nested_from_file(file_name):
    my_dictionary={}
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()

    for line in data:
        if line[0] != "#":
            # Split the line with the delimiter comma (',')
            first_name, last_name, age = line.strip().split(',')
            if last_name not in my_dictionary:
                my_dictionary[last_name] = {first_name: int(age)}
            else:
                if first_name not in my_dictionary[last_name]:
                    my_dictionary[last_name][first_name] = int(age)
    return my_dictionary    

# OJO SOLO LA FUNCION!!!   
# El archivo5.txt contiene el formato solicitado

file_name='archivo5.txt'
evalua_construct_dictionary_nested_from_file = construct_dictionary_nested_from_file(file_name)
print(evalua_construct_dictionary_nested_from_file)