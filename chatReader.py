# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 09:49:42 2022

@author: OrangeCoding2021
"""




from colorama import Fore

#example = "Hi §cHello "
# Split at the prefix for colors and effects. Then analyxe each new string and based on first character add color
#Create a check for if it split at start or not
# splitText = example.split('§')
# for i, st in enumerate(splitText):
#     temp = st
#     comp = st[0]
#     if comp == '4':
    
#     if st[0] == 'c':
#         st=st.replace('c','',1)
        
#         temp = Fore.RED + st
#     splitText[i]=temp
# for txt in splitText:
    
#     print(txt)
    
def colorIn(char,st,temp,color):
    
    # Replace char defining the chat color or effect
    st=st.replace(char,'',1)
    
    # Return the new string part including the color effect
    
    return color + st
    
def convertChat(txt,prefix='§'):
    """Returns the string passed but now in color!
    Prefix typically should be § or &"""
    splitText = txt.split('§')
    for i, st in enumerate(splitText):
        # Get first char in string 
        first = st[0]
        
       
        if first == '0':
            
            temp=colorIn('0',st,temp,Fore.RED)
        elif first == '1':
            temp=colorIn('1',st,temp,Fore.GREEN)
        elif first == '2':
            temp=colorIn('2',st,temp,Fore.RED)
        elif first == '3':
            temp=colorIn('3',st,temp,Fore.RED)
        elif first == '4':
            temp=colorIn('4',st,temp,Fore.MAGENTA)
        elif first == '5':
            temp=colorIn('5',st,temp,Fore.RED)
        elif first == '6':
            temp=colorIn('6',st,temp,Fore.RED)
        elif first == '7':
            temp=colorIn('7',st,temp,Fore.RED)
        elif first == '8':
            temp=colorIn('8',st,temp,Fore.RED)
        elif first == '9':
            temp=colorIn('9',st,temp,Fore.RED)
        elif first == 'a':
            temp=colorIn('a',st,temp,Fore.RED)
        elif first == 'b':
            temp=colorIn('b',st,temp,Fore.RED)
        elif first == 'c':
            temp=colorIn('c',st,temp,Fore.RED)
        elif first == 'd':
            temp=colorIn('d',st,temp,Fore.RED)
        elif first == 'e':
            temp=colorIn('e',st,temp,Fore.RED)
        elif first == 'f':
            temp=colorIn('f',st,temp,Fore.RED)
        elif first == 'k':
            temp=colorIn('k',st,temp,Fore.RED)
        elif first == 'l':
            temp=colorIn('l',st,temp,Fore.RED)
        elif first == 'm':
            temp=colorIn('m',st,temp,Fore.RED)
        elif first == 'n':
            temp=colorIn('n',st,temp,Fore.RED)
        elif first == 'o':
            temp=colorIn('o',st,temp,Fore.RED)
        elif first == 'r':
            temp=colorIn('r',st,temp,Fore.RED)
        else:
            temp = splitText[i]
        
        splitText[i]=temp
        # Return the colored string
    return ''.join(splitText)


if __name__ == "__main__":
    text = convertChat(example)
    print(text)
    for txt in text:
        print(txt)
    