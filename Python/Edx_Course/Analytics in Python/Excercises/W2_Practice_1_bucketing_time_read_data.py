# Let's look at the first 10 lines
data_tuples = list()
with open('sample_data.csv','r') as f:
    for line in f:
        data_tuples.append(line.strip().split(','))
print(data_tuples[0:10])