#Ask the user to type a string
#Print "Dog" if the word "dog" exist in the input string
#Print "Cat" if the word "cat" exist in the input string.
#(if bothj "dog" and "cat" exist in the input string, then you should only print "Dog")
#Otherwise print "None". (pay attention to capitalization)
cadena = input("Insert the string: ")
if "dog" in cadena:
    print("Dog")
elif "cat" in cadena:
    print("Cat")
elif "cat" in cadena and "dog" in cadena:
    print("Dog")    
else:
    print("None")
 
