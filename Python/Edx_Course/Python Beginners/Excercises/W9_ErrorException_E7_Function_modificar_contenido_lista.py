# Errors and Exceptions Exercise 7
# 0 puntos posibles (no calificados)
# You are trying to modify the content of a list and you need to write a function to perform the task. The function takes three arguments. The first argument is the list itself, the second argument is an index 'n' and the third argument is a string. Your job is to set the 'n'th (index) item of the list as the given string and return the modified list if successful. In case of a failure your function should return the original list. Write a function that performs this task using the try...except...else statements.
#
def modificar_contenido_lista(lista,indice,string):
    try:
        lista[indice] = string
    except (IndexError, TypeError):
        return lista
    else:
        return lista
    
# OJO SOLO LA FUNCION!!!   
# Main
lista = [1, 2, 3, 4, 5]
indice = 2
string = "hola"
evalua_modificar_contenido_lista = modificar_contenido_lista(lista,indice,string)
print(evalua_modificar_contenido_lista)