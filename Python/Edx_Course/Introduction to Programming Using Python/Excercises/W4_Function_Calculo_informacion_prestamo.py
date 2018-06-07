# Write a program for loan calculations. Your program should ask the user for three pieces of information (with three seperate input() functions:)
#
# Total amount of loan.
# Annual interest rate. (Assume that the interest rate is a positive integer. For example 5 means that annual interest is 5% (five percent) per year.
# Total duration of loan in years.
# Your Program should use the two functions that you implented in part 1 and 2 of this exercise and display the follwoing information about the loan.
#
# In the first first line show the amount of loan and interest rate.
# In the second line show duration of the loan and monthly payment.
# In each of the following lines show the Loan balance and total amount paid for each year.
# Example 1: assuming that user inputs the following numbers in response to your questions:
#
# Enter loan amount: 1000.0
# Enter annual interest rate (percent): 10.0
# Enter loan duration in years: 5
#    
# The output of your program should be:
#
# LOAN AMOUNT: 1000 INTEREST RATE (PERCENT): 10
# DURATION (YEARS): 5 MONTHLY PAYMENT: 21
# YEAR: 1 BALANCE: 837 TOTAL PAYMENT 254
# YEAR: 2 BALANCE: 658 TOTAL PAYMENT 509
# YEAR: 3 BALANCE: 460 TOTAL PAYMENT 764
# YEAR: 4 BALANCE: 241 TOTAL PAYMENT 1019
# YEAR: 5 BALANCE: 0 TOTAL PAYMENT 1274
#  
# Important notes:
#  * Use floating point numbers in your calculations.
#  * Convert all the numbers to int only for printing them.
#
def informacion_pago_mensual(principal,annual_interest_rate,duration):
   if annual_interest_rate > 0:
      ecuacion_uno = (((annual_interest_rate/100)/12) * (1+((annual_interest_rate/100)/12))**(duration*12))
      ecuacion_dos = (((1+((annual_interest_rate/100)/12))**(duration*12)) - 1)
      calculo = principal * (ecuacion_uno / ecuacion_dos)
   else:
      calculo = principal / (duration*12)
   return calculo

def informacion_pago_saldo_mensual(principal,annual_interest_rate,duration,number_of_payments):
   if annual_interest_rate > 0:
      ecuacion_uno = ((1+((annual_interest_rate/100)/12))**(duration*12))
      ecuacion_dos = ((1+((annual_interest_rate/100)/12))**(number_of_payments))
      ecuacion_tres = (((1+((annual_interest_rate/100)/12))**(duration*12)) - 1)
      calculo = principal * ((ecuacion_uno -  ecuacion_dos) / ecuacion_tres)
   else:
      calculo = principal * (1 - (number_of_payments/(duration**12)))
   return calculo

def informacion_iteracion(principal,annual_interest_rate,duration):
   year=0
   valor_payment=0
   number_of_payments=0
   duration=int(duration)
   payment_month=0
   while year <= (duration-1):
      year=year+1
      number_of_payments = number_of_payments + 12
      evalua_informacion_pago_saldo_mensual = informacion_pago_saldo_mensual(principal,annual_interest_rate,duration,number_of_payments)
      evalua_informacion_pago_mensual = informacion_pago_mensual(principal,annual_interest_rate,duration)
      payment_month=payment_month + (evalua_informacion_pago_mensual*12)
      print("YEAR:",year,"BALANCE:",int(evalua_informacion_pago_saldo_mensual),"TOTAL PAYMENT",int(payment_month))

def informacion(principal, annual_interest_rate, duration):
   evalua_informacion_pago_mensual = informacion_pago_mensual(principal,annual_interest_rate,duration)
   print("LOAN AMOUNT:",int(principal),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
   print("DURATION (YEARS):",int(duration),"MONTHLY PAYMENT:",int(evalua_informacion_pago_mensual))
   evalua_informacion_iteracion = informacion_iteracion(principal,annual_interest_rate,duration)
       
# Main Program #
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
evalua_informacion = informacion(principal,annual_interest_rate,duration)

