#!/usr/bin/env python
# -*- coding: utf-8 -*-

import punto, segmento

class Camino:
    def __init__(self, nomb):
        self.nombre = nomb
        self.listaSegmentos = []
        self.listaAtributos = []

    def agregarAtributo(self, etiqueta):
        self.listaAtributos.append(etiqueta)
        return len(self.listaAtributos)

    def agregarSegmento(self, segm):
        self.listaSegmentos.append(segm)
        return len(self.listaSegmentos)

    def darCantAtributos(self):
        return len(self.listaAtributos)

    def darCantSegmentos(self):
        return len(self.listaSegmentos)

    def puntoEnCamino(self, p):
        pass

    def darDistancia2D(self):
        pass

    def darDistancia(self):
        pass

    def darTiempoTotal(self):
        pass

    def darPuntoInicio(self):
        return self.listaSegmentos[0].puntoInicial

    def darPuntoFin(self):
        return self.listaSegmentos[self.darCantSegmentos()].puntoFinal

    def darTiempoTotal(self):
        return sum(s.darTiempo() for s in self.listaSegmentos)

    def darVelocidadPromedio(self):
        pass


def main(args):
    c = Camino("prueba")

    p0 = punto.Punto(0, 0, 0, 0)
    p1 = punto.Punto(0, 10, 0, 3)
    p2 = punto.Punto(0, 5, 0, 5)

    s1 = segmento.Segmento(p0, p1)
    s2 = segmento.Segmento(p1, p2)

    c.agregarSegmento(s1)
    c.agregarSegmento(s2)

    print(c.darTiempoTotal())
    print(c.darCantSegmentos())

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))