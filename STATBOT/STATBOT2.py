# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:39:16 2024

@author: esimm
"""

import numpy as np
from tkinter import filedialog as fd
import scipy.stats as stats
from STATBOT1 import statbot  # You can do `statbot()` to invoke STATBOT1's functionality.
from datetime import datetime



def getdata():
    """Get data from a file and return as a numpy array"""
    # Use open file dialog (from tkinter) to find the data file
    filename = fd.askopenfilename()
    # Read the data using Numpy
    data = np.loadtxt(filename)
    # The variable data is a numpy array
    return data


def stats2():
    """ OTHER ANALYSIS:
    ~ Z-Score
    ~ Standard Error
    ~ T-Score
    ~ R-Score
    
    3 EXIT MENU"""

    # Read data from a file; variable data is a numpy array
    data = getdata()
    # 1. Report the "shape" of the data (numbers of rows and columns)
    nrows, ncols = data.shape

    # f-strings are pretty useful. I rewrote the below one as an example.
    # They print the same thing.
    print(f"Data has {nrows} cases and {ncols} conditions")

    # 2. Assign columns 0 and 1 of the data to variables
    # Uses numpy notation, ":" means "all the rows"
    data1 = data[:, 0]  # column 0
    data2 = data[:, 1]  # column 1
    n = nrows
    # 3. Compute correlation
    # t value via scipy
    tscore = stats.ttest_rel(data1, data2)
    # r value via scipy
    rscore = stats.pearsonr(data1, data2)
    print("t = ", tscore, "df =", n - 1)
    print("r = ", rscore, "df =", n - 2)
    




def zscore(data):
    """z score written as a function, with the raw data as input"""
    M = np.mean(data)
    # center the data
    centered = data - M
    # zed transform
    score = centered / np.std(data)
    return score


# reimplementing a function from statbot1. This is error prone if you need to make changes.
# Could just import it:
# from .STATBOT1 import se
def SE(data):
    """Standard error of the data"""
    return np.std(data, ddof=1) / np.sqrt(len(data))


def tscore(data1, data2):
    """Paired-samples t-value, data1 vs data2"""
    # Subtract data2 from data1 to get difference scores
    tvalue = stats.ttest_rel(data1, data2)
    return tvalue


def rscore(data1, data2):
    """Compute r-value (Pearson Correlation)"""
    # zed score of both inputs
    zed1 = zscore(data1)
    zed2 = zscore(data2)
    # multiply z-scores of data together
    z1x2 = zed1 * zed2
    # get the sum of the products of the z-scores
    sum_z = np.sum(z1x2)
    # return the sum/N
    r_val = sum_z / len(data1)
    return r_val

def save_results(analysis):
    statNames = [
        "Z-Score"
        "Standard Error"
        "T-Score"
        "R-Score",
    ]
    analysis = [zscore, SE, tscore, rscore]
    print("/n------ STATBOT: DESCRIPTIVE STATS! ------")
    for statName, res in zip(statNames, analysis):

        saveFileName = fd.asksaveasfilename()

        resultsFile = open(saveFileName, "w", encoding='utf-8')

        result = statName + "=" + str(res)

        resultsFile.write(result + "/n")  # You can add strings with +

        # resultsFile.write("/n")

        DT = datetime.now()

        resultsFile.write(str(DT) + "/n")

    print("Results saved to", saveFileName)

    resultsFile.close()
    
def exitMenu():
    """Exit the Menu """
    #dummy function to provide the exit option in the menu
    pass #do nothing
    
def menu():
    print('n/STATBOT Functions')
    all_functions = [statbot, stats2]
    #make a Python dictionary of the demos, each demo is
    #assigned an index starting at 1
    menu_items = dict(enumerate(all_functions, start=1))
    exit_code = len(all_functions) #exit is the last option on menu
    
    while True:
        print('\nSTATBOT Functions ~ What type of analysis would you like to run?')
        #Show the menu in the console
        display_menu(menu_items)
        #get selected index to menu item from user
        selection = int(
            input("Please enter your selection number: "))
        
        if selection > exit_code: #quit if input number is exit or greater
           print('Goodbye dear friend!')
           break #exit the while loop
           
        else: 
            selected_function = menu_items[selection]  # Get the demo function
            selected_function()  # add parentheses to call the demo
            
         
                  
           
def display_menu(menu):
    
    for k,  functions in menu.items():
        doc = functions.__doc__ #get the docstring of the function
        print(k, doc)

#The following will run the demo menu when the file is run
if __name__ == "__main__":
    menu()           

