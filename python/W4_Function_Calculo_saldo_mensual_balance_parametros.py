# Write a function that calculates and returns the remaining loan balance. This function accepts four parameters in the exact order shown below:
# (principal, annual_interest_rate, duration , number_of_payments)
#   
# principal: The total amount of loan. Assume that the principal is positive floating point number.
# annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
# duration: number of years to pay the loan back. Assume that duration is a positive integer.
# number_of_payments: number of monthly payments that are already paid. Assume that number_of_payments is an integer.
# To calculate the reamining loan balance use the following equation
#
#                                r(1+r)^n - (1+r)^p
# Monthly Payment = Principal * ------------------
#                               (1+r)^n - 1
# Where:
#
# r is the monthly interest rate. r should be calculated by first dividing the annual_interest_rate by 100 and then divide the result by 12 to make it monthly. Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the follwing equation:
#                                   
# Monthly Payment = Principal * ( 1 - (p/n))
#                                   
# n is the total number of monthly payments for the entire duration of the loan. Notice that n is equal to loan duration in years multiplied by 12.
# p is the number of payments which are already made.
# Your function should return the remaining balance as a floating point number.
#
# Example: if your function is called with the following parameters:
#
# (1000.0,4.5,5,12)
# Then it should return a floating point number:
# 817.5512804582867
# Remember that you are not asked to print anything. So, your function should just return the resulting remaining balance. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem remember to embed the helper function(s) inside the first function.

def pago_saldo_mensual(principal, annual_interest_rate, duration , number_of_payments):
   if annual_interest_rate > 0:
      ecuacion_uno = ((1+((annual_interest_rate/100)/12))**(duration*12))
      ecuacion_dos = ((1+((annual_interest_rate/100)/12))**(number_of_payments))
      ecuacion_tres = (((1+((annual_interest_rate/100)/12))**(duration*12)) - 1)
      calculo = principal * ((ecuacion_uno -  ecuacion_dos) / ecuacion_tres)
   else:
      calculo = principal * (1 - (number_of_payments/(duration**12)))
   return calculo

# Main Program #
evalua_pago_saldo_mensual = pago_saldo_mensual(1000.0,10,5,12)
print(evalua_pago_saldo_mensual)
