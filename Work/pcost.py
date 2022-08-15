# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f)
cost = 0

for line in f:
    row = line.split(',')
    shares = int(row[1]) 
    price = float(row[2].split(',')[0])
    cost = shares * price + cost
    
f.close()
print('Total cost', cost)