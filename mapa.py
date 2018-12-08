#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Mapa:
    def __init__(self, nomb):
        self.nombre = nomb
        self.listaCaminos = []

    def darCaminoMenorDistancia(self):
        lista_aux = ((c.darDistancia(), c.nombre) for c in self.listaCaminos)
        return min(lista_aux, key=lambda x: x[0])

    def darCaminoMenorTiempo(self):
        lista_aux = ((c.darTiempoTotal(), c.nombre) for c in self.listaCaminos)
        return min(lista_aux, key=lambda x: x[0])


def main(args):
    pass


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))