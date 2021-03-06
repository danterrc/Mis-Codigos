#! /usr/bin/python
# coding: utf-8

from punto import Punto
from vector import  Vector
import math

class Vectores(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.a = self.v1.p2.x - self.v1.p1.x
        self.b = self.v1.p2.y - self.v1.p1.y
        self.c = self.v2.p2.x - self.v2.p1.x
        self.d = self.v2.p2.y - self.v2.p1.y

    def Sumar(self):
        if self.v1.p2.x == self.v2.p1.x and self.v1.p2.y == self.v2.p1.y or self.v1.p1.x == self.v2.p1.x and self.v1.p1.y == self.v2.p1.y or self.v1.p1.x == self.v2.p2.x and self.v1.p1.y == self.v2.p2.y:
            su = self.v1.Distancia() + self.v2.Distancia()
            return "El resultado de la suma es: %i" % su

    def Restar(self):
        if self.v1.p2.x == self.v2.p1.x and self.v1.p2.y == self.v2.p1.y or self.v1.p1.x == self.v2.p1.x and self.v1.p1.y == self.v2.p1.y or self.v1.p1.x == self.v2.p2.x and self.v1.p1.y == self.v2.p2.y:
            res = self.v1.Distancia() - self.v2.Distancia()
            return "El resultado de la resta es: %i" % res
    def Angulo(self):
        if self.v1.p1.x == self.v2.p1.x and self.v1.p1.y == self.v2.p1.y:
            res = (self.a * self.c + self.b * self.d) / (math.sqrt(self.a**2 + self.b**2)* math.sqrt(self.c**2 + self.d**2))
            d = math.acos(res)
            r = math.degrees(d)
            return "El angulo es: %i" % r
