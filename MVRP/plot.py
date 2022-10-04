
from matplotlib import pyplot
import matplotlib.pyplot as plt
from classes import *
import pylab as pl

def plot_sol(routes, nodos, depots):

    for i in range(depots):
        plt.plot(nodos[i].x, nodos[i].y, 'go', linestyle='dashed', linewidth=8, markersize=12)
        pl.text(nodos[i].x+0.125,  nodos[i].y+0.125, str( nodos[i].id), color="red", fontsize=12)
    for i in nodos[depots:]:
        plt.plot(i.x, i.y, "bo")
        pl.text(i.x + 0.125, i.y + 0.125, str(i.id), color="red", fontsize=12)

    for route in routes:
        for i in range(len(route.route)-1):
            if i == 0 and route.route[i].x.id not in [i for i in range(depots)]:
               route.route[i] = edge(route.route[i].y, route.route[i].x)
            if i == len(route.route)-1 and route.route[i].y.id not in [i for i in range(depots)]:
                route.route[i] = edge(route.route[i].x, route.route[i].y)
            if route.route[i].y.id != route.route[i+1].x.id:
                route.route[i + 1] = edge(route.route[i + 1].y, route.route[i + 1].x)


    x = []
    y = []
    for r in routes:
        for e in r.route:
            x.append(e.x.x)
            y.append(e.x.y)

            x.append(e.y.x)
            y.append(e.y.y)

    plt.plot(x, y)
    text = "The distance is: "+str(sum([i.dist for i in routes]))
    for i,route in enumerate(routes):
        text += "\n" + "Route "+ str(i+1)+ ": " + route.__str__()
    plt.title(text, fontsize=8)
    plt.show()