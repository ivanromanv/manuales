#Este prograa convierte celcius a farenheit
celsius=input("Ingrese grados celsius: ")
celsius=float(celsius)
farenheit=((celsius*9)/5)+32
if farenheit > 90 :
    print("It is hot")
else :
    print("It is not hot")
print(farenheit)
