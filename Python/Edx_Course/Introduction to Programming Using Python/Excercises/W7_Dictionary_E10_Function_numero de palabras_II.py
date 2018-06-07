# Write a function that takes a 4 digit integer (from 1000 to 9999 both inclusive) as input argument and returns the integer using words as shown below:
#
# Sample Examples:
# if the input integer is 7000 then the function should return the string "seven thousand"
# if the input integer is 1008 then the function should return the string "one thousand eight"
# if the input integer is 4010 then the function should return the string "four thousand ten"
# if the input integer is 1012 then the function should return the string "one thousand twelve"
# if the input integer is 4506 then the function should return the string "four thousand five hundred six"
# if the input integer is 9900 then the function should return the string "nine thousand nine hundred"
# if the input integer is 8880 then the function should return the string "eight thousand eight hundred eighty"
# if the input integer is 5432 then the function should return the string "five thousand four hundred thirty two"
# Notice that the words in the output strings should all be lower cased and separated by only one space and make sure your words match the following spellings:
# one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
# sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
# ninety, hundred, thousand
#
def numbers_to_words_II(sample_integer):
    # Note that this is just one way
    # of solving this problem
    # It can be solved in many different ways
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"0" : ["zero", ""],
                         "1" : ["one", ""],
                         "2" : ["two","twenty"],
                         "3" : ["three","thirty"],
                         "4" : ["four","forty"],
                         "5" : ["five","fifty"],
                         "6" : ["six","sixty"],
                         "7" : ["seven","seventy"],
                         "8" : ["eight","eighty"],
                         "9" : ["nine","ninety"],
                         "10" : "ten",
                         "11" : "eleven",
                         "12" : "twelve",
                         "13" : "thirteen",
                         "14" : "fourteen",
                         "15" : "fifteen",
                         "16" : "sixteen",
                         "17" : "seventeen",
                         "18" : "eighteen",
                         "19" : "nineteen"}

    thousand_digit = sample_dictionary[splitted[0]][0]
    hundred_digit = sample_dictionary[splitted[1]][0]
    ten_digit = sample_dictionary[splitted[2]][0]
    one_digit = sample_dictionary[splitted[3]][0]

    my_list = []
    # Work with the thousand digit
    my_list.append(thousand_digit)
    my_list.append("thousand")

    if hundred_digit != "zero":
        my_list.append(hundred_digit)
        my_list.append("hundred")

    if ten_digit == "zero" and one_digit != "zero":
        my_list.append(one_digit)

    if ten_digit != "zero" and one_digit == "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)

    if ten_digit != "zero" and ten_digit != "one" and one_digit != "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)
        last_digit = sample_dictionary[splitted[3]][0]
        my_list.append(last_digit)

    if ten_digit != "zero" and ten_digit == "one" and one_digit != "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    if ten_digit != "zero" and ten_digit == "one" and one_digit == "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    # remove any "" that the list contains
    # due to the way the program was implemented
    if "" in my_list:
        my_list.remove("")
    out_string = ""
    out_string = ' '.join(my_list)
    return out_string

# OJO SOLO LA FUNCION!!!   
# Main Program #
sample_integer = "2058"
evalua_numbers_to_words_II = numbers_to_words_II(sample_integer)
print(evalua_numbers_to_words_II)