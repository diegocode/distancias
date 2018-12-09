#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Clase Punto

    Representa una posición en el espacio. Incluye también información temporal.

Atributos:
    x       componente x de coordenadas
    y       componente y de coordenadas
    z       componente z de coordenadas
    t       marca temporal
    nombre  nombre del punto (default "")

Métodos:
    Punto(x, y, z, t)   constructor
    getNombre           devuelve el nombre del Punto
    setNombre(nombre)   fija el nombre del punto

Todo:
    * agregar excepciones

"""


class Punto:

    def __init__(self, x = 0.0, y = 0.0, z = 0.0, t = 0):
        """
        constructor

         recibe valores x, y, z del punto y la información temporal

        :param x:
        :param y:
        :param z:
        :param t:
        """
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        self.nombre = ""

    def setNombre(self, n):
        """
        Fija el nombre del punto

        :param n:  nombre
        """
        self.nombre = n

    def getombre(self):
        """
        Devuelve el nombre del punto

        :return:  nombre del punto
        """
        return self.nombre


def main(args):
    pass


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))