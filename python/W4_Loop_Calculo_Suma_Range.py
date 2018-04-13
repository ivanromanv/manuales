#Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.
numero = int(0)
suma = int(0)
for numero in range(1,101):
    #numero = numero + 1
    divisible = numero % 2
    if divisible == 0:
        suma = suma + numero
print(int(suma))
