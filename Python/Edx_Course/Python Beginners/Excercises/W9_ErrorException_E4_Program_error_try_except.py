# Errors and Exceptions Exercise 4
# 0 puntos posibles (no calificados)
# Write a program that asks the user for an input and tries to handle the error that may occur when you try to type cast the input to an int using the try ... except ... else clause. Your function should print the result if the operation is successful, if the operation is not successful your program should print 'Error'
#
# Main
value = input("Enter the string for resolve error: ")
try:
    value = int(value)
except ValueError:
    print("Error")
else:
    print(value)
