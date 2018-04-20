# Write a function named crazy_list that accepts a list as parameter and returns a boolean (either True or False) based on whether or not the list is the same forward and backwards. You may NOT use list.reverse() method. 
#
# For example, if the list received by the function is:
# 
# [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] 
# v(Notice how the list is exactly the same whethere you read it from left to right, or from right to left) Then your function should return the Boolean
# True 
# however, if the list recieved by the function is something like this:
# [4, 5, 6, 7, 8, 4, 5, 2] 
# (Notice how the list is NOT the same when reading from left to right vs right to left) In this case, your function should return the Boolean
# False 
#
def crazy_list(some_list):
   tamano=int(len(some_list))
   if tamano%2 == 1:
      mitad=int(tamano/2)
      middle=some_list[mitad:mitad+1]
      a=some_list[0:mitad]
      b=some_list[-1:-tamano+3:-1]
      #print(a,b)
      evalua_crazy_list_calculo  = crazy_list_calculo(some_list,a,b)
      return evalua_crazy_list_calculo
   else:
      mitad=int(tamano/2)
      middle=some_list[mitad:mitad]
      a=some_list[0:mitad]
      b=some_list[-1:-tamano+2:-1]
      #print(a,b)
      evalua_crazy_list_calculo  = crazy_list_calculo(some_list,a,b)
      return evalua_crazy_list_calculo

def crazy_list_calculo(some_list,a,b):
      reg_list=len(a)
      x=0
      contador=0
      for x in range(reg_list):
         contador=contador+1
         #print(a[x],b[x])
         if a[x]!=b[x]:
            return False
         elif a[x]==b[x] and reg_list==contador:
            return True

# OJO SOLO LA FUNCION!!!
# Main Program #
some_list = [5,4,3,8,3,4,5]
evalua_crazy_list  = crazy_list(some_list) 
print(evalua_crazy_list)
