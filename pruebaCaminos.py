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


# fig = plt.figure()
#
# VecStart_x = [0, 1, 3, 5]
# VecStart_y = [2, 2, 5, 5]
# VecStart_z = [1, 1, 1, 5]
# VecEnd_x = [1, 2, -1, 6]
# VecEnd_y = [3, 1, -2, 7]
# VecEnd_z = [1, 0, 4, 9]
#
# ax = fig.add_subplot(111, projection='3d')
#
# ax.plot(, [0,0], [1, 2], zs=[0, 4], label='toto')
#
# plt.show()
# Axes3D.plot()