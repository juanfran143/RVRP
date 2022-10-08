

from classes import *
from solution import *
from plot import *
from simheuristic import Simheuristic
import random

if __name__ == '__main__':
    nodes = [node(0, 1, 1, 0), node(1, 6, 4, 0),
             node(2, 3, 3, 1), node(3, 3, 5, 1),
             node(4, 0, 1, 1), node(5, -1, -2, 1),
             node(6, -2, -1, 1)]

    random.seed(123)
    nodes = [node(i+1, random.randint(-10, 10), random.randint(-10, 10), random.randint(1, 4)) for i in range(1, 20)]
    nodes.insert(0, node(0, 0, 0, 0))
    nodes.insert(1, node(1, 5, 5, 0))

    sol = algorithm(nodes, n_depots=2)
    # sol.algo()
    sim_long = Simheuristic(1000, var_distance = 0.1, var_demand=0.1)
    sim_short = Simheuristic(100, var_distance = 0.1, var_demand=0.1)
    sol = algorithm(nodes, n_depots = 2)
    # sol.algo()

    sol.multistart_algo(180, sim_short, sim_long)




