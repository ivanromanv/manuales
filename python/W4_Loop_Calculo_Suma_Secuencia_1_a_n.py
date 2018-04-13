#Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines. For example if 'n' is equal to 4 then the output should look like the following:
#1
#10
#100
#1000
#10000
numero = int(input("Enter number of end: "))
ultimo = int(0)
ultimo = numero
suma = int(1)
for numero in range(1,ultimo+2):
    print(suma)
    valor = int(1*10)
    suma = valor * suma
