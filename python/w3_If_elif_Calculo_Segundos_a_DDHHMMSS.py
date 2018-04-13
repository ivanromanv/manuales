#Write a program that asks the user to enter a positive integer n. Assuming that this integer is in seconds, your program should convert the number of seconds into days, hours, minutes, and seconds and prints them exactly in the format specified below. Here are a few sample runs of what your program is supposed to do: 
#when user enters
#369121517
#your program should print:
#4272 days 5 hours 45 minutes 17 seconds
#when user enters
#24680
#your program should print:
#0 days 6 hours 51 minutes 20 seconds
#when user enters
#129600
#your program should print:
#1 days 12 hours 0 minutes 0 seconds
#Note that the numbers and words in the above output are separated by only one space. All the words are in lower case. Your output should exactly match the format shown above.
numero = input("Enter the number in seconds: ")
#variables
numero = int(numero)
dias = int(0)
horas = int(0)
minutos = int(0)
segundos = int(0)
saldo = int(0)
#calculo
if numero >= 86400 :
    dias = ((numero / 3600) / 24)
    saldo = (numero) % 86400
    numero = saldo
if numero >= 3600 :
    horas = (numero / 3600)
    saldo = (numero) % 3600
    numero = saldo
if numero >= 60 :
    minutos = (numero / 60)
    saldo = (numero) % 60
    numero = saldo
if numero < 60 :
    segundos = (numero)
print(int(dias),"days",int(horas),"hours",int(minutos),"minutes",int(segundos),"seconds")
