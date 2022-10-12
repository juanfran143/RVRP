

from classes import *
from solution import *
from plot import *

if __name__ == '__main__':
    nodes = [node(0, 1, 1, 0, 0, 24), node(1, 2.5, 2, 1, 9, 11),
             node(2, 3, 3, 1, 9, 12), node(3, 3, 5, 1, 10, 15),
             node(4, 0, 1, 1, 12, 18), node(5, -1, -2, 1, 14, 18),
             node(6, -2, -1, 1, 9, 18)]

    sol = algorithm(nodes)
    # sol.algo()

    sol.multistart_algo(20)



