# Part 1: Read file and create dictionary
# 0.0/50.0 puntos (calificados)
# Write a function named create_grades_dict that accepts a string as the name of a file. Assuming that the file is a text file which includes name and grades of students, your function should read the file and return a dictionary with the exact format as shown below: The format of the input file is:
#
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# .... 
# An example of the input file is shown below. Sample Input Output Assuming that the input file "student_grades.txt" contains the following text:
# 1000123456, Rubble, Test_3,  80, Test_4 , 80
# 1000123459, Chipmunk, Test_4, 96, Test_1, 86 , Quiz_1 , 88
# Notes:
# Items are seperated by comma and one or more spaces may exist between the items.
# The "ID" of each student is unique. Two students may have the same Name (but IDs will be different)
# The "Name" of each student will only include a last name with no punctuation. Maximum of 15 characters.
# There will be an integer grade for each test (0-100)
# There are only four valid tests, i.e. Test_1, Test_2, Test_3, Test_4. There may be other grades in the file and you should ignore those grades.
# Each student may have missing grade(s) for the tests. A missing grades should be considered as 0.
# Grades may not be in order i.e. Test_3 may appear before Test_1.
# Your function should read the input file, calculate the average test grade for each student and return a dictionary with the following format:
# {'Student_ID':[Last_name,Test_1_grade,Test_2_grade,Test_3_grade,Test_4_grade,average], ...}
# For example in the case of sample input file shown above, your function should return the following dictionary:
# {'1000123456': ['Rubble', 0, 0, 80, 80, 40.0], '1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}
#
def create_grades_dict(file_name):
    grade_dict={}
    tests=['Test_1','Test_2','Test_3','Test_4']
    fp=open(file_name,'r')
    lines=fp.readlines()
    fp.close()
    for line in lines:
        elements=line.strip().split(",")
        if elements and elements[0]:
            current_key=elements[0].strip()
            if len(current_key)==10:
                if grade_dict.get(current_key)==None:
                    # Key does not exist. Create it
                    grade_dict[current_key]=[elements[1].strip(),0,0,0,0,0]                
                for index in range(2,len(elements),2):
                    current_element=elements[index].strip()
                    if  current_element in tests:
                        grade_dict[current_key][int(current_element[-1])]=int(elements[index+1])
                grade_dict[current_key][5]=sum(grade_dict[current_key][1:5])/4.0
    return grade_dict
    
# OJO SOLO LA FUNCION!!!   
# Main Program #
file_name='student_grades.txt'
evalua_create_grades_dict = create_grades_dict(file_name)
print(evalua_create_grades_dict)
