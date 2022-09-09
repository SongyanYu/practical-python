# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_error=True):
    '''
    Parse a CSV file into a list of records
    '''
    if not has_headers and select:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if select:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_error:
                        print('Couldn\'t convert', row)
                        print('Reason:', e)
            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records

portfolio = parse_csv('Data/portfolio.csv')
portfolio

shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'])
shares_held

portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
portfolio

shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
shares_held

prices = parse_csv('Data/prices.csv', types=[str, float], has_headers=False)
prices

portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
portfolio

parse_csv('Data/prices.csv', select=['name', 'price'], has_headers=False)

portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
