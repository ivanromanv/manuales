# Write a function that accepts two lists both of which consists of numbers and returns the total sum of all the even numbers integers from both lists. If there are no even numbers in the list, the function should return 0.
#
def sum_even_list(a, b):
   reg_list=len(a)
   eval_sum = sum_even(a) + sum_even(b)
   return eval_sum

def sum_even(a):
   calculo=0
   for x in a:
      if x%2 == 0:
         calculo=calculo+x
   return calculo

# OJO SOLO LA FUNCION!!!
# Main Program #
a = [5,2,3,3,4,5]
b = [5,4,3,3,4,5]
evalua_sum_even_list  = sum_even_list(a, b)
print(evalua_sum_even_list)
