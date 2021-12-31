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
    elif answer == '2':
        writeToFile(file)
        
def displayAll(file):
    # Open GZip file in the read text mode
    with g.open(file, 'rt') as f:
            for line in f.readlines():
                print(line) 
def writeToFile(file):
    try:
        with g.open(file, 'rt') as f:
            with open(file+".txt",'w') as out:
                
                out.write(f.read())
    except FileNotFoundError:
        print("Uh oh.. you probably typed this file wrong. Please enter filename and extension only.")
    
if __name__ == '__main__':
    # Get file location from user
    rootOf = input("Root: ")
    while True:
        
        file = rootOf + input("File Location: ")
        displayMenu()
        menu(file)