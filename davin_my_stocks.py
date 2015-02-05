"""Monitors the value of our portfolio's stock holdings (from a csv file).

TODO:
  XXX. look in our csv file for ticker symbols
  XXX. get current price on each symbol
  XXX. compute net gain/loss
"""

import urllib


def get_current_price(symbol):
    "Obtains current price info from Yahoo Finance's RESTful service."
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv"
    u = urllib.urlopen(url % (symbol, ))
    response = u.read()
    fields = response.strip().split(',')
    current_price = float(fields[1])
    return current_price


def read_portfolio(filename):
    "Reads holding info from a given file name."
    holdings = []
    with open(filename) as f:
        for line in f:
            symbol, shares, price = line.strip().split(',')
            holdings.append( (symbol, int(shares), float(price)) )
    return holdings


if __name__ == '__main__':
    portfolio = read_portfolio("stocks.txt")

    returns = {}
    for holding in portfolio:
        symbol, shares, purchase_price = holding
        current_price = get_current_price(symbol)
        current_value = shares * current_price
        cost_basis = shares * purchase_price
        net_gain = current_value - cost_basis
        returns[symbol] = returns.setdefault(symbol, 0.0) + net_gain

    for symbol, net_gain in returns.items():
        print "%s: %f" % (symbol, net_gain)

