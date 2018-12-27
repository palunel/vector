from operator import add, sub
import math


class Vector:

    @classmethod
    def to_spherical(cls, c_vector):
        x = c_vector[0]
        y = c_vector[1]
        z = c_vector[2]
        r = math.sqrt(x**2 + y**2 + z**2)
        theta = math.atan2(y, x)
        phi = math.atan2(math.sqrt(x**2 + y**2), z)
        return Vector(r, math.degrees(theta), math.degrees(phi))

    def __init__(self, length, theta, phi):
        self.length = length
        self.theta = theta % 360
        self.phi = phi % 360

    def __str__(self):
        return (f"({self.length}, {self.theta}, {self.phi})")

    def __add__(self, other):
        summed_vectors = list(
            map(add, self.to_cartesian(), other.to_cartesian()))
        return self.to_spherical(summed_vectors)

    def __sub__(self, other):
        subbed_vectors = list(
            map(sub, self.to_cartesian(), other.to_cartesian()))
        return self.to_spherical(subbed_vectors)

    def __mul__(self, other):
        try:
            product = self.length * other
        except TypeError as ex:
            print(ex)
            print("\nBuilt in mulitplication only valid with scalar values.  For dot product or cross product, use respective dot and cross functions.")
        else:
            return Vector(product, self.theta, self.phi)

    def __div__(self, other):
        try:
            division = self.length / other
        except TypeError as ex:
            print(ex)
            print("\nCan only divide vectors by scalar.")
        else:
            return Vector(division, self.theta, self.phi)

    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def is_equal_to(self, other):
        return self.length == other.length and self.theta == other.theta and self.phi == other.phi

    def to_cartesian(self):
        r = self.length
        cos_phi = math.cos(math.radians(self.phi))
        sin_phi = math.sin(math.radians(self.phi))
        cos_theta = math.cos(math.radians(self.theta))
        sin_theta = math.sin(math.radians(self.theta))
        x = r*sin_phi*cos_theta
        y = r*sin_phi*sin_theta
        z = r*cos_phi
        return [x, y, z]

    def dot(self, other):
        c_self = self.to_cartesian()
        c_other = other.to_cartesian()
        return c_self[0]*c_other[0] + \
            c_self[1]*c_other[1] + c_self[2]*c_other[2]

    def cross(self, other):
        c_self = self.to_cartesian()
        c_other = other.to_cartesian()
        cross_x = c_self[1]*c_other[2] - c_self[2]*c_other[1]
        cross_y = c_self[2]*c_other[0] - c_self[0]*c_other[2]
        cross_z = c_self[0]*c_other[1] - c_self[1]*c_other[0]
        return self.to_spherical([cross_x, cross_y, cross_z])

    def vector_angle(self, other):
        return math.degrees(math.acos(self.dot(other)/(self.length * other.length)))


vector1 = Vector(102, 91, 45)
vector2 = Vector(102, 91, 45)

print(vector1.is_equal_to(vector2))
