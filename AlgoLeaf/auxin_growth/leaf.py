from auxin import AuxinNode
from venationPoint import VenationPoint
from math_stuff import get_distance
from math_stuff import get_newNode
from scipy.spatial import distance

import random


class Leaf:

    #struct shape
    VenationsList = {} #graphe
    AuxinsList = [] #just a list
    shape = None #for the momentb only a triangle
    KD_auxin = None
    KD_venation = None
    petiole = (0, 0)
    ax = None


    def __init__(self, kd_aux, kd_venation, _shape, _ax, nb_initial):
        self.KD_auxin = kd_aux
        self.KD_venation = kd_venation
        self.shape = _shape
        self.ax = _ax

        self.VenationsList[VenationPoint([0, 0])] = []
        self.gen_auxin(nb_initial)

    def display(self):
        self.shape.set_alpha(0.1)
        self.shape.set_facecolor("Green")
        self.ax.add_artist(self.shape)
        self.display_auxins()
        self.display_venNodes()

    def display_auxins(self):
        for auxin in self.AuxinsList:
            auxin.display()

    def display_venNodes(self):
        for ven in self.VenationsList:
            ven.display()


    def run_creation(self, nb_iterations):

        for i in range(nb_iterations):
            self.gen_nodes(0.3)
            self.kill_auxins()
            self.gen_auxin(1)
            self.grow_shape(0.01)

    def get_closest(self, aux):
        all_vens = list(self.VenationsList.keys())
        closest_index = distance.cdist([aux.position], [x.position for x in all_vens]).argmin()
        aux.closest = all_vens[closest_index]


    def gen_nodes(self, step):
        new_nodes =[]
        for ven in self.VenationsList.keys():
            aux = []
            for a in self.AuxinsList:
                if a.closest == ven:
                    aux.append(a)
            if aux:
                new_ven = get_newNode(ven, aux, step)
                for a in aux:
                    if get_distance(a, new_ven) < get_distance(a, ven):
                        a.closest = new_ven
                new_nodes.append(new_ven)
        for node in new_nodes:
            self.VenationsList[node] = []


    def gen_auxin(self, nb_auxin):
        Vertices = self.shape.get_xy()
        current_aux = 0
        while current_aux < nb_auxin:
            r1 = random.random()
            r2 = random.random()

            x_rand = (1 - r1 ** 0.5) * Vertices[0][0] + (r1 ** 0.5) * (1 - r2) * Vertices[1][0] + Vertices[2][
                0] * r2 * (r1 ** 0.5)
            y_rand = (1 - r1 ** 0.5) * Vertices[0][1] + (r1 ** 0.5) * (1 - r2) * Vertices[1][1] + Vertices[2][
                1] * r2 * (r1 ** 0.5)
            A = AuxinNode([x_rand, y_rand])

            to_append = True
            for auxin in self.AuxinsList:
                if get_distance(auxin, A) < self.KD_auxin:
                    to_append = False
                    break
            for ven in self.VenationsList:
                if get_distance(A,ven) < self.KD_venation:
                    to_append = False
                    break
            if to_append:
                self.get_closest(A)
                self.AuxinsList.append(A)
                current_aux += 1

    def kill_auxins(self):
        to_remove = []
        for aux in self.AuxinsList:
            if get_distance(aux, aux.closest) < self.KD_venation:
                to_remove.append(aux)
        for aux in to_remove:
            self.AuxinsList.remove(aux)

    def grow_shape(self, step):
        vertices = self.shape.get_xy()
        sign = lambda a: 1 if a > 0 else -1 if a < 0 else 0
        for v in vertices:
            v[0] += step * sign(v[0])
            v[1] += step * sign(v[1])
        vertices[1][1] += step * sign(vertices[1][1])




    """
    def venation_iteration:
        #Create the new venations associated with good auxins

    def auxin_iteration:
        #remove auxin in the kill distance
        #add new auxins
        #remove the auxins in kill distance

    def grow_leaf:
        print("growing")
        #WTF OMG
    """