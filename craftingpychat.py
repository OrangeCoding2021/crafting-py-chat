
"""
Created on Wed Dec 29 21:18:22 2021

@author: OrangeCoding2021
"""

# Import needed modules
import gzip as g

from chatReader import convertChat

def displayMenu():
    menu = """
1. Display all
2. Write all to file
3. Display Sections
4. Redo file info (leaving one as blank keeps old)
 
    """
    print(menu)
    
def menu(file):

    answer = input("Enter a menu choice: ")
    
    
    
    if answer == '1':
        displayAll(file)
    elif answer == '2':
        writeToFile(file)
    elif answer == '3':
        sects = int(input("how many lines display at a time?: "))
        dispSections(file, sects)
    elif answer == '4':
        rootOf = input("Root: ") 
        rootOf, file = getRootAndFile()

    else:
        print("Invalid Option")
def dispSections(file, sects):
    try:
        with g.open(file, 'rt') as f:
            # Few different ways to do this, another way is probably better but happy to have found one way at least
            fList = list(f)
            leng = len(fList)
            print(str(leng))
            amount = leng//sects
            left = leng%sects
            count=0
            # For each length of sections
            for i in range(amount):
                
                for j in range(sects):
                    print(fList[count])
                    count+=1

                dummy=input(f"Hit Enter to continue. Lines displayed so far: {count}/{leng}")
                if not count+100 <= leng:
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
                    print(convertChat(line,'§')) 
                    
                    # Look into checking what throws OSError
    except FileNotFoundError:
        print("File not found. Prob forgot to do the root right oops")
                
                
def writeToFile(file):
    try:
        with g.open(file, 'rt') as f:
            with open(file+".txt",'w') as out:
                
                out.write(f.read())
    except FileNotFoundError:
        print("Uh oh.. you probably typed this file wrong. Please enter filename and extension only.")
    
def getRootAndFile():
    currentInp = input("Root: ") 
    if currentInp != '':
        rootOf = currentInp
    currentInp  = input("File name: ")
    if currentInp != '':
        file = currentInp
    
    return rootOf, file
    
if __name__ == '__main__':
    # Get file location from user
     
    rootOf, file = getRootAndFile()
    file = rootOf + file
    while True:
        
        
        displayMenu()
        menu(file)