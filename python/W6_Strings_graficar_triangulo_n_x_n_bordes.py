# Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints only the boundaries of the triangle using asterisks "*" of height 'n'. For example if the user enters 6 then the height of the triangle should be 6 as shown below and there should be no spaces between the asterisks on the top line:
#
# ******
# *   *
# *  *
# * *
# **
# *
#
def funcion_grafico_triangulo_nxn_nobordes(number):
    matriz = number*str("*")
    spaces=" "
    caracter="*"
    largo = number
    for x in matriz:
    #while largo <= number:
        if largo==number:
            print(matriz[0:largo])
            #print(caracter*number)
        if largo<number:
            if largo==1:
                print(caracter)
                break
            else:
                print(caracter+spaces*(largo-2)+caracter)
        largo=largo-1

# Main Program #
number = int(input("Enter number: "))
evalua_funcion_grafico_triangulo_nxn_nobordes = funcion_grafico_triangulo_nxn_nobordes(number)
#print(evalua_funcion_grafico_triangulo_nxn_nobordes)
