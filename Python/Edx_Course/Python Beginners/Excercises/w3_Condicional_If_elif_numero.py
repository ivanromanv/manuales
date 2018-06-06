#Write a program which asks the user to type an integer.
#If the number is 2  then the program should print "two",
#If the number is 3  then the program should print "three",
#If the number is 5  then the program should print "five", 
#Otherwise it should print "other".
numero = input("Insert the number: ")
numero = int(numero)
if numero == 2:
    print("two")
elif numero == 3:
    print("three")
elif numero == 5:
    print("five")    
else:
    print("other")
 
