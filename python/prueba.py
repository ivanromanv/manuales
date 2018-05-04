# Example of multidimensional list
my_course=[["Ivan",90,87,95],["Flor",92,89,94],["Samuel",99,87,97],["Bruno",90,85,99]]
for student_data in my_course:
    total_grade=0
    for grade_index in range(1,len(student_data)):
        total_grade=total_grade+student_data[grade_index]
    print("El promedio para", student_data[0], "es", total_grade/3.0)
