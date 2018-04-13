#Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of all numbers from 1 to n (including both 1 and n).
numero = int(input("Enter number of end: "))
ultimo = int(0)
ultimo = numero
suma = int(0)
for numero in range(1,ultimo+1):
    suma = suma + numero
print(int(suma))
