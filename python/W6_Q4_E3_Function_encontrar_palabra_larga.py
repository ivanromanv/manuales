# Write a function named find_longest_word that receives a string as parameter and returns the longest word in the string. Assume that the input to this function is a string of words consisting of alphabetic characters that are separated by space(s). In case of a tie between some words return the last one that occurs.
#
def find_longest_word(cadena):
   #cadena=cadena.lower()
   cadena=cadena.split()
   palabra=""
   contador=[]
   for x in cadena:
      contador.append(len(x))
   mayor=max(contador)
   cantidad=contador.count(mayor)
   tope=0
   
   for word in cadena:
      if len(word)==mayor:
         tope=tope+1
         if tope==cantidad:
            return word

# OJO SOLO LA FUNCION!!!   
# Main Program #
cadena = "brahman the mysterious of the univERsity"
evalua_find_longest_word = find_longest_word(cadena)
print(evalua_find_longest_word)
