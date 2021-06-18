import csv
import math

with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    file = list(reader)
    
data = file[0]

def mean(data):
    n = len(data)
    total = 0
    
    for x in data:
        total += int(x)
        
    mean = total / n 
    
    return mean

sqaureList = []

for n in data:
    a = int(n) - mean(data)
    a = a ** 2
    sqaureList.append(a)
    
sum = 0

for i in sqaureList:
    sum = sum + i

result = sum / (len(data)-1) 
standardDeviation = math.sqrt(result)

print(standardDeviation)