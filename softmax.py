import matplotlib.pyplot as plt
import numpy as np

nums = 500
val = 1.5
minx = -val
maxx =  val
miny = -val
maxy =  val

def softmax_x(x, y):
    return np.e**x / (np.e**x + np.e**y)
def softmax_y(x, y):
    return np.e**y / (np.e**x + np.e**y)

x = np.linspace(minx, maxy, num=nums)
y = np.flip(np.linspace(miny, maxy, num=nums))

x, y = np.meshgrid(x, y)
plt.imshow(softmax_x(x, y), extent=[minx,maxx,miny,maxy], cmap=plt.cm.turbo)
plt.ylabel(r"$v_{1}$")
plt.xlabel(r"$v_{2}$")
plt.savefig("images/softmaxx.svg", bbox_inches='tight', pad_inches=0)
plt.clf()
plt.imshow(softmax_y(x, y), extent=[minx,maxx,miny,maxy], cmap=plt.cm.turbo)
plt.ylabel(r"$v_{1}$")
plt.xlabel(r"$v_{2}$")
plt.savefig("images/softmaxy.svg", bbox_inches='tight', pad_inches=0)
plt.clf()
plt.axes().get_xaxis().set_visible(False)
plt.imshow(np.array([np.linspace(0, 1, num=nums)]).T, extent=[0, 1, -1, 1], cmap=plt.cm.turbo, aspect=20)
plt.xlabel("scale")
plt.savefig("images/softmaxscale.svg", bbox_inches='tight', pad_inches=0)
#plt.show()
plt.clf()

#plt.xlabel(r"$s_{a}$")
#plt.ylabel(r"$r_{a}$")