#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Clase Camino

    Representa un camino como una lista de segmentos

Atributos:
    nombre           nombre del camino
    listaAtributos   lista de etiquetas
    listaSegmentos   lista de segmentos que conforman el camino

Métodos:
    agregarAtributo(etiqueta)

    agregarSegmento(segm)

    darCantAtributos()

    darCantSegmentos()

    *puntoEnCamino(p)

    darDistancia2D()

    darDistancia()

    darPuntoInicio()

    darPuntoFin()

    darTiempoTotal()

    darVelocidadPromedio()
        return self.darDistancia() / self.darTiempoTotal()

    def darVelocidadPromedio2D(self):
        return self.darDistancia2D() / self.darTiempoTotal()

Todo:
    * agregar excepciones
    * puntoEnCamino(p)


"""


class Camino:
    def __init__(self, nomb):
        """
        Constructor
        :param nomb: nombre del camino
        """
        self.nombre = nomb
        self.listaSegmentos = []
        self.listaAtributos = []

    def agregarAtributo(self, etiqueta):
        """
        :param etiqueta: etiqueda para agregar a la lista de atributos
        :return: devuelve la cantidad de atributos en lista
        """
        self.listaAtributos.append(etiqueta)
        return len(self.listaAtributos)

    def agregarSegmento(self, segm):
        """
        :param segm: agrega un segmento al camino
        :return: devuelve la cantidad de segmentos en lista
        """
        self.listaSegmentos.append(segm)
        return len(self.listaSegmentos)

    def darCantAtributos(self):
        """
        :return: devuelve cantidad de atributos
        """
        return len(self.listaAtributos)

    def darCantSegmentos(self):
        """
        :return: devuelve cantidad de segmentos
        """
        return len(self.listaSegmentos)

    def puntoEnCamino(self, p):
        """
        :param p:
        :return:    devuelve true o false segun el punto p
                    se encuentra en el camino
        """
        pass

    def darDistancia2D(self):
        """
        :return: devuelve el largo del camino en plan XY
        """
        return (sum(s.darDistancia2D() for s in self.listaSegmentos))

    def darDistancia(self):
        """
        :return:  devuelve el largo del camino
        """
        return (sum(s.darDistancia() for s in self.listaSegmentos))

    def darPuntoInicio(self):
        """
        :return: devuelve el punto inicial
        """
        return self.listaSegmentos[0].puntoInicial

    def darPuntoFin(self):
        """
        :return: devuelve el punto final
        """
        return self.listaSegmentos[self.darCantSegmentos()].puntoFinal

    def darTiempoTotal(self):
        """
        :return: devuelve el tiempo total empleado en el camino
        """
        return sum(s.darTiempo() for s in self.listaSegmentos)

    def darVelocidadPromedio(self):
        """
        :return: devuelve la velocidad promedio
        """
        return self.darDistancia() / self.darTiempoTotal()

    def darVelocidadPromedio2D(self):
        """
        :return: devuelve la velocidad promedio considerando distancias en XY
        """
        return self.darDistancia2D() / self.darTiempoTotal()


def main(args):
    pass


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))