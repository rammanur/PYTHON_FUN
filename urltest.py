# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:52:58 2013

@author: rammanur
"""

import urllib

url = "https://chart.googleapis.com/chart?cht=qr&chs=200x200&ch1=http://python.org"

u = urllib.urlopen(url)
img = u.read()

with open("python_qr.png", 'wb') as f:
    f.write(img)
