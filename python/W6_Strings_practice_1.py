# Write a function which accepts an input string and returns a string
# and count words of the input string
#Version 1
def funcion_n_contar_words(input_string, n):
    words=input_string.split()
    n_letter_words=0
    for word in words:
        if len(word)==n:
            n_letter_words=n_letter_words+1
    return n_letter_words
           
# OJO SOLO FUNCION!!!
# Main Program #
input_string = "Espero que tengamos todos un lindo dia lleno de alegria"
total_words=0
for k in range(1,11):
    x = funcion_n_contar_words(input_string, k)
    total_words=total_words+x
    print("There are",x,"words with",k,"characters")
print("****\nThere are total of:",total_words,"words")
