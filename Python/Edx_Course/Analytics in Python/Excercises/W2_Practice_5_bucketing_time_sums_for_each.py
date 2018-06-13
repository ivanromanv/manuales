buckets = dict()
data_tuples = list()
with open('sample_data.csv','r') as f:
    for line in f:
        data_tuples.append(line.strip().split(','))
        
for item in data_tuples:
    if item[0] in buckets:
        buckets[item[0]][0] += 1
        buckets[item[0]][1] += item[1]
    else:
        buckets[item[0]] = [1,item[1]] 

print(buckets)