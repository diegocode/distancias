#!/usr/bin/env python
# -*- coding: utf-8 -*-

import punto
import math


""" 
    Clase Segmento

    Representa una segmento dados 2 puntos en el espacio

Atributos:
    p0       punto inicial del segmento
    p1       punto final del segmento
    nombre   nombre del segmento (default "")

Métodos:
    darDistancia2D  devuelve el largo del segmento 
                    sin importar componente Z
                     
    darDistancia    devuelve el largo del segmento  

    darTiempo       devuelve el tiempo necesario 
                    para recorrer el segmento
                    
    *darInclinacion  devuelve inclinación vertical

Todo:
    * agregar excepciones
    * darInclinacion

"""

class Segmento:
    """
    Constructor

    Recibe dos puntos (Clase Punto en punto.py)

    """
    def __init__(self, p0, p1):
        """

        :param p0:  punto de inicio
        :param p1:  punto de fin
        """
        self.puntoInicial = p0
        self.puntoFinal = p1
        self.nombre = ""

    def darDistancia2D(self):
        """
        :return:  devuelve el largo del segmento considerando
                  solo el plano XY
        """
        return math.sqrt((self.puntoFinal.x - self.puntoInicial.x) ** 2 \
                         + (self.puntoFinal.y - self.puntoInicial.y) ** 2)

    def darDistancia(self):
        """
        :return:    devuelve el largo del segmento
        """
        return math.sqrt(  (self.puntoFinal.x - self.puntoInicial.x) ** 2 \
                         + (self.puntoFinal.y - self.puntoInicial.y) ** 2 \
                         + (self.puntoFinal.z - self.puntoInicial.z) ** 2)

    def darTiempo(self):
        """
        :return:    devuelve el tiempo empleado para recorrer el segmento
        """
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