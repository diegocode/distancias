import punto, segmento, camino, mapa

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

m = mapa.Mapa("general")
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