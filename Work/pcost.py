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
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            cost += nshares * price
        except ValueError:
            print('Row:', rowno, "Couldn't parse", row)
    f.close()
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total cost:', cost)