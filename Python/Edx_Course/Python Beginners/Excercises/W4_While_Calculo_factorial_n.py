#Write a program using while loop, which asks the user to type a positive integer, n, and then prints the factorial of n. A factorial is defined as the product of all the numbers from 1 to n (1 and n inclusive). For example factorial of 4 is equal to 24. (because 1*2*3*4=24)
numero = input("Enter the number for calculate factorial: ")
contador = int(numero)
secuencia = 0
factorial = 1
while contador > 0:
    contador = contador - 1
    secuencia = secuencia + 1
    factorial = factorial * secuencia
print(factorial)
