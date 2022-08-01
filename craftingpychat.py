
"""
Created on Wed Dec 29 21:18:22 2021

@author: OrangeCoding2021
"""

# Import needed modules
import gzip as g
import os

# Import own modules
from iterateOverDirEntries import search, fullSearch


def displayMenu():
    """ Displays the menu"""
    menu = """
-------------------------------------------------
1. Display all
2. Write all to file
3. Display Sections
4. Redo file info (leaving one as blank keeps old)
5. List files in a directory
6. Search a whole file
7. Search a whole directory
8. Write All All
-------------------------------------------------



    """
    print(menu)


def writeAllAll(dirOf):
    """Write all files in a given directory to txt files"""
    for i in os.listdir(dirOf):
        writeToFile(os.path.join(dirOf, i))


def menu(dirOf, file):
    """
    dirOf - directory in use
    file - current file in use

    Handles menu operations"""
    answer = input("Enter a menu choice: ")

    # Directory the current file is found + the file name
    current = os.path.join(dirOf, file)
    print(current)
    if answer == '1':

        displayAll(current)
    elif answer == '2':
        writeToFile(current)
    elif answer == '3':
        sects = int(input("Enter how many lines to display at a time: "))
        dispSections(current, sects)
    elif answer == '4':

        dirOf, file = getDirAndFile()
    elif answer == '5':
        path = input("Enter Directory: ")
        listDirInSections(path)
    elif answer == '6':
        term = input("Search Term: ")
        search(current, term)
    elif answer == '7':
        term = input("Search Term: ")
        fullSearch(term, dirOf, 0, 0)
    elif answer == '8':
        writeAllAll(dirOf)
    else:
        print("Invalid Option")


def listDirInSections(path='', sects=10):
    """
    path - directory desired
    sects - amount of items to display per page

    Lists files in directory in pages"""
    dirList = os.listdir(path)
    # Few different ways to do this, another way is probably better but happy to have found one way at least

    # Get length of the list of files
    leng = len(dirList)
    print(str(leng))

    # Get the amount of times the loop can loop before running into a error
    amount = leng//sects
    # Get the amount of items left after the safe looping
    left = leng % sects
    count = 0
    # For each length of sections
    for i in range(amount):

        # Display the amount of items requested
        for j in range(sects):
            print(dirList[count])
            count += 1

        skip = input(
            f"Hit enter to continue. e to exit. Lines displayed so far: {count}/{leng}")
        if skip == 'e':
            print("exiting...")
            break
        # For the remaining items after the safe loop. Could maybe move this out of the for i loop?
        # Maybe not once a back option is implemented? Perhaps look at another page method?
        if not count+sects <= leng:
            for line in dirList[count:count+left]:
                print(line)
                count += 1
            print(f"Lines displayed: {count}/{leng}")


def dispSections(file, sects):
    """
    file - file to display
    sects - how many items to display per page

    Displays contents of desired file in pages"""
    # Try to open a gzip file, if not open it as a file. (Possibly a better way to check the file type beforehand?)
    try:
        with g.open(file, 'rt') as f:
            # Few different ways to do this, another way is probably better but happy to have found one way at least
            fList = list(f)
            leng = len(fList)
            print(str(leng))
            amount = leng//sects
            left = leng % sects
            count = 0
            # For each length of sections
            for i in range(amount):

                for j in range(sects):
                    print(fList[count])
                    count += 1

                skip = input(
                    f"Hit any key to continue. Lines displayed so far: {count}/{leng}")
                if not count+sects <= leng:
                    for line in fList[count:count+left]:
                        print(line)
                        count += 1
                    print(f"Lines displayed: {count}/{leng}")

    except FileNotFoundError:
        print("Uh oh.. you probably typed this file wrong. Please enter filename and extension only.")


def displayAll(file):
    try:
        # Open GZip file in the read text mode
        with g.open(file, 'rt') as f:
            for line in f.readlines():
                print(line)

                # Look into checking what throws OSError
    except FileNotFoundError:
        print("File not found. Prob forgot to do the directory right oops")


def writeToFile(file):
    try:
        with g.open(file, 'rt') as f:
            with open(file+".txt", 'w') as out:

                out.write(f.read())

    except FileNotFoundError:
        print("Uh oh.. you probably typed this file wrong. Please enter filename and extension only.")


def getDirAndFile(dirOf=0, file=0):

    # Change the directory or file name being used. if left blank keep the currently used one.
    currentInp = input("Directory: ")
    if currentInp != '':
        dirOf = os.path.normcase(currentInp)

    while not os.path.isdir(dirOf):
        print("Please input directory again in a accepted format")
        dirOf = os.path.normcase(input())

    currentInp = input("File name: ")
    if currentInp != '':
        file = currentInp
    while not os.path.isfile(os.path.join(dirOf, file)):
        print("Please input file again in a accepted format")
        file = input()

    return dirOf, file


if __name__ == '__main__':
    # Get file location from user

    dirOf, file = getDirAndFile()

    while True:

        displayMenu()
        menu(dirOf, file)
