
from matplotlib import pyplot
import matplotlib.pyplot as plt
from classes import *
import pylab as pl
import numpy as np

def plot_sol(routes, nodos, depots, fail = None):

    for i in range(depots):
        plt.plot(nodos[i].x, nodos[i].y, 'go', linestyle='dashed', linewidth=8, markersize=12)
        pl.text(nodos[i].x+0.125,  nodos[i].y+0.125, str(nodos[i].id), color="red", fontsize=12)
    for i in nodos[depots:]:
        plt.plot(i.x, i.y, "bo")
        pl.text(i.x + 0.125, i.y + 0.125, str(i.id), color="red", fontsize=12)

    for route in routes:
        for i in range(len(route.route)-1):
            if i == 0 and route.route[i].x.id not in [j for j in range(depots)]:
               route.route[i] = edge(route.route[i].y, route.route[i].x)
            if i == len(route.route)-1 and route.route[i].y.id not in [j for j in range(depots)]:
                route.route[i] = edge(route.route[i].x, route.route[i].y)
            if route.route[i].y.id != route.route[i+1].x.id:
                route.route[i + 1] = edge(route.route[i + 1].y, route.route[i + 1].x)



    for r in routes:
        x = []
        y = []
        for e in r.route:
            x.append(e.x.x)
            y.append(e.x.y)

            x.append(e.y.x)
            y.append(e.y.y)

        plt.plot(x, y)

    text = "The distance is: "+str(sum([i.dist for i in routes]))
    for i,route in enumerate(routes):
        text += "\n" + "Route "+ str(i+1)+ ": " + route.__str__()

    if fail is not None:
        text += "\n" + "Fail: " + str(fail)

    plt.title(text, fontsize=6)
    plt.show()


def plot_boxplot(best_dist, lim = 5):
    data = [i[2] for i in best_dist[0:min([lim, len(best_dist)])]]
    fig, ax = plt.subplots()

    bp = ax.boxplot(data, patch_artist=True)

    colors = ['#0000FF', '#00FF00',
              '#FFFF00', '#FF00FF']

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for median in bp['medians']:
        median.set(color='red',
                   linewidth=3)

    ax.set_xticklabels(["Route "+str(i+1) for i in range(min([lim, len(best_dist)]))])

    plt.show()