#Write a program which asks the user to enter an integer 'n' which would be the total numbers of hours the user worked in a week and calculates and prints the total amount of money the user made during that week. If the user enters any number less than 0 or greater than 168 (n < 0 or n > 168) then your program should print INVALID 
#Assume that hourly rate for the first 40 hours is $8 per hour. 
#Hourly rate for extra hours between 41 and 50 (41 <= n <= 50 ) is $9 per hour. 
#Hourly rate for extra hours greater than 50 is $10 per hour. 
#Here are a few examples:
#if the user enters -5, then your program should print
#INVALID
#if the user enters 34, then your program should print
#YOU MADE 272 DOLLARS THIS WEEK
#if the user enters 45, then your program should print
#YOU MADE 365 DOLLARS THIS WEEK
#if the user enters 67, then your program should print
#YOU MADE 580 DOLLARS THIS WEEK
#Note that the amount of money made by the user must be an integer (not a float) and your output should exactly match the format specified above (including spaces and capitalization).
numero = input("Enter the number in hours: ")
numero = int(numero)
sueldo = int(0)
if numero >= 1 and numero <= 40 :
    sueldo = (numero * 8)
if numero >= 41 and numero <= 50 :
    sueldo = (40 * 8) + ((numero - 40) * 9)
if numero > 50 and numero <= 168 :
    sueldo = (40 * 8) + (10 * 9) + ((numero - 50) * 10)
if numero < 0 or numero > 168 :
    print('INVALID')
else:
    print('YOU MADE', sueldo, "DOLLARS THIS WEEK")
