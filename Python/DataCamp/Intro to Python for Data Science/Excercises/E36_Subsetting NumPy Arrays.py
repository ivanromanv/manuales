# You've seen it with your own eyes: Python lists and numpyarrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:
# x = ["a", "b", "c"]
# x[1]
#
# np_x = np.array(x)
# np_x[1]
# The script on the right already contains code that imports numpy as np, and stores both the height and weight of the MLB players as numpy arrays.
#
def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    #data = file_pointer.readlines()
    data=file_pointer.readlines()
    #print(my)
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    #my_dictionary = {}
    np_height = []
    np_weight = []
    for line in data:
        if line.count('#',0,-1) == 0:
            name, team, position, height, weight, age, posCategory = line.strip().split(',')
            np_height.append(int(height))
            np_weight.append(int(weight))
    height=np_height
    weight=np_weight
###############################################################################################
### CODIGO REAL PARA PROCESAR ARCHIVO baseball.txt    
###############################################################################################    
    # height and weight are available as a regular lists

    # Import numpy
    import numpy as np
    # Store weight and height lists as numpy arrays
    np_weight = np.array(weight)
    np_height = np.array(height)
    # Print out the weight at index 50
    print(np_weight[50])
    # Print out sub-array of np_height: index 100 up to and including index 110
    print(np_height[100:111])
 
#########################################################################################
# OJO SOLO LA FUNCION!!!   
# El baseball.txt contiene el formato solicitado

file_name='baseball.txt'
evalua_list_from_file = list_from_file(file_name)
print(evalua_list_from_file)







