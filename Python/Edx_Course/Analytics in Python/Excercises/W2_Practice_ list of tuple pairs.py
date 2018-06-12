# Practice problem
#
# Write a function search_list that searches a list of tuple pairs and returns the value associated with the first element of the pair
#
def search_list(prices,ticker):
# Sol-1    
#    new_list = []
#    for lista in prices:
#        if lista[0] == ticker:
#            new_list.append(lista)
#    return new_list

# Sol-2
    for lista in prices:
        if lista[0] == ticker:
            return lista
    return 0
    
prices = [('AAPL',96.43),('IONS',39.28),('GS',159.53)]
ticker = 'IONS'
eval = (search_list(prices,ticker))
print(eval)
