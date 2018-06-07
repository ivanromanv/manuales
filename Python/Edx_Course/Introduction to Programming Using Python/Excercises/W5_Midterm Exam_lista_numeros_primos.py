# Write a function named list_of_primes that accepts a positive integer n and returns a sorted list (ascending order) of all the prime numbers between 2 and n (including 2 but not including n)
#
def list_of_primes(n):
   list_primes=[]
   start_number=2
   end_number=n
   current_number=start_number
   for current_number in range(current_number,end_number+1):
      is_current_number_prime = True
      for current_divisor in range(2,current_number):
         if current_number % current_divisor == 0:
            is_current_number_prime = False
            break
      if is_current_number_prime :
#         print(current_number, "es primo")
         list_primes.append(current_number)
   reg_list=len(list_primes)
   list_new=[]
   if current_number%2 == 0:
      list_new=list_primes[0:reg_list]
   else:
      list_new=list_primes[0:reg_list-1]
   return list_new

# OJO SOLO LA FUNCION!!!
# Main Program #
n = int(input("Enter the number:"))
evalua_list_of_primes  = list_of_primes(n)
print(evalua_list_of_primes)
