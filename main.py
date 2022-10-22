from this import d
import numpy as np
from math import e, floor, ceil, comb
import matplotlib.pyplot as plt

def tanh(x):
    out = np.copy(x)
    neg = np.where(x<0)
    out[neg] = x[neg] * 0.3
    return out

def elo(x):
    return 1/(1+e**((0-x)/400))

def elo_back(x):
    return 0 - np.log((1-x)/x)*400


x = np.arange(0, 1, 0.001)
print(x)
plt.plot(x, elo_back(x))
plt.xlabel(r"$s_{a}$")
plt.ylabel(r"$r_{a}$")
plt.savefig("images/elo_back.svg")
plt.show()

