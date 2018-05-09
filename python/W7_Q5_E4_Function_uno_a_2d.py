# Quiz 5, Part 4 (one_to_2D)
# 0.0/20.0 puntos (calificados)
#
# Write a function named one_to_2D which receives an input list and two integers r and c as parameters and returns a new two-dimensional list having r rows and c columns.
#
# Note that if the number of elements in the input list is larger than r*c then ignore the extra elements. If the number of elements in the input list is less than r*c then fill the two dimensional list with the keyword None. For example if your fuction is called as hown below:
#
# one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3)
#
# Then it should return:
#
# [[8, 2, 9],[4, 1, 6]]
#
def one_to_2D(some_list, r, c):
    tamano_lista=len(some_list)
    tamano_matriz=int((r*c)/2)
    matriz=[]
    
    for names in range(0,len(some_list)):
        if tamano_matriz>=tamano_lista:
            return None        
        matriz.append(some_list[0:tamano_matriz])
        matriz.append(some_list[tamano_matriz:tamano_matriz*2])
        break
    return matriz

# OJO SOLO LA FUNCION!!!   
# Main Program #
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
r = 4
c = 4
##
#one_to_2D([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4, 4)
#Your function returns:
#[[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
#The correct return value is:
#[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
##
evalua_one_to_2D = one_to_2D(some_list, r, c)
print(evalua_one_to_2D)