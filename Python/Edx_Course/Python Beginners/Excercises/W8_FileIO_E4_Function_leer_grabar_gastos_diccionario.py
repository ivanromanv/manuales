# File I/O Exercise 4
# 0 puntos posibles (no calificados)
# Write a function that accepts a filename as input argument, the file contains the information about a persons expenses on milk and bread and returns a dictionary that contains exactly the strings 'milk' and 'bread' as the keys and their floating point values in a list as values. Each line of the file may start with a 'm' or a 'b' denoting milk or bread respectively. For example if the contents of the file are:
#
# m 0 0 0
# b 2 5 1
# b 3 5 4
# m 1 0 0
# b 5 3 1
# m 0 1 0
# b 2 4 5
# then your function should return a dictionary such as:
# out_dict = {'milk': [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], 
#            'bread': [[2.0, 5.0, 1.0], [3.0, 5.0, 4.0], [5.0, 3.0, 1.0], [2.0, 4.0, 5.0]]}
#
def construct_dictionary_from_expenses(file_name):
    my_dictionary={}
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    milk = []
    bread = []
    for line in data:
        name, expense1, expense2, expense3 = line.strip().split(' ')
        if name=='m':
            milk.append([float(expense1), float(expense2), float(expense3)])
        else:
            bread.append([float(expense1), float(expense2), float(expense3)])
    my_dictionary['milk'] = milk
    my_dictionary['bread'] = bread
    return my_dictionary    

# OJO SOLO LA FUNCION!!!   
# El archivo4.txt contiene el formato solicitado

file_name='archivo4.txt'
evalua_construct_dictionary_from_expenses = construct_dictionary_from_expenses(file_name)
print(evalua_construct_dictionary_from_expenses)