#Write a program which asks the user to enter their age in years (Assume that the user always enters an integer) and based on the following conditions, prints the output exactly as in the following format (as highlighted in yellow): 
#When age is less than or equal to 0, your program should print
#UNBORN
#When age is greater than 0 and less than or equal to 150, your program should print
#ALIVE
#When age is greater than 150, your program should print
#VAMPIRE
#Note that your printed output should be in capital letters and there should be no extra spaces.
edad = input("Give me you age: ")
edad = int(edad)
if edad <= 0:
    print('UNBORN')
elif edad > 0 and edad <= 150:
    print('ALIVE')
if edad > 150:
    print('VAMPIRE')
 
