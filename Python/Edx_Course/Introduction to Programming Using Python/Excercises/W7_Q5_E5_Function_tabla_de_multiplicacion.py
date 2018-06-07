# Quiz 5, Part 5 (multiplication_table)
# 0.0/20.0 puntos (calificados)
# Write a function named multiplication_table that receives a positive integer 'n' as parameter and returns a n by n multiplication table as a two-dimensional list. 
#
# For example if the integer received by the function 'n' is:
#
# 4
# then your program should return a two_dimensional list with 4 rows and 4 columns such as:
# [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
#
def multiplication_table(n):
    matriz=[]
    for sequence in range(1,n+1):
        evalua_multiplication_table_row = multiplication_table_row(sequence, n)
        matriz.append(evalua_multiplication_table_row)
    return matriz
        
def multiplication_table_row(sequence, n):
    fila_matriz=[]
    contador=1
    for number in range(sequence,n*n+1,sequence):
        fila_matriz.append(number)
        if n>contador:
            contador=contador+1
        else:
            break
    return fila_matriz

# OJO SOLO LA FUNCION!!!   
# Main Program #
n = 4
evalua_multiplication_table  = multiplication_table (n)
print(evalua_multiplication_table )