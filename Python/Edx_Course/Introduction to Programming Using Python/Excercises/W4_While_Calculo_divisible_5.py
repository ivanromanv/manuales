#Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. ( 1 and 101 are included) (Use while loop)
#Program: W4_While_Calculo_divisible_5
numero = int(1)
suma = int(0)
divisible = int(0)
while numero <= 101:
    divisible = numero % 5
    if divisible == 0:
        suma = suma + numero
    numero = numero + 1
print(int(suma))
