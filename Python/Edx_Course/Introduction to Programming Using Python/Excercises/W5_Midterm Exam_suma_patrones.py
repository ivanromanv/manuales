# Write a function named crazy_list that accepts a list as parameter and returns a boolean (either True or False) based on whether or not the list is the same forward and backwards. You may NOT use list.reverse() method. 
#
# For example, if the list received by the function is:
# 
# [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] 
# v(Notice how the list is exactly the same whethere you read it from left to right, or from right to left) Then your function should return the Boolean
# True 
# however, if the list recieved by the function is something like this:
# [4, 5, 6, 7, 8, 4, 5, 2] 
# Write a function called pattern_sum that receives two single digit positive integers, (k and m) as parameters and calculates and returns the total sum as:
# k + kk + kkk + .... (the last number in the sequence should have m digits)
# For example, if the two integers are:
#
# (4, 5)
#
# Your function should return the total sum of:
# 4 + 44 + 444 + 4444 + 44444
# Notice the last number in this sequence has 5 digits. The return value should be:
#
# 49380
#
# if the two integers are:
#
# (5, 3)
#
# Your function should return the total sum of:
# 5 + 55 + 555
# Notice the last numebr in this sequence has 3 digits. The return value should be:
#
# 615
#
def pattern_sum(a, b):
   contador = str()
   suma=int(0)
   for x in range(1,b+1):
      contador = contador + str(a)
      suma = int(contador) + suma
   return suma

# OJO SOLO LA FUNCION!!!
# Main Program #
a = 7
b = 4
evalua_pattern_sum  = pattern_sum(a, b) 
print(evalua_pattern_sum)
