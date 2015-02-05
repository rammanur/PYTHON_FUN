'Acquire mountain information and convert it to a convenient form'

import re
import urllib
import BeautifulSoup

url = 'http://www.factmonster.com/ipka/A0001771.html'

def get_min_summit():
    'Named summits over a certain minimum height'
    f = urllib.urlopen(url)
    page = f.read()
    mo = re.search(r'Over\s+([0-9,]+)\s+Feet', page)
    return int(mo.group(1).replace(',' ,''))

def get_mountain_table():
    'Return a list of lists with the parsed Mountain data'

    f = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(f)
    table = soup.find('table', id="A0001772")

    tabledata = []
    for row in table.findAll('tr'):
        rowdata = [col.text for col in row.findAll('td')]
        tabledata.append(rowdata)
    return tabledata

if __name__ == '__main__':
    from pprint import pprint

    print get_min_summit()
    pprint(get_mountain_table(), width=200)

