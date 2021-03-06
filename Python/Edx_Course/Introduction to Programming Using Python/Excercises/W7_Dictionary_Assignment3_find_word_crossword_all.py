# Part 3: Find a word in a crossword
# 0.0/40.0 puntos (calificados)
# Write a function named capitalize_word_in_crossword that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. This function searches the rows and columns of the 2d list to find a match for the word. If a match is found, this functions capitalizes the matched characters in 2-dimensional list and returns the list. If no match is found, this function simply returns the origianl 2-dimensional list with no modification.
#
# Example 1: If the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
# word='cat'
# capitalize_word_in_crossword(crosswords,word)
# then your function should return:
# [['s','d','o','g'],['C','u','c','m'],['A','x','a','t'],['T','e','t','k']]
# Notice that the above list is a representation for a 2-dimensional crossword puzzle as shown below.
# s	d	o	g
# C	u	c	m
# A	x	a	t
# T	e	t	k
# Example 2: if the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
# word='cat'
# capitalize_word_in_crossword(crosswords,word)
# then your function should return:
# [['s','d','o','g'],['c','u','c','m'],['a','C','A','T'],['t','e','t','k']]
# Notice that the above list is a representation for a 2-dimensional crossword puzzle as shown below.
# s	d	o	g
# c	u	c	m
# a	C	A	T
# t	e	t	k
# Note: If both a horizontal and a vertical match is found then only select the horizontal match. For example, in the above case there is a horizontal match starting at [2,1] and there is also a veritcal match starting at [1,0]. Notice that only the characters in the horizontal match should be capitalized in the returned list.
# Hint: You should use the functions that you developed in part 1 and part 2 as helper functions for part 3.
#
def find_word_horizontal(crossword,word):
    if not crossword or not word:
        return None
    for index,row in enumerate(crossword):
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None

def find_word_vertical(crossword,word):
    if not crossword or not word:
        return None    
    number_of_columns=len(crossword[0])
    for col_index in range (number_of_columns):
        temp_str=''
        for row_index in range(len(crossword)):
            temp_str=temp_str+crossword[row_index][col_index]
        if temp_str.find(word)>=0:
            return [temp_str.find(word),col_index]
    return None

def capitalize_word_in_crossword(crossword,word):
    if not crossword or not word:
        return None    
    found_position= find_word_horizontal(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]][found_position[1]+k]=crossword[found_position[0]][found_position[1]+k].upper()
        return crossword 
    found_position= find_word_vertical(crossword,word)
    if found_position:
        for k in range(len(word)):
            crossword[found_position[0]+k][found_position[1]]=crossword[found_position[0]+k][found_position[1]].upper()
    return crossword
    
# OJO SOLO LA FUNCION!!!   
# Main Program #
# [['a', 'b'], ['c', 'd']] y b = [['a', 'B'], ['c', 'd']]
crossword=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
evalua_capitalize_word_in_crossword = capitalize_word_in_crossword(crossword,word)
print(evalua_capitalize_word_in_crossword)
