def get_hour_bucket_averages(filename):
    def get_data(filename):
        data_tuples = list()
        with open(filename,'r') as f:
            for line in f:
                data_tuples.append(line.strip().split(','))
        import datetime
        format_str = "%Y-%m-%d %H:%M:%S"
        data_tuples = [(datetime.datetime.strptime(x[0],format_str).hour,float(x[1])) for x in data_tuples]
        return data_tuples
    
    buckets = dict()
    for item in get_data(filename):
        if item[0] in buckets:
            buckets[item[0]][0] += 1
            buckets[item[0]][1] += item[1]
        else:
            buckets[item[0]] = [1,item[1]]  
    return [(key,value[1]/value[0]) for key,value in buckets.items()]

eval = get_hour_bucket_averages('sample_data.csv')
print(eval)