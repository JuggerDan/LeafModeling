 //
// Created by dany on 25/05/19.
//

#include "Nodes.hh"
#include <math.h>

namespace Nodes {


VenNodePlot::VenNodePlot(std::vector<Nodes::VenNodePlot> child_list, Point3D position) {

    pos = position;
    childrens = child_list;
    if (!childrens.empty()) {
        double sum;
        for (auto &v: childrens) {
            sum += pow(v.radius, 2);

        }

        radius = pow(sum, 0.5);
    } else {

        radius = 1;

    }


}


bool Nodes::AuxinPoint::operator==(const Nodes::AuxinPoint &aux) {

        return pos == aux.pos;
}


bool operator==(const Nodes::VenationPoint &ven1, const Nodes::VenationPoint &ven2) {

    return ven1.pos == ven2.pos;
}


}