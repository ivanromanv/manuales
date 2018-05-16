# Tuples Exercise 1 (Statistics)
# 0 puntos posibles (no calificados)
# Write a function that accepts a tuple of positive integers and returns the mean and median of the integers as a tuple. For example if the input tuple is:
#
# (3, 3, 0, 1, 12, 13, 15, 16)
# then your function should return a tuple that contains the mean and median as:
# (7.875, 7.5)
# You may use (import) the numpy package in your function. Do not use the "statistics" package.
#
def tuple_mean_media(tuple_list):
    import numpy
    mean = sum(tuple_list)/len(tuple_list)
    median = numpy.median(numpy.array(tuple_list))
    return mean, median
    
# OJO SOLO LA FUNCION!!!   
# Main
tuple_list = ((38, 39, 40, 42, 44, 44, 46, 47, 50, 50, 96),)
evalua_tuple_mean_media = tuple_mean_media(tuple_list)
print(evalua_tuple_mean_media)