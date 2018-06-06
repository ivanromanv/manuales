# Quiz 6, Part 5
# 0.0/20.0 puntos (calificados)
# Write a function named calculate_expenses that receives a filename as argument. The file contains the information about a person's expenses on items. Your function should return a list of tuples sorted based on the name of the items. Each tuple consists of the name of the item and total expense of that item as shown below:
#
# milk,2.35
# bread , 1.95
#  chips ,    2.54
# milk  ,    2.38
# milk,2.31
# bread,    1.90
#
#
# Notice that each line of the file only includes an item and the purchase price of that item separated by a comma. There may be spaces before or after the item or the price. Then your function should read the file and return a list of tuples such as:
# [('bread', '$3.85'), ('chips', '$2.54'), ('milk', '$7.04')]
# Notes:
# Tuples are sorted based on the item names i.e. bread comes before chips which comes before milk.
# The total expenses are strings which start with a $ and they have two digits of accuracy after the decimal point.
# Hint: Use "${:.2f}" to properly create and format strings for the total expenses.
#
# Please read the "File I/O Exercise Notes" before you attempt to write code.
#
def calculate_expenses(filename):
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!    
    
    my_dictionary = {}
    for line in data:
        line = line.strip().split(',')
        my_item = line[0].strip()
        my_price = float(line[1].strip())
          
        if my_item not in my_dictionary:
            my_dictionary[my_item] =  my_price
        else:
            my_dictionary[my_item] +=  my_price
    my_list = []
    my_keys = sorted(my_dictionary.keys())
    for x in my_keys:
        my_list.append((x,"${0:.2f}".format(my_dictionary[x])))
    return my_list
        
# OJO SOLO LA FUNCION!!!   
# Main Program #
# El archivo7.txt contiene el formato solicitado
    
filename='archivo7.txt'
evalua_calculate_expenses = calculate_expenses(filename)
print(evalua_calculate_expenses)