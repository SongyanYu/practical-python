# report.py
#
# Exercise 2.4

import csv
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of distionaries with keys
    name, shares, and price.
    '''
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
    for s in portfolio:
        price_new = prices[s['name']]
        change = s['price'] - float(price_new)
        summary = (s['name'], s['shares'], '$'+price_new, change)
        report.append(summary)
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10s %10.2f' % r)

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')

files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, 'Data/prices.csv')
    print()