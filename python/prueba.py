#Declara variables
co=0
desc=0
tp=0
#Mensaje + lectura
co=int(input("Ingrese el total compra: "))
desc=int(input("Ingrese % de descuento : "))
#Proceso
desc=int(co*(desc/100))
tp=co-desc
#Presentacion de resultados
print("  El Subtotal:",co)
print(" (-)Descuento:",desc)
print("Total a pagar:",tp)
#Fin

        
