# coding: utf-8
#! /usr/bin/python

import os
os.system('clear')

class Punto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setxy(self, nx, ny):
        self.x = nx
        self.y = ny
    def setx(self, nx):
        self.x = nx
    def sety(self, ny):
        self.y = ny
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getxy(self):
        return "x,y: %i,%i" % (self.x,self.y)
    def impri(self):
        return "Punto: (%i,%i)" % (self.x, self.y)
