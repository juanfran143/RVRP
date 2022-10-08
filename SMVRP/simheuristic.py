import random as rnd
import numpy as np
from classes import edge

class Simheuristic:

    def __init__(self, simulations, var_distance= 0, var_demand = 0):
        self.simulations = simulations
        self.var_distance = var_distance
        self.var_demand = var_demand

    """ 
    def simulation_distance(self, solution):
        distances = []
        for _ in self.simulations:
            suma = 0
            for route in solution:
                for edge in route.route:
                    suma += rnd.lognormvariate(edge.dist, self.var)

            distances.append(suma)

        return distances
    """
    def simulation(self, solution, capacity = 9999999999):
        """

        :param solution: Solution from the algorithm
        :param capacity: Capcity of the truck
        :return: A list of distances (distances) and the number of failures in the solution (in case that demand is
        include in the simulation)
        """
        distances = []
        fail = 0

        for _ in range(self.simulations):
            distance = 0
            first = True
            for route in solution:
                demand = 0

                for selected_edge in route.route[:-1]:
                    aux = np.random.lognormal(np.log(selected_edge.y.demand), self.var_demand)
                    demand += aux
                    distance += np.random.lognormal(np.log(selected_edge.dist), self.var_distance)
                    if demand > capacity:
                        demand = aux
                        distance += (edge(selected_edge.x, route.route[0].x)).dist + (edge(route.route[0].x, selected_edge.y)).dist - selected_edge.dist
                        if first:
                            first = False
                            fail += 1

            distances.append(distance)

        return (distances, fail)