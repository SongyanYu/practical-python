# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    import csv
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    cost = 0
    for row in rows:
        try:
            shares = int(row[1])
        except ValueError:
            print("Couldn't parse", row)
        price = float(row[2].split(',')[0])
        cost = shares * price + cost
    f.close()
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total cost:', cost)