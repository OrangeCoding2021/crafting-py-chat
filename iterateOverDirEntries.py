# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:53:43 2021

@author: OrangeCoding2021
"""

import os
import gzip as g


def fullSearch(term, path='', dateStart=0, dateEnd=0):
    # Get list of items in dir, for each item do the following
    for i in os.listdir(path):
        search(i,term)
            



def search(file,term):

        try:
            with g.open((file), 'rt') as f:
                for line in f.readlines():
                    if term in line:
                        print(f"{term} found in " + str(file))
                       
        except g.BadGzipFile:
            print(str(file)+"is not a GZip file... trying open")
            try:
                with open(file, 'r') as f:
                    for line in f.readlines():
                        if term in line:
                            print(f"{term} found in " + str(file))
                            
                            
            except:
                pass