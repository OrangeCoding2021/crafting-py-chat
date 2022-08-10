# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:53:43 2021

@author: OrangeCoding2021
"""

import os
import gzip as g


def fullSearch(term, path, dateStart=0, dateEnd=0):
    """
    term - string to search
    path - directory the search
    dateStart - eventually a sorting method
    dateEnd - eventually a sorting method

    Function outputs to console every occurance of that term in the log files.
    """
    # Get list of items in dir, for each item do the following
    for i in os.listdir(path):
        # Validate file type.
        if ".gz" in os.path.splitext(os.path.join(path, i))[-1]:
            # If right type of file, search
            print("Searching... " + str(i))
            search(os.path.join(path, i), term)


def search(file, term):
    """
    file - file to perform the search in
    term - search term

    Searches given file for specified string
    """
    try:
        linenum = 0
        # Open file and output the lines the search term is found on
        with g.open((file), 'rt') as f:
            for line in f.readlines():
                linenum += 1
                if term in line:
                    print(f"{term} found on line {linenum} ")

    except g.BadGzipFile:
        print(str(file)+"is not a GZip file... trying open")
        # Think about removing because of limited use case only really good for
        # When a file in the directory is a text file already
        # If it is not a gZip file tries opening file regularly
        try:
            linenum = 0
            with open(file, 'r') as f:
                print("Sucessfully opened !")
                for line in f.readlines():
                    linenum += 1
                    if term in line:
                        print(f"{term} found on line {linenum} ")

        except:
            print("Open failed as well")
            pass
