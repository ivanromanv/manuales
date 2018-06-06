# File I/O Exercise 3
# 0 puntos posibles (no calificados)
# Write a function that takes a file name (string) of a CSV file which contains the information about student's names and their grades for four courses and returns a dictionary that contains information about the students whose grades in both Math and Chemistry is above 70. Note that if the file has any comments (lines starting with #) then you should ignore such a line. The file will have the following format:
#
# #first_name,math,physics,chemistry,biology
# For example if the contents of the file are:
# Luke,89,94,81,97
# Eva,40,50,65,90
# Joseph,55,58,54,99
# Oliver,73,74,89,91
# then your function should return a dictionary such as:
# out_dict = {'Luke': [89.0, 94.0, 81.0, 97.0],
#             'Oliver': [73.0, 74.0, 89.0, 91.0]}
#
def construct_dictionary_from_file_CSV(file_name):
    my_dictionary={}
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        if line.count('#',0,-1) ==0:
            name, course1, course2, course3, course4 = line.strip().split(',')
            if float(course1)>70 and float(course3)>70:
                my_dictionary[name] = [float(course1), float(course2), float(course3), float(course4)]
    return my_dictionary

# OJO SOLO LA FUNCION!!!   
# El archivo3.csv contiene el formato solicitado

file_name='archivo3.csv'
evalua_construct_dictionary_from_file_CSV = construct_dictionary_from_file_CSV(file_name)
print(evalua_construct_dictionary_from_file_CSV)