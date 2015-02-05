# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:35:18 2013


TODO:

@author: rammanur
"""

import urllib

URL="http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv"

def get_stock_price(stock_symbol):
    "Obtains stock info for provided Stock Symbol"
    url = urllib.urlopen(URL % stock_symbol)
    response = url.read()
    fields = response.strip().split(',')
    current_price = float(fields[1])
    return current_price

    
def read_portfolio(fname, stockname):
    holdings = [] #List
    all_stock_info = {} #Dictionary
    print "My stocks\n---------\n"
    with open(fname) as f:
         for holdings in f:
             symbol, shares, price = holdings.strip().split(',')
             all_stock_info[symbol] = get_stock_price(symbol)
    return all_stock_info

if __name__ == '__main__':
    stock_details = read_portfolio("stocks.txt", "GOOG")
    for symbols in stock_details.keys(): #using dictionary keys
        print "%s:" % symbols, stock_details[symbols] #using dictionary values