# pcost.py
#
# Exercise 1.27

import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)

    cost = 0
    for rowno, row in enumerate(portfolio):
        try:
            cost += row['shares'] * row['price']
        except ValueError:
            print('Row:', rowno, "couldn't parse")

    return cost
