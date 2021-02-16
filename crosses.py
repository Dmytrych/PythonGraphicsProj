from numpy import argwhere, isnan, sign
from scipy import optimize

# returns a dot from the cross of OY axe
def getCrossWithOY(func):
    crossY = func(0)
    if abs(crossY) != float("inf"):
        return (0, crossY)
    else:
        return None

# returns an array of dots from the crosses of OY axe
def getCrossWithOX(func, x_val, y_val):
    signums = sign(y_val)
    crosses = []
    for i in range(len(x_val)-1):
        if signums[i] + signums[i+1] == 0 or signums[i] == 0:
            dotX = optimize.brentq(func, x_val[i], x_val[i+1])
            if(abs(dotX) <= 1e-3):
                dotX = 0
            
            dotY = func(dotX)
            if isnan(dotY) or abs(dotY) > 1e-3:
                continue
            crosses.append((dotX, 0))
    
    return crosses

# returns all crosses with all coordinate axes
def getCrosses(func, x_val, y_val):
    return (getCrossWithOX(func, x_val, y_val), getCrossWithOY(func))