import matplotlib.pyplot as plt
from ponto import *
from bresenham import *
from ponto_medio import *
from curvas import *
from t_basicas import *
from preenchimento import *
from recorte import *


"""
#chamada pro recorte de linha
#obs: mudar limite plt.axis no Arquivo Bresenham
CS_Clip(Point(1,1),Point(50,60), 2,40,3,50)
drawLine(Point(1,1),Point(50,60))
"""

"""
#PREENCHIMENTO RECURSIVO
poligono = [[0,10], [20,15], [10,25], [30,35],[65,15],[65,0],[50,15],[40,0]]
#PONTO INICIAL  = Point(30,17)

#poligono = [[1,1],[1,10],[11,10],[11,1]]
#desenhar as bordas
s = drawPolygon(poligono)
show(s)
#preenchendo o poligono
FloodFill(Point(30,17), s)
s.extend(fill)

#exibindo o poligono preenchido
for i in range(0, len(s)):
   plt.plot([s[i].x], [s[i].y], 'rs')

plt.axis([0,70,0,70])
plt.show()
"""




"""
# chamada para o bresenham
p1 = Point(0, 3)
p2 = Point(10, 10)
drawLine(p1,p2)
"""



"""
#chamada para o ponto médio
raio = 50
drawcircle(raio)
"""


"""
#chamada pra bezier
curve2 = g((0, 0), (5, 10), (10, 15),(20,0))

t = 0
lista = []
for i in range(0, 200):
    lista.append(list(curve2(t)))
    t += 0.01


for i in range(0, len(lista)):
	plt.plot( [lista[i][0]], [lista[i][1]], 'ro')

plt.axis([0,25,0,25])
plt.grid(1)
plt.show()
"""


#chamada para transformações basicas


#lista = [[2, 4], [2, 5], [2, 6], [2, 6], [3, 6], [4, 5], [4, 5], [5, 6], [6, 6], [7, 7], [7, 5], \
            #  [7, 6], [7, 7], [2, 4], [3, 3], [4, 2], [4, 2], [5, 3], [6, 4], [7, 5]]
#pivot(4,2)
#escala(lista, [3, 3])

#translacao(lista, [-3,-6])

#lista =[[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[2,2],[2,3],[2,4],[2,5],[2,6],[2,6],[3,7],[3,8],[4,9],[5,10],[5,10],[6,9],[7,8],\
#[7,7],[8,6],[8,6],[8,5],[8,4],[8,3],[8,2]]
#pivot(2,2)

rotacao(lista, 90, [4,2])

