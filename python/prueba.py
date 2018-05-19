def trianguloPascal(n):
    # Caso base 
    if n == 0: 
        return [] 
    if n == 1: 
        return [[1]] 
    # Caso recursivo 
    last_list = trianguloPascal(n-1) 
    this_list = [1] 
    for i in range(1, n-1): 
        this_list.append(last_list[n-2][i-1] + last_list[n-2][i]) 
    this_list.append(1) 
    last_list.append(this_list) 
    print(last_list)
    return last_list

n = int(input("Numero de lineas para triangulo de Pascal: "))
resultado = trianguloPascal(n)
# mostramos el resultado
#for i in resultado:
#    print i


        
