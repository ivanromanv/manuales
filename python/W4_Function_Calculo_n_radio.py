# Write a function that a accepts a positive number 'r' as the radius of a circle and calculates and returns the area of the circle. Use the value of pi as 3.14
def area_circunferencia(radio):
   area = float((radio * radio) * 3.14)
   return area

# Main Program #
area = area_circunferencia(2)
print(area)
