# Write a function named count_consonants that receives a string as parameter and returns the total count of the consonants in the string. Consonants are all the characters in the english alphabet except for 'a', 'e', 'i', 'o', 'u'. If the same consonant repeats multiple times you should count all of them. Note that capitalization and punctuation does not matter here i.e. a lower case character should be considered the same as an upper case character.
#
def count_consonants(cadena):
   cadena=cadena.lower()
   total_consonantes=int(0)
   consonantes=['a', 'e', 'i', 'o', 'u']
   for x in cadena:
      if x not in consonantes:
         if x!=" ":
            total_consonantes=total_consonantes+1
   return total_consonantes

# OJO SOLO LA FUNCION!!!   
# Main Program #
cadena = "Hercules was a hero"
evalua_count_consonants = count_consonants(cadena)
print(evalua_count_consonants)
