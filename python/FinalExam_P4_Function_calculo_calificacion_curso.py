# Final Exam, Part 4 (Calculate your grade for this course)
# 0.0/20.0 puntos (calificados)
# Write a function named my_final_grade_calculation that receives a file name and returns a dictionary that tells whether a student in this course passed or failed based on the following criteria. 
#
# Each line of the file will have the format:
#
# name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final
# where
# name is a string
# q1 through q6 are quiz scores (integers)
# a1 through a4 are assignment scores (integers values)
# midterm is midterm score (integer)
# final is final exam score (integer)
# For example, if the content of the file looks like this:
# tom, 10, 20, 0, 100, 0, 100, 70, 80, 90, 0, 80, 85
# mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85
# joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5
# Note that there may be additional spaces between the entries in each line. 
#
# Your function should return a dictionary such as:
# {"tom":"pass", "mary":"pass", "joan":"fail"} 
# Notes:
# Two of the lowest quizzes should be dropped and the average of the remaining four quizzes is worth 25% of the total grade.
# The lowest assignment score should be dropped and the average of the remaining three assignments is worth 25% of the total grade.
# Midterm and final exams are each 25% of the total grade.
# Calculate the total score of the student and if the total score is greater than or equal to 60 (totalscore >= 60) then the student has passed. Notice that the keys (names) and the values (pass or fail) of the dictionary should be all lower cased with no spaces in any of them.
#
# insert the code from your function in part 1 here
def my_final_grade_calculation(filename):
    grade_dict={}
    tests=['Quiz_1','Quiz_2','Quiz_3','Quiz_4','Quiz_5','Quiz_6','Assing_1','Assing_2','Assing_3','Assing_4','Midterm','Final_Exam']
    fp=open(filename,'r')
    lines=fp.readlines()
    fp.close()
    for line in lines:
        elements=line.strip().split(",")
        if elements and elements[0]:
            current_key=elements[0].strip()
            suma=0
            #if grade_dict.get(current_key)==None:
                # Key does not exist. Create it
                #grade_dict[current_key]=[elements[1].strip(),0,0,0,0,0,0,0,0,0,0,0,0,0]
            #    grade_dict[current_key]=[0,0,0,0,0,0,0,0,0,0,0,0,0.0]
            for index in range(2,len(elements),1):
                current_element=elements[index].strip()
                if current_element not in tests:
                    #grade_dict[current_key][int(current_element[-1])]=int(elements[index+1])
                    rango=sum(elements[1:13])
                    #suma=(grade_dict[current_element][1:12])/12
                    #suma=suma+int(current_element)
            print(rango)
            print(int(suma/12))
                    
            #grade_dict[current_key][13]=sum(grade_dict[current_key][1:13])/12.0
    return grade_dict

# OJO SOLO LA FUNCION!!!   
# Main
filename = "final_exam.txt"

evalua_my_final_grade_calculation = my_final_grade_calculation(filename)
print(evalua_my_final_grade_calculation)