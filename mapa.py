#!/usr/bin/env python
# -*- coding: utf-8 -*-

import camino, punto, segmento


class Mapa:
    def __init__(self, nomb):
        self.nombre = ""
        self.listaCaminos = []

    def darCaminoMenorDistancia(self):
        lista_aux = ((c.darDistancia(), c.nombre) for c in self.listaCaminos)
        return min(lista_aux, key=lambda x: x[0])

    def darCaminoMenorTiempo(self):
        lista_aux = ((c.darTiempoTotal(), c.nombre) for c in self.listaCaminos)
        return min(lista_aux, key=lambda x: x[0])

def main(args):
    c = camino.Camino("prueba")

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

    print(c.darDistancia())

    m = Mapa("general")
    m.listaCaminos.append(c)

    p0 = punto.Punto(0, 0, 0, 0)
    p1 = punto.Punto(0, 10, 0, 3)
    p3 = punto.Punto(10, 0, 0, 18)
    p4 = punto.Punto(10, 0, 10, 22)

    s1 = segmento.Segmento(p0, p1)
    s2 = segmento.Segmento(p1, p3)
    s4 = segmento.Segmento(p3, p4)

    c = camino.Camino("dos")

    c.agregarSegmento(s1)
    c.agregarSegmento(s2)
    c.agregarSegmento(s4)

    print(c.darDistancia())

    m.listaCaminos.append(c)

    print(list(m.darCaminoMenorDistancia()))
    print(list(m.darCaminoMenorTiempo()))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))