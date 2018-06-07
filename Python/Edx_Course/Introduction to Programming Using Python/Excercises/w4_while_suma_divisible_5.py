#Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. ( 1 and 101 are included) (Use while loop)
numero = int(1)
while numero <= 101:
    suma = int(0)
    print("Numero", numero)
    saldo = numero % 5
    print(saldo)
    numero = numero + 1
    if saldo == 0 :
        suma = suma + numero
#calculo
print(int(suma))
