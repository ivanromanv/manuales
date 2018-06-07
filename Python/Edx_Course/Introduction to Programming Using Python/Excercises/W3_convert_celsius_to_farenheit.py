#Este programa convierte celcius a farenheit
celsius=input("Ingrese grados celsius: ")
celsius=float(celsius)
farenheit=((celsius*9)/5)+32
print("The temperarature is ",farenheit, "degrees Farenheit")
if farenheit < 32 :
    print("It is freesing")
elif farenheit < 50 :
    print("It is chilly")
elif farenheit < 90:
    print("It is OK")
else :
    print("It is hot")

