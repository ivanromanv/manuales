#  Final Exam, Part 6 (Dictionary of word counts)
# 0.0/20.0 puntos (calificados)
#
# Write a function that takes a string of words as input argument and returns a dictionary of word counts. The keys of this dictionary should be the unique words and the values should be the total count of those words. Assume that characters are not case sensitive. For example if the input string is :
#
# "I am tall when I am young and I am short when I am old" 
#
# Then the output should be:
#
# {'short': 1, 'young': 1, 'am': 4, 'when': 2, 'tall': 1, 'i': 4, 'and': 1, 'old': 1} 
#
def diccionario_conteo_palabras(string_text):
    my_diccionary={}
    string_text=string_text.lower()
    string_text=string_text.strip().split(' ')
    
    lista_unicos=[]
    for unicos in string_text:
        if unicos not in lista_unicos:
            lista_unicos.append(unicos)
    
    for word in lista_unicos:
        contador=0
        for palabra in string_text:
            if word==palabra:
                contador=contador+1
#        print(word,"esta",contador,"veces")
        my_diccionary[word]=contador
    return my_diccionary

# OJO SOLO LA FUNCION!!!   
# Main
string_text = "I am tall when I am young and I am short when I am old" 

evalua_diccionario_conteo_palabras = diccionario_conteo_palabras(string_text)
print(evalua_diccionario_conteo_palabras)