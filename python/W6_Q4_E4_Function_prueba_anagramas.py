# Write a function named test_for_anagrams that receives two strings as parameters, both of which consist of alphabetic characters and returns True if the two strings are anagrams, False otherwise. Two strings are anagrams if one string can be constructed by rearranging the characters in the other string using all the characters in the original string exactly once. For example, the strings "Orchestra" and "Carthorse" are anagrams because each one can be constructed by rearranging the characters in the other one using all the characters in one of them exactly once. Note that capitalization does not matter here i.e. a lower case character can be considered the same as an upper case character
#
def test_for_anagrams(my_string1,my_string2):
   my_string1=my_string1.lower()
   my_string2=my_string2.lower()

   if len(my_string1) == len(my_string2):
      contador=0
      for x in my_string2:
         if x not in my_string1:
            return False
         else:
            contador=contador+1
      if contador==len(my_string1):
         return True
   else:
      return False

# OJO SOLO LA FUNCION!!!   
# Main Program #
my_string1 = "doodle"
my_string2 = "poodlx"
evalua_test_for_anagrams = test_for_anagrams(my_string1,my_string2)
print(evalua_test_for_anagrams)
