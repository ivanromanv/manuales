def get_data(filename):
    data_tuples = list()
    with open(filename,'r') as f:
        for line in f:
            data_tuples.append(line.strip().split(','))
    import datetime
    format_str = "%Y-%m-%d %H:%M:%S"
    data_tuples = [(datetime.datetime.strptime(x[0],format_str).hour,float(x[1])) for x in data_tuples]
    return data_tuples  

eval=get_data('sample_data.csv')
print(eval)