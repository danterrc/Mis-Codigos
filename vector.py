#! /usr/bin/python
# coding: utf-8
from punto import Punto
import math
class Vector(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def Distancia(self):
        # d = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
        d = (((self.p2.getx() - self.p1.getx())**2) + ((self.p2.gety() - self.p1.gety())**2)) ** 0.5
        return d
    def Pendiente(self):
        p = (self.p2.gety() - self.p1.getx()) / (self.p2.getx() - self.p1.getx())
        return p
    def Datos_angulo(self):
        a = self.p2.x - self.p1.x
        b = self.p2.y - self.p1.y
        c = (a,b)
        return c
