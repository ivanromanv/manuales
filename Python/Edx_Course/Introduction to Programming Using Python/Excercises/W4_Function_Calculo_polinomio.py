# Write a function that accepts a number  and evaluates the following polynomial expression:
# y = x^4 - 12x^3 + 13x^2 + 11
# and returns the value of y
def polinomio(valor):
   resultado = (valor**4) - (12*(valor**3)) + 13*(valor**2) + 11
   return resultado

# Main Program #
evalua_polinomio = polinomio(1)
print(evalua_polinomio)

