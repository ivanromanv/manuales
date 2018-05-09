# Dictionary Exercise 9 (Day of the Week)
# 0 puntos posibles (no calificados)
# Write a function that accepts a string which contains a particular date from the Gregorian calendar. Your function should return what day of the week it was. Here are a few examples of what the input string(Month Day Year) will look like. However, you should not 'hardcode' your program to work only for these input!
#
# "June 12 2012"
# "September 3 1955"
# "August 4 1843" 
# Note that each item (Month Day Year) is separated by one space. For example if the input string is:
# "May 5 1992"
# Then your function should return the day of the week (string) such as:
# "Tuesday"
# Algorithm with sample example:
# # Assume that input was "May 5 1992"
# day (d) = 5        # It is the 5th day
# month (m) = 3      # (*** Count starts at March i.e March = 1, April = 2, ... January = 11, February = 12)
# century (c) = 19   # the first two characters of the century
# year (y) = 92      # Year is 1992 (*** if month is January or february decrease one year)
# # Formula and calculation
# day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
# after calculation we get, (w) = 2
# Count for the day of the week starts at Sunday, i.e Sunday = 0, Monday = 1, Tuesday = 2, ... Saturday = 6
# Since we got 2, May 5 1992 was a Tuesday
#
def day_of_the_week_calendar(input_string):
    import math
    my_month, day, year = input_string.split(" ")    
    #convertir a lista
    string_list =list(input_string)
    
    dictionary_months={"March": 1,"April": 2,"May": 3,"June": 4,"July": 5,"August": 6,"September": 7,"October": 8,"November": 9, "December":10,"January":11,"February":12}
    dictionary_day_of_week= {"Sunday": 0,"Monday": 1,"Tuesday": 2,"Wednesday": 3,"Thursday": 4,"Friday": 5,"Saturday": 6}
    
    month = dictionary_months[my_month]
    day = int(day)
    # Los primeros 2 caracteres del year
    century = int(year[0] + year[1])
    # Los ultimos 2 caracteres del year
    year = int(year[2] + year[3])
    
    # If month > 10 (Enero y Febrero cuando se reste del year)
    if month > 10:
        year = year - 1
    # Calculos segun formula
    w = (day + math.floor(2.6*month - 0.2) -2*century + year + math.floor(year/4) + math.floor(century/4))%7
    for day in dictionary_day_of_week:
        if dictionary_day_of_week[day] == w:
            return day

# OJO SOLO LA FUNCION!!!   
# Main Program #
input_string = "June 12 2012"
evalua_day_of_the_week_calendar = day_of_the_week_calendar(input_string)
print(evalua_day_of_the_week_calendar)
