# Modify the following word_distribution function so that
# it returns a dictionary with the count of each word in 
# the input string.
#
# Don't forget to put the words in lowercase.
#
# If there's a punctuation sign at the end of a word, you should remove it.
# You should remove only one punctuation sign if there are multiple signs.
#
# Tests:
#
# word_distribution("Hello. How are you? Please say hello if you don't love me!") 
# should return {'hello': 2, 'how':1, 'are':1, 'you':2, 'please':1, "don't": 1, 'say':1, 'if':1, 'love':1,'me':1}
#
# word_distribution("That's when I saw Jane (John's sister)!")
# should return {"that's":1, "when":1,"i":1,"saw":1,"jane":1, "(john's":1, "sister)":1}
#
def word_distribution(s, word_list = None):
    s=s.lower()
    s=s.split()
    wordcount = {}
    word_list = list()
    for word in s:
        len_word=len(word)
        if word[len_word-1:len_word].isalpha() == False:
            word=word.replace(word[len_word-1:len_word],"")
        word_list.append(word)

    for word in word_list:
        wordcount[word] = word_list.count(word)
    return wordcount

# OJO SOLO LA FUNCION!!!   
# Main Program #
s = "Hello. How are you? Please say hello if you don't love me!"

evalua_word_distribution = word_distribution(s)
print(evalua_word_distribution)
