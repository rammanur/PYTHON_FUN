'''Create a vcard for each employee found in a csv file for Raisin Megacorp.

TODO:
1. Open the csv file for reading
2. Step through 1 line at a time (one employee at a time)
   2a.  split each line into fields
3. Create vcard string for that employee

We are using "String Interpolation" below

'''

import sys
import urllib

vcard_template = \
'''BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s

TITLE:%s
TEL;WORK;VOICE:%s

EMAIL;PREF;INTERNET:%s
END:VCARD
'''


def create_vcard(fname):
    "Create vcard for all employees found in a csv file that is provided"
    
    with open(fname) as f:
        f.seek(0)
        line = f.readline()
        while len(line) > 0:
           fields = line.strip().split(',')
           vcard = vcard_template % (fields[0], 
                                   fields[1],
                                   fields[1], 
                                   fields[0],
                                   fields[2],
                                   fields[4], 
                                   fields[3])
           print vcard
           url_template = "https://chart.googleapis.com/chart?cht=qr&chs=200x200&ch1=%s"
           u = urllib.urlopen(url_template % (vcard,))
           img = u.read()
           
           with open("%s_qr.png" % (fields[0],), 'wb') as pngfp:
               pngfp.write(img)
           
           line = f.readline()     

if __name__ == '__main__':
    filename = "raisin_team.csv"
    try:
        filename = sys.argv[1]
    except IndexError:
        print "No filename provided, defaulting to raising.csv as input"
    create_vcard(filename)
