
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
8. Write all .gz files to .txt files
-------------------------------------------------



    """
    print(menu)


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

        print("Option disabled for time being. Use display sections instead. ")
    elif answer == '2':
        writeToFile(current)
    elif answer == '3':
        sects = int(input("Enter how many lines to display at a time: "))
        dispSections(current, sects)
    elif answer == '4':

        dirOf, file = getDirAndFile(dirOf, file)
    elif answer == '5':
        listDirInSections(dirOf)
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
            print(f"Current Place: {count}/{leng}")


def dispSections(file, sects):
    """
    file - file to display
    sects - how many sections(lines) to display per page

    Displays contents of desired file in pages"""
    # Try to open a gzip file, if not open it as a file. (Possibly a better way to check the file type beforehand?)
    try:
        with g.open(file, 'rt') as f:
            # Few different ways to do this, another way is probably better but happy to have found one way at least
            fList = list(f)
            leng = len(fList)
            print(str(leng))

            # Initialize variables
            firstSplitPt = 0
            lastPt = sects
            continueDisplay = True
            # For each length of sections
            while continueDisplay:

                for line in fList[firstSplitPt:lastPt]:
                    print(line)
                count = lastPt

                #print(f"1st{firstSplitPt}last {lastPt}")

                # Update the two end counters accordingly

                skip = input(
                    f"Enter to continue. 'e' to exit. Integer to jump to around that line. Lines: {firstSplitPt+1} to {lastPt} End: {leng}.")

                if skip == 'e':
                    print("exiting...")
                    break
                # If string entered is a digit, jump to around that line
                elif skip.isdigit() and int(skip) <= leng and int(skip) >= 0:
                    skip = int(skip)
                    firstSplitPt = skip-int(sects/2)
                    if firstSplitPt < 0:
                        firstSplitPt = 0
                    elif firstSplitPt > leng+1:
                        firstSplitPt = leng + 1

                    lastPt = firstSplitPt + sects
                else:
                    firstSplitPt += sects
                    lastPt += sects
                    pass

                if lastPt > leng+1:
                    lastPt = leng+1
                # for j in range(sects):
                #     print(fList[count])
                #     count += 1
                #
                # skip = input(
                #     f"Enter to continue. 'e' to exit. Integer to jump to around that line. Lines displayed so far: {count}/{leng}")
                #
                # if skip == 'e':
                #     print("exiting...")
                #     break
                # # If string entered is a digit, jump to around that line
                # elif skip.isdigit() and int(skip) <= leng:
                #     skip = int(skip)
                #     count = skip-int(sects/2)
                # else:
                #     pass
                # # Handle where the first pt will be
                # firstSplitPt = count-int(sects/2)
                # if firstSplitPt >= leng:
                #     firstSplitPt = leng
                #     lastPt = leng+1
                # elif firstSplitPt <= 0:
                #     firstSplitPt = 0
                # lastPt = count+int(sects/2)
                # if lastPt > leng+1:
                #     lastPt = leng+1
                # elif lastPt < sects:
                #     lastPt = sects
                # else:
                #     pass
                #
                # for line in fList[firstSplitPt:lastPt]:
                #     print(line)
                # count = lastPt
                # print(f"Lines displayed: {count}/{leng}")
                # print(f"1st{firstSplitPt}last {lastPt}")

    except FileNotFoundError:
        print("Uh oh.. you probably typed this file wrong. Please enter filename and extension only.")


def displayAll(file):
    """Display all lines of the file"""
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
        try:

            with open(file+"-craftPyChat.txt", 'r') as out:
                print(".txt version already exists!")

        except:
            with g.open(file, 'rt') as f:
                with open(file+"-craftPyChat.txt", 'w') as out:

                    out.write(f.read())
                print("File written to: " + file + ".txt")

    except FileNotFoundError:
        print("Uh oh.. you probably typed this file wrong. Please enter filename and extension only.")


def getDirAndFile(dirOf=0, file=0):

    # Change the directory or file name being used. if left blank set to default.
    print("Please input directory or leave blank for default")
    currentInp = input("Directory: ")
    if currentInp != "":
        dirOf = os.path.normcase(currentInp)
    elif currentInp == "":
        dirOf = os.path.normcase = "C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\.minecraft\\logs"
        print(dirOf)

    while not os.path.isdir(dirOf):
        print("Please input directory again in a accepted format")
        dirOf = os.path.normcase(input())

    # Gets all files in directory
    fileslists = [f for f in os.listdir(str(dirOf)) if os.path.isfile(os.path.join(str(dirOf), f))] 
    # Creates a copy of the list because you cannot (reliably) modify a list while it is in use
    fileslistscopy = fileslists.copy()
    for x in fileslists:
        tmp = str(x).split(".")
        if "debug" in x or "latest" in x or tmp[-1] != "gz": # removes all entries that are not .gz or have debug/latest in the name
            fileslistscopy.remove(x)
    del fileslists # Cleanup
    print("Please input File name or leave blank for most recent found ("+str(fileslistscopy[-1])+")")
    currentInp = input("File name: ")
    if currentInp != "":
        file = currentInp
    elif currentInp == "":
        file = fileslistscopy[-1]

    while not os.path.isfile(os.path.join(dirOf, file)):
        print("Please input file again in a accepted format")
        file = input()

    del fileslistscopy # Cleanup
    return dirOf, file


def writeAllAll(dirOf):
    """Write all files in a given directory to txt files"""
    for i in os.listdir(dirOf):
        if ".gz" in os.path.splitext(os.path.join(dirOf, i))[-1]:
            writeToFile(os.path.join(dirOf, i))


if __name__ == '__main__':
    # Get file location from user

    dirOf, file = getDirAndFile()

    while True:

        displayMenu()
        menu(dirOf, file)
