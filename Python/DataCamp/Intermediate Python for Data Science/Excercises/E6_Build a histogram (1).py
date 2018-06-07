# life_exp, the list containing data on the life expectancy for different countries in 2007, is available in your Python shell.
#
#To see how life expectancy in different countries is distributed, let's create a histogram of life_exp.
#matplotlib.pyplot is already available as plt.
#
# Create histogram of life_exp data
# life_exp contiene los datos
import matplotlib.pyplot as plt
plt.hist(life_exp, bins=10)
# Display histogram
plt.show()


