import punto, segmento, camino, mapa

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

m = mapa.Mapa("general")
c = camino.Camino("prueba")

p0 = punto.Punto(10, 20, 0, 0)
p1 = punto.Punto(40, 30, 5, 3)
p2 = punto.Punto(70, 30, 7, 5)
p3 = punto.Punto(90, 20, 8, 9)
p4 = punto.Punto(110, 10, 6, 14)
p5 = punto.Punto(150, 40, 10, 20)
p6 = punto.Punto(190, 30, 13, 25)
p7 = punto.Punto(230, 36, 9, 31)

s1 = segmento.Segmento(p0, p1)
s2 = segmento.Segmento(p1, p2)
s3 = segmento.Segmento(p2, p3)
s4 = segmento.Segmento(p3, p4)
s5 = segmento.Segmento(p4, p5)
s6 = segmento.Segmento(p5, p6)
s7 = segmento.Segmento(p6, p7)

c.agregarSegmento(s1)
c.agregarSegmento(s2)
c.agregarSegmento(s3)
c.agregarSegmento(s4)
c.agregarSegmento(s5)
c.agregarSegmento(s6)
c.agregarSegmento(s7)

print(c.darDistancia())

m.listaCaminos.append(c)

c = camino.Camino("dos")

p0 = punto.Punto(10, 20, 0, 0)
p3 = punto.Punto(90, 20, 0, 10)
p5 = punto.Punto(150, 40, 0, 22)
p7 = punto.Punto(230, 36, 9, 39)

s1 = segmento.Segmento(p0, p3)
s2 = segmento.Segmento(p3, p5)
s3 = segmento.Segmento(p5, p7)

c.agregarSegmento(s1)
c.agregarSegmento(s2)
c.agregarSegmento(s3)

print(c.darDistancia())

m.listaCaminos.append(c)

print(m.darCaminoMenorDistancia())
print(m.darCaminoMenorTiempo())


fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

for c in m.listaCaminos:
    ciX = []
    ciY = []
    ciZ = []

    ciX.append(c.listaSegmentos[0].puntoInicial.x)
    ciY.append(c.listaSegmentos[0].puntoInicial.y)
    ciZ.append(c.listaSegmentos[0].puntoInicial.z)

    for s in c.listaSegmentos:
        ciX.append(s.puntoFinal.x)
        ciY.append(s.puntoFinal.y)
        ciZ.append(s.puntoFinal.z)
        #print("%f - %f - %f" % (s.puntoInicial.x, s.puntoInicial.y, s.puntoInicial.z))

    ax.plot(ciX, ciY, zs=ciZ, label='toto')

plt.show()