# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:19:40 2013

Uses TCP, Beaustiful Soup tr
@author: rammanur
"""
import notes.BeautifulSoup
import urllib
import re

URL = "http://www.factmonster.com/ipka/A0001771.html"

def get_minimum_height(url):
    "Retrieves page at url and extracts minimum peak height as int."
    u = urllib.urlopen(url)
    raw_html = u.read()
    match = re.search("Over\s+([0-9,]+)\s+Feet", raw_html)
    minimum_height = int(match.group(1).replace(',', ''))
    return minimum_height

def get_all_table_data(URL):
    u = urllib.urlopen(URL)
    soup = notes.BeautifulSoup.BeautifulSoup(u)
    table = soup.find('table', id="A0001772")
    table_data = []
    for table_row in table.findAll('tr'):
        # List comprehension in next line
        values = [cell.getText() for cell in table_row.findAll('td')]
        if values:
            table_data.append(values)
    return table_data