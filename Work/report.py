# report.py
#
# Exercise 2.4

import fileparse
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of distionaries with keys
    name, shares, and price.
    '''
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str, int, float])

def read_prices(filename):
    return dict(fileparse.parse_csv(filename, has_headers=False))

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

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)