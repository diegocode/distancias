#ifndef CAMINOS_H_INCLUDED
#define CAMINOS_H_INCLUDED

/*
  Representa un punto en el espacio (x, y, z)
  con marca temporal t
*/
typedef struct punto {
    double x;
    double y;
    double z;
    long t;
} Punto;


/*
  Representa un segmento mediante
  Punto p0: punto inicial
  Punto p1: punto final
*/
typedef struct segmento {
    Punto p0;
    Punto p1;
} Segmento;


/*
  Representa un camino mediante un vector de segmentos
  (30 segmentos como máximo)
*/
typedef struct caminos {
    Segmento camino[30];
    char     nombre[30];
    int      cant_segmentos;
} Camino;


/*
  Usado para devolución de darCaminoMasCorto()
*/
typedef struct corto {
    int     numCamino;
    double  valor;
} Corto;

#endif // CAMINOS_H_INCLUDED

void crearPunto(Punto *p, double x, double y, double z, long t);
void mostrarPunto(Punto p);
void crearSegmento(Segmento *s, Punto p0, Punto p1);
void mostrarSegmento(Segmento s);
double darDistanciaSegmento(Segmento s);
int agregarSegmento(Camino *m, Segmento s);
void mostrarCamino(Camino m);
double darDistanciaCamino(Camino m);
void darCaminoMasCorto(Camino *mps, int cant, Corto *corto);
