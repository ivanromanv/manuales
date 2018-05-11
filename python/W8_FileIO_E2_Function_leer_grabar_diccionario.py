# File I/O Exercise 2
# 0 puntos posibles (no calificados)
# Write a function that accepts a filename(string) of a CSV file which contains the information about student's names and their grades for four courses and returns a dictionary of the information. The keys of the dictionary should be the name of the students and the values should be a list of floating point numbers of their grades. For example, if the content of the file looks like this:
#
# Mark,90,93,60,90
# Abigail,84,50,72,75
# Frank,46,83,53,79
# Yohaan,47,77,74,96
# then your function should return a dictionary such as:
# out_dict = {'Frank': [46.0, 83.0, 53.0, 79.0],
#            'Mark': [90.0, 93.0, 60.0, 90.0],
#            'Yohaan': [47.0, 77.0, 74.0, 96.0],
#            'Abigail': [84.0, 50.0, 72.0, 75.0]}
#
def construct_dictionary_from_file(file_name):
    my_dictionary={}
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        name, course1, course2, course3, course4 = line.strip().split(',')
        my_dictionary[name] = [float(course1), float(course2), float(course3), float(course4)]
        return my_dictionary    

# OJO SOLO LA FUNCION!!!   
# archivo.txt, debe contener
# ['Mark,90,93,60,90','Abigail,84,50,72,75','Frank,46,83,53,79','Yohaan,47,77,74,96']

file_name='archivo2.txt'
evalua_construct_dictionary_from_file = construct_dictionary_from_file(file_name)
print(evalua_construct_dictionary_from_file)