#Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)
#(1 + 4 + 7 + 10 + ....)
numero = int(1)
suma = int(0)
while numero <= 1001:
    suma = suma + numero
    numero = numero + 3
print(int(suma))
