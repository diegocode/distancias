#include <math.h>
#include "caminos.h"

/*
  Asigna valores a los componentes x, y, z del punto p
*/
void crearPunto(Punto *p, double x, double y, double z, long t) {
    p->x = x;
    p->y = y;
    p->z = z;
    p->t = t;
}

/*
    muestra componentes del punto p
*/
void mostrarPunto(Punto p){
    printf("(%.3f, %.3f, %.3f) -- t: %d\n", p.x, p.y, p.z, p.t);
}

/*
    asiggna valores a los componentes del segmento s
    p0 es el punto inicial (tipo Punto)
    p1 es el punto final  (tipo Punto)
*/
void crearSegmento(Segmento *s, Punto p0, Punto p1){
    s->p0 = p0;
    s->p1 = p1;
}

/*
    muestra inicio y fin del segmento s
*/
void mostrarSegmento(Segmento s){
    printf("(%.3f, %.3f, %.3f) ---> (%.3f, %.3f, %.3f)\n", s.p0.x, s.p0.y, s.p0.z, s.p1.x, s.p1.y, s.p1.z);
}

/*
    devuelve la longitud del segmento s
*/
double darDistanciaSegmento(Segmento s){
    double dX, dY, dZ;

    dX = s.p1.x - s.p0.x;
    dY = s.p1.y - s.p0.y;
    dZ = s.p1.z - s.p0.z;

    return sqrt(dX * dX + dY * dY + dZ * dZ);
}

/*
    agrega el segmento s al camino m
    incrementa el contador de segmentos del camino
*/
int agregarSegmento(Camino *m, Segmento s){
    m->camino[m->cant_segmentos] = s;
    (m->cant_segmentos)++;
    return m->cant_segmentos;
}

/*
    muestra el camino m
*/
void mostrarCamino(Camino m) {
    for (int i = 0; i < m.cant_segmentos; i++){
        mostrarSegmento(m.camino[i]);
    }
}

/*
    devuelve el largo total del camino m
*/
double darDistanciaCamino(Camino m) {
    double largo = 0;
    for (int i = 0; i < m.cant_segmentos; i++){
        largo += darDistanciaSegmento(m.camino[i]);
    }
    return largo;
}

/*
    devuelve una estructura tipo Corto con
    el número y el largo del camino más corto de un
    vector mps con Caminos
*/
void darCaminoMasCorto(Camino *mps, int cant, Corto *corto){
    double aux, largoMin = darDistanciaCamino(*mps);
    int numCaminoCorto = 0;

    for(int i = 1; i < cant; i++){
        aux = darDistanciaCamino(*(mps + i));
        if (aux < largoMin) {
            largoMin = aux;
            numCaminoCorto = i;
        }
    }

    corto->numCamino = numCaminoCorto;
    corto->valor = largoMin;
}
