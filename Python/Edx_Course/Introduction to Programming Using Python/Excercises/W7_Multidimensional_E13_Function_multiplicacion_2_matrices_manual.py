# Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product. Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the same as the number of rows of the second matrix(b). Do NOT use numpy module for this exercise. The input for this function will be two 2 Dimensional lists. For example if the input lists are:
#
# a = [[2, 3, 4], [3, 4, 5]]
# b = [[4, -3, 12], [1, 1, 5], [1, 3, 2]]
# Then your function should return their product such as:
# [[15, 9, 47], [21, 10, 66]] 
###
# NO NUMPY
###
def multiplication_2_matrices_manual(matrix_a,matrix_b):
    final_list=[]
    evalua_check_multiplication_2_matrices = check_multiplication_2_matrices(matrix_a,matrix_b)
    if evalua_check_multiplication_2_matrices == True:
        output_list=[]
        temp_row=len(matrix_b[0])*[0]
        for r in range(len(matrix_a)):
            output_list.append(temp_row[:])
        for row_index in range(len(matrix_a)):
            for col_index in range(len(matrix_b[0])):
                sum=0
                for k in range(len(matrix_a[0])):
                    sum=sum+matrix_a[row_index][k]*matrix_b[k][col_index]
                output_list[row_index][col_index]=sum
    return output_list
    
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
evalua_multiplication_2_matrices_manual = multiplication_2_matrices_manual(matrix_a,matrix_b)
print(evalua_multiplication_2_matrices_manual)
