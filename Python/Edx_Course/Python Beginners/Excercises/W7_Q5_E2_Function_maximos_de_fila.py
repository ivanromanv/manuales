# Quiz 5, Part 2 (row_maximums)
# 20/20 puntos (calificados)
# Write a function named row_maximums that accepts a 2-dimensional list of numbers as parameter and returns a dictionary whose values would be the maximum value of each row and whose keys would be the appropriate strings as specified below. 
#
# For example if the function receives the following list:
#
# [[5, 0, 0, 0, 13], [0, 12, 0, 0], [20, 0, 11, 0], [6, 0, 0, 8]]
# then your function should return the dictionary such as:
# {'row 0 max': 13, 'row 1 max': 12, 'row 3 max': 8, 'row 2 max': 20}
# Notes:
# Everything in the keys is separated by one space and the characters are lower cased.
# The 2-dimensional list may have different number of columns in each row.
# The row indicies for the keys should start at 0 and go to n. So your program should work for any number of rows and columns.
# You may not use the built in max() function.
#
def row_maximums(some_multi_dimensional_list):
    fila=0
    dictionary={}
    
    for linea in some_multi_dimensional_list:
        numero_max = linea[0]
        for numero in linea:
            if numero > numero_max :
                numero_max = numero
        texto="row"+" "+str(fila)+" "+"max"
        dictionary[texto]=numero_max
        fila=fila+1
    return dictionary

# OJO SOLO LA FUNCION!!!   
# Main Program #
some_multi_dimensional_list = [[5, 0, 0, 0, 13], [0, 12, 0, 0], [20, 0, 11, 0],  [6, 0, 0, 8]]
evalua_row_maximums = row_maximums(some_multi_dimensional_list)
print(evalua_row_maximums)