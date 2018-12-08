import punto, segmento, camino

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

print(c.darTiempoTotal())
print(c.darCantSegmentos())
print(c.darDistancia())
print(c.darDistancia2D())
print(c.darVelocidadPromedio())
print(c.darVelocidadPromedio2D())


fig = plt.figure()

VecStart_x = [0, 1, 3, 5]
VecStart_y = [2, 2, 5, 5]
VecStart_z = [1, 1, 1, 5]
VecEnd_x = [1, 2, -1, 6]
VecEnd_y = [3, 1, -2, 7]
VecEnd_z = [1, 0, 4, 9]

ax = fig.add_subplot(111, projection='3d')

ax.plot(, [0,0], [1, 2], zs=[0, 4], label='toto')

#ax.plot([0,1], [2,3], zs=[1,1])

plt.show()
Axes3D.plot()