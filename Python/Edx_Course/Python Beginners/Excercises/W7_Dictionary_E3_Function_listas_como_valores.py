# Write a function that accepts a dictionary as input which contains the names and grades of students (The keys are student names and the values are lists of grades for 3 exams (1 Dimensional list)) and returns the list of names for those students whose grade on all three exams is greater than or equal to 78.
#
def dictionary_list_as_values(dictionary):
    output_list = []
    keys = dictionary.keys()
    for estudiante in keys:
        lista_notas = dictionary[estudiante]
        materia_1=lista_notas[0]
        materia_2=lista_notas[1]
        materia_3=lista_notas[2]
        if materia_1>=78 and materia_2>=78 and materia_3>=78:
            output_list.append(estudiante)
    return output_list

# OJO SOLO LA FUNCION!!!   
# Main Program #
dictionary = {'Hectar': [80, 50, 0], 'John': [70, 80, 85], 'Undertaker': [90, 92, 93], 'Priest': [75, 78, 83], 'Henry': [80, 85.2, 88]}
evalua_dictionary_list_as_values = dictionary_list_as_values(dictionary)
print(evalua_dictionary_list_as_values)
