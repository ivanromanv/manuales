# Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product. Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the same as the number of rows of the second matrix(b). Hint: You may import and use the numpy module but your return must be a python list not a numpy array. The input for this function will be two 2 Dimensional lists. For example if the input lists are:
#
# a = [[2, 3, 4], [3, 4, 5]]
# b = [[4, -3, 12], [1, 1, 5], [1, 3, 2]]
# Then your function should return their product such as:
# [[15, 9, 47], [21, 10, 66]] 
###
# INSTALAR LAS LIBRERIAS
# pip install numpy
# pip install matplotlib
###
import numpy as np
def multiplication_2_matrices(matrix_a,matrix_b):
    final_list=[]
    evalua_check_multiplication_2_matrices = check_multiplication_2_matrices(matrix_a,matrix_b)
    if evalua_check_multiplication_2_matrices == True:
        resultado = np.dot(matrix_a,matrix_b)
        final_list.append(resultado.tolist())
        return final_list[0]
    
def check_multiplication_2_matrices(matrix_a,matrix_b):
    new_list = []
    filas=len(matrix_a[0])
    
    for columns in matrix_b:
        columnas=len(matrix_b[0])
    
    if filas==columnas:
        return True
    else:
        return False

# OJO SOLO LA FUNCION!!!   
# Main Program #
matrix_a = [[2, 3, 4], [3, 4, 5]]
matrix_b = [[4, -3, 12], [1, 1, 5], [1, 3, 2]]
evalua_multiplication_2_matrices = multiplication_2_matrices(matrix_a,matrix_b)
print(evalua_multiplication_2_matrices)
