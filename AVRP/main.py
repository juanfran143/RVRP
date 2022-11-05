

from classes import *
from solution import *
from plot import *


if __name__ == '__main__':
    streets = ["calle conde de peñalver 16", "calle alcalá 111", "calle granvia 15", "calle lavapies 77",
               "calle sombrerería 18"]
    demands = [0, 1, 1, 1, 1]
    nodes = []
    i = 0
    for s, d in zip(streets, demands):
        nodes.append(node(i, street=s, demand=d))
        i += 1
    """    
    nodes = [node(0, 1, 1, 0), node(1, 2.5, 2, 1),
             node(2, 3, 3, 1), node(3, 3, 5, 1),
             node(4, 0, 1, 1), node(5, -1, -2, 1),
             node(6, -2, -1, 1)]"""

    sol = algorithm(nodes)
    # sol.algo()

    sol.multistart_algo(20)



