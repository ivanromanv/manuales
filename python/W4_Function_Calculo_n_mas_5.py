# Write a function that a accepts a positive number 'r' as the radius of a circle and calculates and returns the area of the circle. Use the value of pi as 3.14
def area_circunferencia(radio):
   area = float((radio * radio) * 3.14)
   #resultado = [area]
   #return resultado
   return area

# Main Program #
#my_list = area_circunferencia(2)
#my_list = float(my_list[0])
#print(my_list)
#area_circunferencia(2)
area = area_circunferencia(2)
print(area)
