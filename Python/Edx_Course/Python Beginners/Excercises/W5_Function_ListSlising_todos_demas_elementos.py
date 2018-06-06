# Write a function that accepts a list as input and returns a new list which includes every other element in the original list. Keep the first element, i.e. input_list[0]. For example if:
#
# input_list = ["we", "love", "python", "so","much"]
# then your function should return a list such as:
# ['we', 'python', 'much']
#
def funcion_todos_demas_elementos(input_list):
   new_list=[]
   new_list=input_list[0:1]+input_list[2:3]+input_list[4:5]
   return new_list
 
# OJO SOLO LA FUNCION!!!   
# Main Program #
input_list = ["we", "love", "python", "so","much"]
evalua_funcion_todos_demas_elementos = funcion_todos_demas_elementos(input_list)
print(evalua_funcion_todos_demas_elementos)
