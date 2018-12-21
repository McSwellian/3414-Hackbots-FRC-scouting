# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 00:12:39 2018

@author: Maxwell Ledermann
"""

import pickle
import os

def is_number(inpt):
    try:
        float(inpt)
        return True
    except ValueError:
        return False
    
while(True): 
    print("Type 'exit' or 'x' at any time to safely exit the program.")
    team_number = input("Enter team number: ")
    if team_number in ("exit","x"):
        break
    if is_number(team_number) == True:
        match_number = input("Enter match number, leave blank to cancel: ")
        if match_number in ("exit","x"):
            break
        elif match_number != "" and is_number(match_number) == True:
            scan = input("Press enter to begin scan, type any other value to cancel: ")
            if scan in ("exit","x"):
                break
            elif scan == "":
                keyword = True
                pickle.dump((team_number,match_number,keyword), open( "entry data.p", "wb" ))
            
    keyword = False
    clear = lambda: os.system('cls')
    clear()