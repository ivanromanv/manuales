#Figure out the format string
# http://pubs.opengroup.org/onlinepubs/009695399/functions/strptime.html 
data_tuples = list()
#Abrir el archivo
with open('sample_data.csv','r') as f:
    for line in f:
        data_tuples.append(line.strip().split(','))
#Muestra los 10 primeros        
print(data_tuples[0:10])

import datetime
x='2016-01-01 00:00:09'
format_str = "%Y-%m-%d %H:%M:%S"
datetime.datetime.strptime(x,format_str)
for i in range(0,len(data_tuples)):
    data_tuples[i][0] = datetime.datetime.strptime(data_tuples[i][0],format_str)
    data_tuples[i][1] = float(data_tuples[i][1])
    #Formato [datetime.datetime(2016, 1, 1, 0, 0, 9), 0.0815162037037037]    
#Muestra los 10 primeros        
print(data_tuples[0:10])

# We can replace the datetime by hourly buckets
x=data_tuples[0][0]
x.hour
data_tuples = [(x[0].hour,x[1]) for x in data_tuples]

# Use list comprehension to bucket the data
data_tuples = list()
with open('sample_data.csv','r') as f:
    for line in f:
        data_tuples.append(line.strip().split(','))
import datetime
for i in range(0,len(data_tuples)):
    data_tuples[i][0] = datetime.datetime.strptime(data_tuples[i][0],format_str)
    data_tuples[i][1] = float(data_tuples[i][1])
