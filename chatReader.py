# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 09:49:42 2022

@author: OrangeCoding2021
"""
import colorama
from colorama import Fore

example = "Hi &cHello &nothing"
# Split at the prefix for colors and effects. Then analyxe each new string and based on first character add color
#Create a check for if it split at start or not
splitText = example.split('&')
for i, st in enumerate(splitText):
    temp = st
    if st[0] == 'c':
        st=st.replace('c','',1)
        
        temp = Fore.RED + st
    splitText[i]=temp
for txt in splitText:
    
    print(txt)