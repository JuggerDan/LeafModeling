from matplotlib.patches import Polygon
from leaf import Leaf
from leaf_shape import first_param
from pylab import *

if __name__ == '__main__':




    leaf_shape = Polygon([(-1, 0), (0, 3), (1, 0)], closed=True)

    Bob = Leaf(0.5, 0.6, leaf_shape,150, 4, 0.004)

    Bob.run_creation(1300)

    Bob.display(8, 15)



    #Leaf = first_param(None, 2.8)
   # Leaf.plot_shape(2.8)
