# You have another look at the MLB data and realize that it makes more sense to restructure all this information in a 2D numpyarray. This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns (for height and weight).
#The MLB was, again, very helpful and passed you the data in a different structure, a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this embedded list is baseball.
#Can you store the data as a 2D array to unlock numpy's extra functionality?
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
    # baseball is available as a regular list of lists

    # Import numpy package
    import numpy as np
    # Create a 2D numpy array from baseball: np_baseball
    np_baseball = np.array(data)
    # Print out the shape of np_baseball
    print(np_baseball.shape)
    
#########################################################################################
# OJO SOLO LA FUNCION!!!   
# El baseball.txt contiene el formato solicitado

file_name='baseball.txt'
evalua_list_from_file = list_from_file(file_name)
print(evalua_list_from_file)








