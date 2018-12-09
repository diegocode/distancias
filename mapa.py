#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Clase Mapa

    Representa un conjunto de caminos

Atributos:
    nombre           nombre del mapa
    listaCaminos     lista de caminos

Métodos:
    darCaminoMenorDistancia()     devuelve el camino más corto
    darCaminoMenorTiempo()        devuelve el camino más rápido

Todo:
    * agregar excepciones

"""

class Mapa:
    def __init__(self, nomb):
        """
        Constructor
        :param nomb:  nombre del mapa
        """
        self.nombre = nomb
        self.listaCaminos = []

    def darCaminoMenorDistancia(self):
        """
        devuelve el camino más corto
        :return: tupla (distancia, nombre de camino)
        """
        lista_aux = ((c.darDistancia(), c.nombre) for c in self.listaCaminos)
        return min(lista_aux, key=lambda x: x[0])

    def darCaminoMenorTiempo(self):
        """
        devuelve el camino más rápido
        :return: tupla (tiempo, nombre de camino)
        """
        lista_aux = ((c.darTiempoTotal(), c.nombre) for c in self.listaCaminos)
        return min(lista_aux, key=lambda x: x[0])


def main(args):
    pass


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))