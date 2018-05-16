# Part 2: Print grades
# 0.0/50.0 puntos (calificados)
# Write a function called print_grades that accepts the name of a file (string) as input argument. Assuming the format of the file is the same as the file in part 1, your function should call the function that you developed in part 1 to read the file and create the grades dictionary. Using the grades dictionary, your function should print the names, grades, and averages of students with the exact format shown below. Notice that you are asked to write a function (NOT a program) and that function prints the grades. Your function should return None after printing the grades.
#
# Sample Input file:
#
# 1000123456, Rubble, Test_3,  80, Test_4 , 80, quiz , 90
# 1000123210, Bunny, Test_2, 100, Test_1, 100,Test_3   , 100 ,Test_4 , 100
# 1000123458, Duck, Test_1, 86, Test_5   , 100 , Test_2 ,93 ,Test_4, 94
# Your program's output should be:
#
#     ID     |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |  Avg.  |
# 1000123210 | Bunny            |    100 |    100 |    100 |    100 | 100.00 |
# 1000123456 | Rubble           |      0 |      0 |     80 |     80 |  40.00 |
# 1000123458 | Duck             |     86 |     93 |      0 |     94 |  68.25 |
# Notes:
# Column titles are all centered
# The printed output is sorted in ascending order based on the student IDs
# Each column is seperated from a neighboring column(s) by three characters ' | ' (space vertical_bar space).
# IDs are always 10 characters and they are left justified (not counting the boundary characters)
# Names are left justified (maximum of 16 characters, not counting the boundary characters).
# Grades and averages are right justified. The width of the columns for the grades and averages is 6 characters (not counting the boundary characters).
# Averages are right justified with two digits of accuracy after the decimal point.
# Hint: Use the function which you developed in part 1 to read the input file and create a dictionary. Use .format() to format the output.
#
def create_grades_dict(file_name):
    # insert the code from your function in part 1 here
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

# Your main program starts below this line
def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict=create_grades_dict(file_name)
    cabecera = "{0:^11s}|{1:^18s}|{2:^8s}|{3:^8s}|{4:^8s}|{5:^8s}|{6:^8s}|".format("ID","Name","Test_1","Test_2","Test_3","Test_4","Avg.")
    print(cabecera)
    keys = tuple(grades_dict.keys())
    values = tuple(grades_dict.values())
    for id in sorted(grades_dict.keys()):
        detalle="{0:<11s}| {1:<17s}|{2: >7d} |{3: >7d} |{4: >7d} |{5: >7d} |{6:>7.2f} |".format(id,grades_dict[id][0],grades_dict[id][1],grades_dict[id][2],grades_dict[id][3],grades_dict[id][4],grades_dict[id][5])
        print(detalle)
        
# OJO SOLO LA FUNCION!!!   
# Main Program #
file_name='student_grades.txt'
evalua_print_grades = print_grades(file_name)
print(evalua_print_grades)
