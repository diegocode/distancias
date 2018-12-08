#!/usr/bin/env python
# -*- coding: utf-8 -*-

import punto

class Segmento:
    def __init__(self, p0, p1):
        self.puntoInicial = p0
        self.puntoFinal = p1

    def darDistancia2D(self):
        return self.puntoFinal.x - self.puntoInicial.x

    def darDistancia(self):
        return self.puntoFinal.x - self.puntoInicial.x

    def darTiempo(self):
        return self.puntoFinal.t - self.puntoInicial.t

def main(args):
    pa = punto.Punto()
    pb = punto.Punto(10, 0, 0, 3)
    s = Segmento(pa, pb)

    print(s.darDistancia2D())
    print(s.darDistancia())
    print(s.darTiempo())

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))