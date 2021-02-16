import matplotlib.pyplot as plt
from numpy import arange, log
from crosses import getCrosses

# returns two arrays: x-values, generated in the range, and y-values = func(x) on this range
def getFunctionArrays(func, start, end, tab):
    x_val = tab * arange(start / tab, end / tab)
    y_val = func(x_val)
    return (x_val, y_val)

# draws the graph using matplotlib instruments on arrays on values
def drawGraph(x_val, y_val):
    plt.plot(x_val, y_val, '-')
    plt.show()

# getting data from the user
def getAllNecessaryData():
    print("Welcome!")
    return list(map(lambda v: float(v), input("Input please the start value, finish value and tab for the function y=ln(x)/x: ").split(' ')))

# prints crosses with coordinate axes
def printCrosses(crossesX, crossY):
    print()
    if len(crossesX) == 0:
        print("There is no crosses with OX")
    else:
        print("Crosses with OX: ")
        for dot in crossesX:
            print(dot)

    if crossY is not None:
        print("Cross with OY: ")
        print(crossY)
    else:
        print("There is no crosses with OY")

# function from the variant: y = ln(x) / x
func = lambda x: x**2 + 2

[start, end, tab] = getAllNecessaryData()

(x, y) = getFunctionArrays(func, start, end, tab)
(crossesX, crossY) = getCrosses(func, x, y)

printCrosses(crossesX, crossY)
drawGraph(x, y)
