
from matplotlib import pyplot
import matplotlib.pyplot as plt
from classes import *
import pylab as pl

def plot_sol(routes, nodos):

    for i in range(1):
        plt.plot(nodos[i].x, nodos[i].y, 'go', linestyle='dashed', linewidth=8, markersize=12)
        pl.text(nodos[i].x+0.125,  nodos[i].y+0.125, str( nodos[i].id), color="red", fontsize=12)
    for i in nodos[1:]:
        plt.plot(i.x, i.y, "bo")
        pl.text(i.x + 0.125, i.y + 0.125, str(i.id), color="red", fontsize=12)

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


def plot_boxplot(best_dist, lim = 5):
    import matplotlib.pyplot as plt
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