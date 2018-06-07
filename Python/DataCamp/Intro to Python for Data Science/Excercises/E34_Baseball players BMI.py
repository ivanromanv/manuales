# The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height and weight. height is in inches and weight is in pounds.
# It's now possible to calculate the BMI of each baseball player. Python code to convert height to a numpy array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game!
#
# height and weight are available as a regular lists
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
    # Import numpy
    import numpy as np
    # Create array from height with correct units: np_height_m
    np_height_m = np.array(height) * 0.0254
    # Create array from weight with correct units: np_weight_kg
    np_weight_kg = np.array(weight) * 0.453592
    # Calculate the BMI: bmi
    bmi = np_weight_kg / np_height_m ** 2
    # Print out bmi
    print(bmi)    
#########################################################################################
# OJO SOLO LA FUNCION!!!   
# El baseball.txt contiene el formato solicitado

file_name='baseball.txt'
evalua_list_from_file = list_from_file(file_name)
print(evalua_list_from_file)




