#Programa que presenta numeros primos
# en medio de 2 y 50
start_number=2
end_number=50
current_number=start_number
while current_number <= end_number:
    current_divisor = 2
    is_current_number_prime = True
    while(current_divisor <current_number):
        if current_number % current_divisor == 0:
            is_current_number_prime = False
            break
        current_divisor = current_divisor + 1
    if is_current_number_prime :
        print(current_number, "es primo")
    current_number = current_number + 1
print("hecho!")
