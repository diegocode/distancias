#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "caminos.h"

int cant_mapas = 0;
Camino mapa[20];

int main()
{
    Punto p0, p1, p2, p3, p4;
    Segmento s1, s2, s3, s4;
    Corto resu;

    crearPunto(&p0, 0, 0, 0, 0);
    crearPunto(&p1, 0, 10, 0, 3);
    crearPunto(&p2, 10, 10, 0, 5);
    crearPunto(&p3, 10, 0, 0, 16);
    crearPunto(&p4, 10, 0, 10, 22);

    crearSegmento(&s1, p0, p1);
    crearSegmento(&s2, p1, p2);
    crearSegmento(&s3, p2, p3);
    crearSegmento(&s4, p3, p4);

    agregarSegmento(&mapa[0], s1);
    agregarSegmento(&mapa[0], s2);
    agregarSegmento(&mapa[0], s3);
    agregarSegmento(&mapa[0], s4);

    cant_mapas++;

    crearSegmento(&s1, p0, p1);
    crearSegmento(&s2, p1, p3);
    crearSegmento(&s3, p3, p4);

    agregarSegmento(&mapa[1], s1);
    agregarSegmento(&mapa[1], s2);
    agregarSegmento(&mapa[1], s3);

    cant_mapas++;

    for(int i = 0; i < cant_mapas; i++) {
            puts("--------------------------------------------------");

            mostrarCamino(mapa[i]);
            printf("largo: %.3f\n", darDistanciaCamino(mapa[i]));
    }

    darCaminoMasCorto(mapa, cant_mapas, &resu);
    printf("Camino corto: # %d - largo: %.3f\n", resu.numCamino, resu.valor);

    return 0;
}
