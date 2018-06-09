# Modify the following replace function so that where the first occurrence of
# replace_string in test_string is replaced by bodega.
#
# Tests:
#
# replace("Hi how are you?", "you") should return "Hi how are bodega?"
#
# replace("Love is in the air", "air") should return "Love is in the bodega"
#
#def replace(test_string, replace_string):
#    test_string = test_string.replace(replace_string,"bodega")
#    return test_string
def replace(test_string, replace_string):
    len_word = len(replace_string)
    to_string = test_string.find(replace_string)
    part_1 = test_string[0:to_string]
    part_2 = "bodega"
    part_3 = test_string[to_string+len_word:]
    new_string = part_1+part_2+part_3
    return new_string

# OJO!!! SOLO LA FUNCION
test_string = "Hi how are you?"
replace_string = "you"
eval = replace(test_string, replace_string)
print(eval)