import matplotlib.pyplot as plt
import numpy as np

nums = 500
minx = -2
maxx =  2
miny = -2
maxy =  2

def softmax_x(x, y):
    return np.e**x / (np.e**x + np.e**y)
def softmax_y(x, y):
    return np.e**y / (np.e**x + np.e**y)

x = np.linspace(minx, maxy, num=nums)
y = np.flip(np.linspace(miny, maxy, num=nums))

x, y = np.meshgrid(x, y)
plt.imshow(softmax_x(x, y), extent=[minx,maxx,miny,maxy], cmap=plt.cm.turbo)
plt.ylabel("dimension 1")
plt.xlabel("dimension 2")
plt.savefig("images/softmaxx.svg", bbox_inches='tight', pad_inches=0)
plt.clf()
plt.imshow(softmax_y(x, y), extent=[minx,maxx,miny,maxy], cmap=plt.cm.turbo)
plt.ylabel("dimension 1")
plt.xlabel("dimension 2")
plt.savefig("images/softmaxy.svg", bbox_inches='tight', pad_inches=0)
plt.clf()
plt.axes().get_xaxis().set_visible(False)
plt.imshow(np.array([np.linspace(0, 1, num=nums)]).T, extent=[0, 1, -1, 1], cmap=plt.cm.turbo, aspect=20)
plt.xlabel("scale")
plt.savefig("images/softmaxscale.svg", bbox_inches='tight', pad_inches=0)
plt.show()
plt.clf()