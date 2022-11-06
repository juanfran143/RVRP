
import matplotlib.pyplot as plt
from classes import *
import pylab as pl
import numpy as np

def add_arrow(line, position=None, direction='right', size=15, color=None):
    """
    add an arrow to a line.

    line:       Line2D object
    position:   x-position of the arrow. If None, mean of xdata is taken
    direction:  'left' or 'right'
    size:       size of the arrow in fontsize points
    color:      if None, line color is taken.
    """
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if position is None:
        position = xdata.mean()
    # find closest index
    start_ind = np.argmin(np.absolute(xdata - position))
    if direction == 'right':
        end_ind = start_ind + 1
    else:
        end_ind = start_ind - 1

    line.axes.annotate('',
        xytext=(xdata[start_ind], ydata[start_ind]),
        xy=(xdata[end_ind], ydata[end_ind]),
        arrowprops=dict(arrowstyle="->", color=color),
        size=size
    )

def plot_sol(routes, nodos):

    for i in range(1):
        plt.plot(nodos[i].x, nodos[i].y, 'go', linestyle='dashed', linewidth=8, markersize=12)
        pl.text(nodos[i].x+0.125,  nodos[i].y+0.125, str( nodos[i].id), color="red", fontsize=12)
    for i in nodos[1:]:
        plt.plot(i.x, i.y, "bo")
        pl.text(i.x + 0.125, i.y + 0.125, str(i.id), color="red", fontsize=12)

    for i in nodos[1:]:
        plt.plot(i.x, i.y, "bo")
        text = "["+str(i.min_interval)+ ","+ str(i.max_interval)+"]"
        pl.text(i.x-0.25, i.y - 0.35, text, color="green", fontsize=8)

    for r in routes:
        for e in r.route:
            x = []
            y = []
            x.append(e.x.x)
            y.append(e.x.y)

            x.append(e.y.x)
            y.append(e.y.y)

            line = plt.plot(x, y)[0]
            add_arrow(line)


    text = "The distance is: "+str(sum([i.dist for i in routes]))
    for i,route in enumerate(routes):
        text += "\n" + "Route "+ str(i+1)+ ": " + route.__str__()
    plt.title(text, fontsize=8)
    plt.show()