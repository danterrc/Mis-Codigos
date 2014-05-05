#! /usr/bin/python
# coding: utf-8
from punto import Punto
from vector import Vector
from programa import Vectores
import os
os.system('clear')
import math

lista_vector = []
list_vect = []
def vec(cant):
    for i in range(cant):
        x1 = input("Ingrese x%s: " % i)
        y1 = input("Ingrese y%s: " % i)
        x2 = input("Ingrese x%s: " % (i+1))
        y2 = input("Ingrese y%s: " % (i+1))
        p1 = (x1,y1)
        p2 = (x2,y2)
        v = (p1,p2)
        list_vect.append(v)
        print "--------------"
cant = input("Ingrese cuantos vectores deseas: ")
if cant == 0 or cant == 1:
    print "Por favor ingrese un valor mayor igual de 2."
    cant = input("Ingrese cuantos vectores deseas: ")

vec(cant)

os.system('clear')
while True:
    print"""MENÚ DE OPCIONES
    1: Imprimir  Lista de vectores
    2: Operaciones Algebraicas con vectores
    3: Salir
    """
    op = input("Ingrese una opción: ")
    if op == 3:
        break
    if op == 1:
        os.system('clear')
        print list_vect

    if op == 2:
        os.system('clear')
        while True:
            print "MENU DE OPERACIONES"
            for i in range(len(list_vect)):
               print "Vector %d" % int(i+1)
               print list_vect[i]
               print"--------"
            print """¿Que desea hacer?
            1: Sumar vectores
            2: Restar vectores
            3: Ángulo del vector
            4: Salir"""
            print "Selecionar 2 vectores para operar"
            sel = input("Ingrese el que vector desea operar:  ")
            sel1 = input("Ingrese el siguiente vector: ")
            p1 = Punto(list_vect[sel-1][0][0], list_vect[sel-1][0][1])
            p2 = Punto(list_vect[sel-1][1][0], list_vect[sel-1][1][1])
            p3 = Punto(list_vect[sel1-1][0][0], list_vect[sel1-1][0][1])
            p4 = Punto(list_vect[sel1-1][1][0], list_vect[sel1-1][1][1])
            v1 = Vector(p1,p2)
            v2 = Vector(p3,p4)
            f = Vectores(v1,v2)
            op = input("Ingrese una opcion: ")
            if op == 4:
                break
            if op == 0 or op > 4:
                print"ERROR, este número no existe"
                break
            elif op == 1:
                os.system('clear')
                print f.Sumar()
                print "---------------"
            elif op == 2:
                os.system('clear')
                print f.Restar()
                print "---------------"
            elif op == 3:
                os.system('clear')
                print f.Angulo()
                print "---------------"
