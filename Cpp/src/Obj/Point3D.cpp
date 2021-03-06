//
// Created by revetoon on 3/1/19.
//

#include <cmath>
#include "Point3D.hh"
#include "../Constants.hh"
#include "../Utils/dblutils.hh"

Point3D::Point3D(double x, double y, double z, double w) : x(x), y(y), z(z), w(w) {}

Point3D::Point3D()
    : x(0),
      y(0),
      z(0)
{}

Point3D::Point3D(double x, double y, double z) : x(x), y(y), z(z) {}

double Point3D::getX() const {
    return x;
}

double Point3D::getY() const {
    return y;
}

double Point3D::getZ() const {
    return z;
}

double Point3D::getW() const {
    return w;
}

bool Point3D::operator==(const Point3D &rhs) const {
    return x == rhs.x &&
           y == rhs.y &&
           z == rhs.z &&
           w == rhs.w;
}

bool Point3D::operator!=(const Point3D &rhs) const {
    return !(rhs == *this);
}

Point3D Point3D::operator+(const Vector3D &rhs) const {
    return Point3D(x + rhs.getX(), y + rhs.getY(), z + rhs.getZ());
}

Point3D Point3D::operator*(const Vector3D &rhs) const {
    return Point3D(x * rhs.getX(), y * rhs.getY(), z * rhs.getZ());
}

const Vector3D Point3D::operator-(const Point3D &rhs) const {
    return Vector3D(x - rhs.getX(), y - rhs.getY(), z - rhs.getZ());
}

void Point3D::setX(double x) {
    Point3D::x = x;
}

void Point3D::setY(double y) {
    Point3D::y = y;
}

void Point3D::setZ(double z) {
    Point3D::z = z;
}

void Point3D::setW(double w) {
    Point3D::w = w;
}

std::ostream& operator<<(std::ostream &out, const Point3D &p) {
    out << "X: " << p.getX() << std::endl;
    out << "Y: " << p.getY() << std::endl;
    out << "Z: " << p.getZ() << std::endl;
    return out;
}


std::size_t Point3D::hash::operator () (const Point3D &p) const {
    auto h1 = std::hash<double>{}(dblutils::trunc(p.x, constants::OBJ_DBL_PRECISION));
    auto h2 = std::hash<double>{}(dblutils::trunc(p.y, constants::OBJ_DBL_PRECISION));
    auto h3 = std::hash<double>{}(dblutils::trunc(p.z, constants::OBJ_DBL_PRECISION));
    auto h4 = std::hash<double>{}(dblutils::trunc(p.w, constants::OBJ_DBL_PRECISION));

    return h1 ^ h2 ^ h3 ^ h4;
}