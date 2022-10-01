
from matplotlib import pyplot
import matplotlib.pyplot as plt
from classes import *

def plot_sol(routes, nodos, depots):

    for i in range(depots):
        plt.plot(nodos[i].x, nodos[i].y, 'go', linestyle='dashed', linewidth=8, markersize=12)
    for i in nodos[depots:]:
        plt.plot(i.x, i.y, "bo")

    for route in routes:
        for i in range(len(route.route)-1):
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
    plt.title("The distance is: "+str(sum([i.dist for i in routes])))
    plt.show()