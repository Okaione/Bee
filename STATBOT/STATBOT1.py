# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:37:35 2024

@author: esimm
"""
import numpy as np

# import tkinter to use Windows OFD
from tkinter import filedialog as fd

# import math to calculate descriptive statistics
import math

# import datetime to time stamp results file
from datetime import datetime

# import scipy.stats to calculate kurtosis and skew
from scipy.stats import kurtosis
from scipy.stats import skew


def readdata():
    """Get data from a file and return as a numpy array"""
    # Use open file dialog (from tkinter) to find the data file
    filename = fd.askopenfilename()
    # Read the data using Numpy
    data = np.loadtxt(filename)
    # The variable data is a numpy array
    return data


# Calculate and return the sum of all datapoints.
# Function could be replaced by `np.sum(data)` wherever it's used.
def summ(data):
    total = 0
    for dataPoint in data:
        total = total + (dataPoint)
        return total
    print("The sum of all datapoints is", summ(data))


# Calculate and return the mean of all datapoints.
# Function could be replaced by `np.mean(data)` wherever it's used.
def mean(data):
    """Mean of the data"""
    print("The mean of the data set is", summ(data) / len(data))
    return summ(data) / len(data)


# Calculate and return the smallest datapoint.
# Function could be replaced by `min(data)` wherever it's used.
def mini(data):
    """Find the minimum value in a data set"""
    smallest = data[0]

    for item in data:
        if item < smallest:
            smallest = item
    print("The smallest datapoint is", smallest)
    return smallest


# Calculate and return the largest datapoint.
# Function could be replaced by `max(data)` wherever it's used.
def maxi(data):
    """Find the maximum value in a data set"""
    largest = data[0]

    for item in data:
        if item > largest:
            largest = item
    print("The largest datapoint is", largest)
    return largest


# Calculate the difference between the smallest and largest datapoint.
# maxi and mini functions could be replaced by `max/min(data)`.
def rangeof(data):
    print("The range is", maxi(data) - mini(data))
    return maxi(data) - mini(data)


# Any reason you need this function? Could just call `skew` directly.
# This just adds a print statement to it.
def skw(data):
    # Calculate skew.
    print("The skew of the data set is", skew(data, axis=0, bias=True))
    return skew(data, axis=0, bias=True)


# Any reason you need this function? Could just call `kurtosis` directly.
# This just adds a print statement to it.
def kurt(data):
    # Calculate kurtosis.
    print("The kurtosis of the data set is", kurtosis(data, axis=0, bias=True))
    return kurtosis(data, axis=0, bias=True)


# Calculate and return SSE.
def sse_func(data):
    """sum squared error of data"""
    mu = mean(data)
    sse_var = 0
    for item in data:
        diff_2 = (item - mu) ** 2
        sse_var = sse_var + diff_2

    print("The sum squared error of the datapoints is", sse_var)
    return sse_var


# Calculate and return the variance in the data set.
# Function could be replaced by `np.var(data)` wherever it's used.
def var(data, sample=1):
    """variance of the data"""
    n = len(data) - sample
    variance = sse_func(data) / n
    print("The variance of the data set is", variance)
    return variance


# Calculate and return the standard deviation in the data set.
# Function could be replaced by `np.std(data)` wherever it's used.
def sd(data):
    """standard deviation of the data"""
    deviation = var(data) ** 0.5
    print("The standard deviation of the data set is", deviation)
    return deviation


# Calculate and return the standard error in the data set.
def se(data):
    """standard error of the data"""
    std_err = sd(data) / math.sqrt(len(data))
    print("The standard error of the data set is", std_err)
    return std_err


def dostats(data):
    """compute all descriptive statistics and show the results"""
    SUM = summ(data)
    MEAN = mean(data)
    MAX = maxi(data)
    MIN = mini(data)
    SSE = sse_func(data)
    RANGEOF = rangeof(data)
    VAR = var(data, sample=1)
    SD = sd(data)
    KURTOSIS = kurt(data)
    SKEW = skw(data)
    SE = sd(data) / math.sqrt(len(data))

    # Could use:
    # SUM = np.sum(data)
    # MEAN = np.mean(data)
    # MAX = max(data)
    # MIN = min(data)
    # SSE = sse_func(data)
    # RANGEOF = rangeof(data)
    # VAR = np.var(data, sample=1)
    # SD = np.std(data)
    # KURTOSIS = kurtosis(data)
    # SKEW = skew(data)
    # SE = np.std(data) / math.sqrt(len(data))

    descriptives = [SUM, MEAN, MAX, MIN, SSE, RANGEOF, VAR, SD, SE, KURTOSIS, SKEW]

    return descriptives


def save_results(descriptives):
    statNames = [
        "Sum",
        "Mean",
        "Maximum",
        "Minimum",
        "SSE",
        "Range",
        "Variance",
        "SD",
        "SE",
        "Kurtosis",
        "Skew",
    ]
    print("/n------ STATBOT: DESCRIPTIVE STATS! ------")
    for statName, res in zip(statNames, descriptives):

        saveFileName = fd.asksaveasfilename()

        resultsFile = open(saveFileName, "w", encoding="utf-8")

        result = statName + "=" + str(res)

        resultsFile.write(result + "/n")  # You can add strings with +

        # resultsFile.write("/n")

        DT = datetime.now()

        resultsFile.write(str(DT) + "/n")

    print("Results saved to", saveFileName)

    resultsFile.close()


def statbot():
    """MAIN FUNCTION TO LINK STATBOT TOGETHER"""

    # 1. Get the data to be analysed
    data = readdata()

    # 2. Do descriptives on the data
    results = dostats(data)

    # 3. Save the results to a text file
    save_results(results)


def main() -> None:  # pragma: no cover
    """Entry point for module."""
    statbot()
    return


if __name__ == "__main__":
    main()  # This lets you invoke the script by `python -m <script_name>`
