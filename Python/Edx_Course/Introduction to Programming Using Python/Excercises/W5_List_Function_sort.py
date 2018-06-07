# Write a program that asks the user to enter an integer between 1 and 9999 (both inclusive) and then prints the input integer using words. For example if the user enters:
#
# 3421
# Then your program should print
# three thousand four hundred twenty one
# more examples:
# Input	Printed Output
# 15	fifteen
# 7000	seven thousand
# 501	five hundred one
# 1008	one thousand eight
# 7	seven
# Notes:
# the words in the printed output should all be lower cased and separated by only one space
# There is no "and" between the printed words.
# Notice that when you use a print() statement, Python by default adds a new line after each printed output. If you do not want each new print statment to be printed in a new line then you should add end="" at the end of your print arguments as shown below:
# print("seven ", end = "")
# print("thousand")
# This will print
# seven thousand
# Also when you use two arguments in a print statement, Python adds a space between them by default. For example:
# print("x",5)
# will print
# x 5
# If you do not want a space to be inserted between your arguments then you should add sep="" at the end of your print arguments as shown below:
# print("x",5,sep="")
# will print
# x5
# Make sure your words match the following spellings:
# one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
# sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
# ninety, hundred, thousand
#
def funcion_numeros_a_letras(number):
   centenas = ['hundred']
   miles = ['thousand']
   resultado=str("")
   evalua_funcion_numeros_a_letras_decenas=""
   evalua_funcion_numeros_a_letras_basico2=""
   evalua_funcion_numeros_a_letras_basico3=""
   if number>=1 and number<10:
      evalua_funcion_numeros_a_letras_basico = funcion_numeros_a_letras_basico(number)
      #print(evalua_funcion_numeros_a_letras_basico)
      resultado=evalua_funcion_numeros_a_letras_basico
   elif number>=10 and number<=19:
      evalua_funcion_numeros_a_letras_especial = funcion_numeros_a_letras_especial(number-9)
      #print(evalua_funcion_numeros_a_letras_especial)
      resultado=evalua_funcion_numeros_a_letras_especial
   elif number>=20 and number<=99:
      cadena=''.join([str(number)])
      numeros=[]
      for valor in (cadena):
         elnumero=int(valor)
         numeros.append(elnumero)
      evalua_funcion_numeros_a_letras_decenas = funcion_numeros_a_letras_decenas(numeros[0])
      evalua_funcion_numeros_a_letras_basico = funcion_numeros_a_letras_basico(numeros[1])
      resultado=evalua_funcion_numeros_a_letras_decenas+" "+evalua_funcion_numeros_a_letras_basico
      #print(evalua_funcion_numeros_a_letras_decenas,evalua_funcion_numeros_a_letras_basico,sep=" ")
   elif number>=100 and number<=999:
      cadena=''.join([str(number)])
      numeros=[]
      for valor in (cadena):
         elnumero=int(valor)
         numeros.append(elnumero)
      print(numeros)
      evalua_funcion_numeros_a_letras_basico = funcion_numeros_a_letras_basico(numeros[0])
      resultado=evalua_funcion_numeros_a_letras_basico+" "+centenas[0]      
      if numeros[1]!=0:
         evalua_funcion_numeros_a_letras_decenas = funcion_numeros_a_letras_decenas(numeros[1])
         resultado=resultado+" "+evalua_funcion_numeros_a_letras_decenas
      if numeros[2]!=0:         
         evalua_funcion_numeros_a_letras_basico2 = funcion_numeros_a_letras_basico(numeros[2])
         resultado=resultado+" "+evalua_funcion_numeros_a_letras_basico2
      resultado=evalua_funcion_numeros_a_letras_basico+" "+centenas[0]+" "+evalua_funcion_numeros_a_letras_decenas+" "+evalua_funcion_numeros_a_letras_basico2
      #print(evalua_funcion_numeros_a_letras_basico,centenas[0],evalua_funcion_numeros_a_letras_decenas,evalua_funcion_numeros_a_letras_basico2,sep=" ")
      print(resultado)
   elif number>=1000 and number<=9999:
      cadena=''.join([str(number)])
      numeros=[]
      for valor in (cadena):
         elnumero=int(valor)
         numeros.append(elnumero)
      evalua_funcion_numeros_a_letras_basico = funcion_numeros_a_letras_basico(numeros[0])
      if numeros[1]!=0:
         evalua_funcion_numeros_a_letras_basico2 = funcion_numeros_a_letras_basico(numeros[1])
      if numeros[2]!=0:
         evalua_funcion_numeros_a_letras_decenas = funcion_numeros_a_letras_decenas(numeros[2])
      if numeros[3]!=0:
         evalua_funcion_numeros_a_letras_basico3 = funcion_numeros_a_letras_basico(numeros[3])
      resultado=evalua_funcion_numeros_a_letras_basico+" "+miles[0]+" "+evalua_funcion_numeros_a_letras_basico2+" "+centenas[0]+" "+evalua_funcion_numeros_a_letras_decenas+" "+evalua_funcion_numeros_a_letras_basico3
      #print(evalua_funcion_numeros_a_letras_basico,miles[0],evalua_funcion_numeros_a_letras_basico2,centenas[0],evalua_funcion_numeros_a_letras_decenas,evalua_funcion_numeros_a_letras_basico3,sep=" ")
   return resultado

def funcion_numeros_a_letras_basico(number):
   basico = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
   numero=''.join(basico[number-1:number:1])
   return numero

def funcion_numeros_a_letras_especial(number):
   especial = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
   numero=''.join(especial[number-1:number:1])
   return numero

def funcion_numeros_a_letras_decenas(number):
   decenas = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
   numero=''.join(decenas[number-2:number-1:1])
   return numero
  
# Main Program #
number=int(input('please enter an integer between 1 and 9999: '))
evalua_funcion_numeros_a_letras = funcion_numeros_a_letras(number)
print(evalua_funcion_numeros_a_letras)
