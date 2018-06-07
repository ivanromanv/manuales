# Write a function named "reverse_dictionary" that receives a dictionary as input argument and returns a reverse of the input dictionary where the values of the original dictionary are used as keys for the returned dictionary and the keys of the original dictionary are used as value for the returned dictionary as explained below: 
#
# For example, if the function is called as
#
# reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']})
# then your function should return
# {'precise': ['accurate', 'exact'], 'clever': ['astute', 'smart'], 'talented': ['smart'], 'bright': ['smart'], 'exact': ['accurate'], 'smart': ['astute']}
# Notes:
# The list of values in the returned dictionary is sorted in ascending order
# Capitalization does not matter. This means that all the words should be converted to lower case letters. For example the word "Accurate" is capitalized in the original dictionary but in the returned dictionary it is written with all lower case letters
# Do NOT import any module for solving this problem.
#
def reverse_dictionary(input_dict):
    output_dict={}
    for llave in input_dict:
        for valor in input_dict[llave]:
            llave_lowered=llave.lower()
            valor_lowered=valor.lower()
            if output_dict.get(valor_lowered):
                if llave not in output_dict[valor_lowered]:
                    output_dict[valor_lowered].append(llave_lowered)
                    output_dict[valor_lowered].sort()
            else:
                output_dict[valor_lowered]=[llave_lowered]
    return output_dict

# OJO SOLO LA FUNCION!!!   
# Main Program #
input_dict = {'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}
evalua_reverse_dictionary = reverse_dictionary(input_dict)
print(evalua_reverse_dictionary)
