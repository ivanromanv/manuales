# Quiz 5, Part 4 (one_to_2D)
# 0.0/20.0 puntos (calificados)
#
# Write a function named one_to_2D which receives an input list and two integers r and c as parameters and returns a new two-dimensional list having r rows and c columns.
#
# Note that if the number of elements in the input list is larger than r*c then ignore the extra elements. If the number of elements in the input list is less than r*c then fill the two dimensional list with the keyword None. For example if your fuction is called as hown below:
#
# one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3)
#
# Then it should return:
#
# [[8, 2, 9],[4, 1, 6]]
#
def one_to_2D(some_list, r, c):
    tamano_lista=len(some_list)
    matriz=[]
    inicio_matriz=0
    fin_matriz=c
    salto=0
    insertar_none=0
    for names in range(0,len(some_list)):
        #llenado de lista r de c
        #print(some_list[names])
        if tamano_lista+1>(r*c):
            matriz.append(some_list[inicio_matriz:fin_matriz])
            inicio_matriz=fin_matriz
            fin_matriz=fin_matriz+c
            #Iteracion
            salto=salto+1
            if salto>r-1:
                return matriz
        if tamano_lista<(r*c):
            matriz.append(some_list[inicio_matriz:fin_matriz])
            inicio_matriz=fin_matriz
            fin_matriz=fin_matriz+c
            #Iteracion
            salto=salto+1
            #Agregar None a addnone para luego sumar a matriz
            add_none=some_list[inicio_matriz:fin_matriz]
            if len(some_list[inicio_matriz:fin_matriz])<=c:
                while insertar_none < c-len(some_list[inicio_matriz:fin_matriz]):
                    add_none.append(None)
                    insertar_none=insertar_none+1
                matriz.append(add_none)
                while salto+1 < r:
                    matriz.append([None]*c)
                    salto=salto+1
            return matriz

# OJO SOLO LA FUNCION!!!   
# Main Program #
some_list = [0, 15, 30, 45, 60, 75, 90, 105]
r = 3
c = 6
evalua_one_to_2D = one_to_2D(some_list, r, c)
print(evalua_one_to_2D)