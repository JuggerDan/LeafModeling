import random as rand

from pylab import *
import matplotlib.patches as patches

class first_param:

    growth_size = 0

    equation = None
    rectangle = None #where to project the points
    ax = None
    growth_x = None
    growth_y = None
    points = []

    def __init__(self, equation, _growth, rectangle, _growth_x = 1,
                 _growth_y = 1):
        self.equation = equation
        self.growth_size = _growth
        self.rectangle = rectangle
        self.growth_x = _growth_x
        self.growth_y = _growth_y


    def plot_shape(self, ax):
        x = np.linspace(-1.0, 1.0, 1000)
        y = np.linspace(-0.5, 2.0, 1000)
        X, Y = np.meshgrid(x, y)
        ax.contour(X, Y, self.equation(X, Y, self.growth_size, self.growth_x, self.growth_y), [0])
        x = self.rectangle[0][0]
        y = self.rectangle[0][1]
        x_lim = x + self.rectangle[1]
        y_lim = y + self.rectangle[2]

        rect = patches.Rectangle((x, y), x_lim, y_lim, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)




    def plot_points(self, coord):
        plot(coord[0], coord[1], 'bo')


    def gen_point(self):
        coord = None
        find = False
        x = self.rectangle[0][0]
        y = self.rectangle[0][1]
        x_lim = x + self.rectangle[1]
        y_lim = y + self.rectangle[2]
        while not find:
            r1 = x + random() * (x_lim - x)
            r2 = y + random() * (y_lim - y)

            if 0.02 >= self.equation(r1, r2, self.growth_size,self.growth_x, self.growth_y) >= -0.01:
                find = True
                coord = [r1, r2]
        return coord



