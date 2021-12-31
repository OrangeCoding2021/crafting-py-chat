# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:53:43 2021

@author: OrangeCoding2021
"""

import os
import gzip as g

# Get list of items in dir, for each item do the following
for i in os.listdir(""):
    #print("path to file excluding file"+i)
    
    try:
        with g.open(("path to file excluding file"+i), 'rt') as f:
            for line in f.readlines():
                if 'search term' in line:
                    print("search term found in " + str(i))
                    answer = input("help")
    except g.BadGzipFile:
        print(str(i)+"Not a GZip file... trying open")
        try:
            with open(("path to file excluding file"+i), 'r') as f:
                for line in f.readlines():
                    if 'search term' in line:
                        print("search term found in " + str(i))
                        answer = input("help")
                        
        except:
            pass