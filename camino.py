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
        return (sum(s.darDistancia2D() for s in self.listaSegmentos))

    def darDistancia(self):
        return (sum(s.darDistancia() for s in self.listaSegmentos))

    def darPuntoInicio(self):
        return self.listaSegmentos[0].puntoInicial

    def darPuntoFin(self):
        return self.listaSegmentos[self.darCantSegmentos()].puntoFinal

    def darTiempoTotal(self):
        return sum(s.darTiempo() for s in self.listaSegmentos)

    def darVelocidadPromedio(self):
        return self.darDistancia() / self.darTiempoTotal()

    def darVelocidadPromedio2D(self):
        return self.darDistancia2D() / self.darTiempoTotal()

def main(args):
    c = Camino("prueba")

    p0 = punto.Punto(0, 0, 0, 0)
    p1 = punto.Punto(0, 10, 0, 3)
    p2 = punto.Punto(10, 10, 0, 5)
    p3 = punto.Punto(10, 0, 0, 9)
    p4 = punto.Punto(10, 0, 10, 14)

    s1 = segmento.Segmento(p0, p1)
    s2 = segmento.Segmento(p1, p2)
    s3 = segmento.Segmento(p2, p3)
    s4 = segmento.Segmento(p3, p4)

    c.agregarSegmento(s1)
    c.agregarSegmento(s2)
    c.agregarSegmento(s3)
    c.agregarSegmento(s4)

    print(c.darTiempoTotal())
    print(c.darCantSegmentos())
    print(c.darDistancia())
    print(c.darDistancia2D())
    print(c.darVelocidadPromedio())
    print(c.darVelocidadPromedio2D())


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))