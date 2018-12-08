#!/usr/bin/env python
# -*- coding: utf-8 -*-

import punto
import math

class Segmento:
    def __init__(self, p0, p1):
        self.puntoInicial = p0
        self.puntoFinal = p1

    def darDistancia2D(self):
        return math.sqrt((self.puntoFinal.x - self.puntoInicial.x) ** 2 \
                         + (self.puntoFinal.y - self.puntoInicial.y) ** 2)

    def darDistancia(self):
        return math.sqrt(  (self.puntoFinal.x - self.puntoInicial.x) ** 2 \
                         + (self.puntoFinal.y - self.puntoInicial.y) ** 2 \
                         + (self.puntoFinal.z - self.puntoInicial.z) ** 2)

    def darTiempo(self):
        return self.puntoFinal.t - self.puntoInicial.t

def main(args):
    pa = punto.Punto(2, 3, 1, 0)
    pb = punto.Punto(8, -5, 0, 3)
    s = Segmento(pa, pb)

    print(s.darDistancia2D())
    print(s.darDistancia())
    print(s.darTiempo())

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))