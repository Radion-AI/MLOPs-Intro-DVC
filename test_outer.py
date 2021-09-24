import os

def is_datazip_present():
    return os.path.isfile('./data.zip')

def is_model_present():
    return os.path.isfile('./model.pt')

def check_model_accuracy():
    with open('metrics.csv', 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]
        lst = last_line.split(',')
        return (float(lst[2]) > float(0.7))
        
