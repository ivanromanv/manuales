# Write a function that takes a string as input argument and returns a dictionary of letter counts i.e. the keys of this dictionary should be individual letters and the values should be the total count of those letters. You should ignore white spaces and they should not be counted as a character. Also note that a small letter character is equal to a capital letter character.
#
def dictionary_letter_count(sample_string):
    sample_string=sample_string.lower()
    sample_string=sample_string.replace(" ","")
    dictionary = {}
    vocales = ['a','e','i','o','u']
    for letra in sample_string:
        for vocal in vocales:
            if vocal==letra:
                dictionary[letra] = sample_string.count(vocal)
    return dictionary

# OJO SOLO LA FUNCION!!!   
# Main Program #
sample_string = 'Esta es una prueba para conteo de letras'
evalua_dictionary_letter_count = dictionary_letter_count(sample_string)
print(evalua_dictionary_letter_count)
