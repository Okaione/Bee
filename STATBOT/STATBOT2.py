# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:39:16 2024

@author: esimm
"""

import numpy as np
from tkinter import filedialog as fd
import scipy.stats as stats
from .STATBOT1 import (
    statbot,
)  # You can do `statbot()` to invoke STATBOT1's functionality.


def getdata():
    """Get data from a file and return as a numpy array"""
    # Use open file dialog (from tkinter) to find the data file
    filename = fd.askopenfilename()
    # Read the data using Numpy
    data = np.loadtxt(filename)
    # The variable data is a numpy array
    return data


def stats2():
    """MAIN FUNCTION: Call this to run STATBOT2"""

    # Read data from a file; variable data is a numpy array
    data = getdata()
    # 1. Report the "shape" of the data (numbers of rows and columns)
    nrows, ncols = data.shape

    # f-strings are pretty useful. I rewrote the below one as an example.
    # They print the same thing.
    print("Data has", nrows, "cases", "and", ncols, "conditions")
    print(f"Data has, {nrows} cases and {ncols} conditions")

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
    my_rval = rvalue(data1, data2)
    print("t = ", tscore, "df =", n - 1)
    print("r = ", rscore, "df =", n - 2)
    print("My r = ", my_rval)


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


def tvalue(data1, data2):
    """Paired-samples t-value, data1 vs data2"""
    # Subtract data2 from data1 to get difference scores
    diffs = data1 - data2  # <- This isn't used, can it be deleted?
    tvalue = stats.ttest_rel(data1, data2)
    return tvalue


def rvalue(data1, data2):
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
