#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
    pass


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))