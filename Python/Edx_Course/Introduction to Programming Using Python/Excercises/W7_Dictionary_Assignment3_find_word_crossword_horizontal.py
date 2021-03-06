# Part 1: Find a word in a crossword (Horizontal)
# 0.0/30.0 puntos (calificados)
# Write a function named find_word_horizontal that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. This function searches the rows of the 2d list to find a match for the word. If a match is found, this functions returns a list containing row index and column index of the start of the match, otherwise it returns the value None (no quotations).
#
# For example if the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
# word='cat'
# find_word_horizontal(crosswords,word)
# then your function should return
# [2,1]
# Notice that the 2d input list represents a 2d crossword and the starting index of the horizontal word 'cat' is [2,1]
#
# s	d	o	g
# c	u	c	m
# a	c	a	t
# t	e	t	k
# Note: In case of multiple matches only return the match with lower row index. If you find two matches in the same row then return the match with lower column index.
#
def find_word_horizontal(crosswords,word):
    word=word.lower()
    for row_index, row in enumerate(crosswords):
        #print('input: ', row_index, row)
        row_string = ''.join(row)
        #print('joined row: ', row_string)
        column_index = row_string.find(word)
        if(column_index > -1):
            return [row_index, column_index]    

# OJO SOLO LA FUNCION!!!   
# Main Program #
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
evalua_find_word_horizontal = find_word_horizontal(crosswords,word)
print(evalua_find_word_horizontal)
