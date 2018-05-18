# Final Exam, Part 3 (N letter dictionary)
# 0.0/20.0 puntos (calificados)
# Write a function named n_letter_dictionary that receives a string (words separated by spaces) as parameter and returns a dictionary whose keys are numbers and whose values are lists that contain unique words that have the number of letters equal to the keys. 
#
# For example, when your function is called as:
#
# n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become")
# Then, your function should return a dictionary such as
# {2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'], 5: ['treat'], 6: ['become', 'people']}
# Notes:
# Each list of words with the same number of letters should be sorted in ascending order
# The words in a list should be unique. For example, even though the word "them" is repeated twice in the above sentence, it is only considered once in the list of four letter words.
# Capitalization does not matter, this means that all the words should be converted to lower case. For example the words "The" and "the" appear in the sentence but they are both considered as lower case "the".
# Do NOT import any module for solving this problem.
#
def n_letter_dictionary(string):
    my_dictionary={}
    string=string.lower()
    string=string.split(' ')
    lista_unica=[]
    #quitando palabras repetidas
    for words in string:
        if words not in lista_unica:
            lista_unica.append(words)
    #Ordenando numericamente por candidad de letras
    #hasta 15 caracteres por palabra
    for k in range(1,15):
        lista_palabras=[]
        n_letter_words=0
        for word in lista_unica:
            #k cantidad de caracteres por palabra
            if len(word)==k:
                n_letter_words=n_letter_words+1
                lista_palabras.append(word)
        if lista_palabras!=[]:
            lista_palabras.sort()
            my_dictionary[k] = lista_palabras
    return my_dictionary

# OJO SOLO LA FUNCION!!!   
# Main
string = "I loved a girl once"

evalua_n_letter_dictionary = n_letter_dictionary(string)
print(evalua_n_letter_dictionary)