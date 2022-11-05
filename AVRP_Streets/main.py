

from classes import *
from solution import *
from plot import *
from get_problem import main

if __name__ == '__main__':
    streets = ["calle conde de peñalver 16", "calle alcalá 111", "calle granvia 15", "calle lavapies 77",
               "calle sombrerería 18"]

    streets = ["Calle lorenzo palmireño 14", "Calle manuel Candela 27", "Calle Xátiva 22 Valencia", "Calle Colón 12 Valencia",
               "Estación del Nord"]

    demands = [0, 1, 1, 1, 1]
    nodes = []
    edges = []
    i = 0
    for s, d in zip(streets, demands):
        nodes.append(node(i, street=s, demand=d))
        i += 1

    for i in nodes:
        for j in nodes:
            if i == j:
                continue
            edges.append(edge(i, j, by="walking"))

    sol = algorithm(nodes, edges)
    # sol.algo()

    best_sol = sol.multistart_algo(20)
    main.plot_sol(best_sol, by="walking")


