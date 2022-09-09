import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
from scipy.ndimage.filters import gaussian_filter1d

def leakyReLU(x):
    out = np.copy(x)
    neg = np.where(x<0)
    out[neg] = x[neg] * 0.3
    return out

def dleakyReLU(x):
    out = np.ones_like(x)
    neg = np.where(x<0)
    out[neg] = 0.3
    return out

def tanh(x):
    return (np.e**x - np.e**(-x))/(np.e**x + np.e**(-x))

def sech(x):
    return (2*np.e**x)/(np.e**(2*x)+1)

def softmax(x):
    x = 2.0**x
    return x / 128.0

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -3, 3, -1, 1
ticks_frequency = 1

# Plot points
fig, ax = plt.subplots(figsize=(xmax - xmin, ymax - ymin))
x = np.arange(xmin-1, xmax+1, 0.1)
plt.plot(x, (leakyReLU(x)))
plt.plot(x, (dleakyReLU(x)))# gaussian_filter1d   , sigma=1

# Set identical scales for both axes
ax.set(xlim=(xmin-0.5, xmax+0.5), ylim=(ymin-0.5, ymax+0.5))

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create custom major ticks to determine position of tick labels
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])

# Create minor ticks placed at each integer to enable drawing of minor grid
# lines: note that this has no effect in this example with ticks_frequency=1
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

# Draw major and minor grid lines
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

fig.savefig("/home/julian/Matur/AlphaZeroTheory/fig.svg")

plt.show()