# report.py
#
# Exercise 2.4

import csv
def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio

import csv

def read_prices(filename):
    prices= {}

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) != 0:
                prices[row[0]] = row[1]

    return prices

def make_report(portfolio, prices):
    report = []
    for name, shares, price in portfolio:
        price_new = prices[name]
        change = price - float(price_new)
        summary = (name, shares, '$'+price_new, change)
        report.append (summary)
    return report

portfolio = read_portfolio('Data/portfolio.csv')

from collections import Counter
holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']


prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' %headers)
print(('-' * 10 + ' ')* len(headers))
for r in report:
    print('%10s %10d %10s %10.2f' %r)

