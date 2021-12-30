# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:18:22 2021

@author: OrangeCoding2021
"""

# Import needed modules
import gzip as g





    
def displayMenu():
    menu = """
    1. Display all
    2. Display sections
    3. Change file selection
    4. Use list of files
    """
    print(menu)
def menu(file):

    answer = input("Enter a menu choice: ")
    
    # Add logic to re display or exit if invalid choice
    
    if answer == '1':
        displayAll(file)
        
def displayAll(file):
    # Open GZip file in the read text mode
    with g.open(file, 'rt') as f:
            for line in f.readlines():
                print(line) 


    
if __name__ == '__main__':
    # Get file location from user
    file = input("File Location: ")
    displayMenu()
    menu(file)