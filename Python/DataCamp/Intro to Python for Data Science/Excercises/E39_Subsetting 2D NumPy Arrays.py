# If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.
# regular list of lists
# x = [["a", "b"], ["c", "d"]]
# [x[0][0], x[1][0]]
#
# numpy
# import numpy as np
# np_x = np.array(x)
# np_x[:,0]
# If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.
# regular list of lists
# x = [["a", "b"], ["c", "d"]]
# [x[0][0], x[1][0]]
#
# numpy
# import numpy as np
# np_x = np.array(x)
# np_x[:,0]
#
# For regular Python lists, this is a real pain. For 2D numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.
# The code that converts the pre-loaded baseball list to a 2D numpy array is already in the script. The first column contains the players' height in inches and the second column holds player weight, in pounds. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0!
#
#
def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    #data = file_pointer.readlines()
    data=file_pointer.readlines()
    print(data)
    #print(my)
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    #my_dictionary = {}

#    baseball = []
#    for line in data:
#        if line.count('#',0,-1) == 0:
#            line=line.replace("\n","")
#            name, team, position, height, weight, age, posCategory = line.strip().split(',')
#            baseball.append(line)
#    #baseball = list_from_file(file_name='baseball.txt')
    
###############################################################################################
### CODIGO REAL PARA PROCESAR ARCHIVO baseball.txt    
###############################################################################################    
    # baseball is available as a regular list of lists

    # Import numpy package
    import numpy as np
    # Create np_baseball (2 cols)
    np_baseball = np.array(baseball)
    # Print out the 50th row of np_baseball
    print(np_baseball[49,:])
    # Select the entire second column of np_baseball: np_weight
    np_weight = np_baseball[:,1]
    print(np_weight)
    # Print out height of 124th player
    print(np_baseball[123,0])
#########################################################################################
# OJO SOLO LA FUNCION!!!   
# El baseball.txt contiene el formato solicitado

file_name='baseball.txt'
evalua_list_from_file = list_from_file(file_name)
print(evalua_list_from_file)

