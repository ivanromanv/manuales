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
    fp=open(filename,'r')
    lines=fp.readlines()
    fp.close()
    average_q=0
    average_a=0    
    for line in lines:
        average_quiz=[]
        average_assign=[]        
        elements=line.strip().split(",")
        current_key=elements[0].strip()
        average_quiz.append(int(elements[1]))
        average_quiz.append(int(elements[2]))
        average_quiz.append(int(elements[3]))
        average_quiz.append(int(elements[4]))
        average_quiz.append(int(elements[5]))
        average_quiz.append(int(elements[6]))
        average_assign.append(int(elements[7]))
        average_assign.append(int(elements[8]))
        average_assign.append(int(elements[9]))
        average_assign.append(int(elements[10]))            
        average_quiz.sort()
        average_assign.sort()
        average_quiz.pop(0)
        average_quiz.pop(0)
        average_assign.pop(0)
        average_q=(sum(average_quiz))/4
        average_a=(sum(average_assign))/3
        totalscore=int(average_q+average_a+int(elements[11])+int(elements[12]))/4
        if totalscore>=60:
            mensaje="pass"
        else:
            mensaje="fail"
        grade_dict[current_key]=mensaje
    return grade_dict

# OJO SOLO LA FUNCION!!!   
# Main
filename = "final_exam.txt"

evalua_my_final_grade_calculation = my_final_grade_calculation(filename)
print(evalua_my_final_grade_calculation)