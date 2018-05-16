# Quiz 6, Part 3
# 0.0/20.0 puntos (calificados)
# Write a function named calculate_grades that receives a file name. The file contains names of students and their grades for 4 quizzes and returns a tuple as specified below. Each line of the file will have the following format:
#
# name,quiz1_score,quiz2_score,quiz3_score,quiz4_score
# For example if the contents of the file are:
# john,89,94,81,97
# eva,40,45,65,90
# joseph,0,0,54,99
# tim,73,74,89,91
# The name and grades are separated by commas. Your function should return the names of the student and their quiz averages as a tuple of tuples as shown below:
# (('eva', 60.0), ('john', 90.25), ('joseph', 38.25), ('tim', 81.75))
# The tuples should be sorted in ascending order by the student's name.
# Please read the "File I/O Exercise Notes" before you attempt to write code.
#
def calculate_grades(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    for students in data:
        print(students)
    
# OJO SOLO LA FUNCION!!!   
# Main Program #
# El archivo6.txt contiene el formato solicitado
    
file_name='archivo6.txt'    
evalua_calculate_grades = calculate_grades(file_name)
print(evalua_calculate_grades)