import copy

from classes import *
from plot import plot_sol
from time import sleep
import random as rnd
import time
class algorithm:

    def __init__(self, nodes, capacity=10, n_depots = 1):
        self.nodes = nodes
        self.n_depots = n_depots
        self.routes = []
        self.capacity = capacity

    def create_saving_list(self):
        saving_list = []
        for i in range(self.n_depots, len(self.nodes)-1):
            for j in range(i+1, len(self.nodes)):
                if self.nodes[i].depot == self.nodes[j].depot:
                    edge_i = edge(self.nodes[i], self.nodes[self.nodes[i].depot])
                    edge_j = edge(self.nodes[j], self.nodes[self.nodes[i].depot])
                    edge_i_j = edge(self.nodes[i], self.nodes[j])
                    saving_list.append((i, j, edge_i.dist+edge_j.dist-edge_i_j.dist))

        return saving_list

    def dummy_solution_multidepot(self):
        routes = []
        for i in range(self.n_depots, len(self.nodes)):
            dist = []
            for j in range(self.n_depots):
                dist.append((j, ((self.nodes[j].x - self.nodes[i].x) ** 2 + (self.nodes[j].y - self.nodes[i].y) ** 2) ** (1 / 2)))

            dist.sort(key=lambda x: x[1])
            selected = rnd.randint(0, min([len(dist), 1]))

            self.nodes[i].depot = selected
            routes.append(route([edge(self.nodes[selected], self.nodes[i]), edge(self.nodes[i], self.nodes[selected])],
                                demand = self.nodes[i].demand))

        return routes

    def merge_routes(self, edge, saving, verbose_plot = False):
        route_1 = -1
        route_2 = -1
        for i, r in enumerate(self.routes):
            route = [r.route[0].y.id] + [r.route[0].x.id] + [r.route[-1].x.id] + [r.route[-1].y.id]
            if edge.x.id in route:
                route_1 = i
            if edge.y.id in route:
                route_2 = i
            if route_1 != -1 and route_2 != -1:
                break

        plot = False
        if route_1 != route_2 and self.routes[route_1].demand+self.routes[route_2].demand <= self.capacity \
                and route_1 != -1 and route_2 != -1 and self.routes[route_1].route[0].x.id == self.routes[route_2].route[0].x.id:
            
            if self.routes[route_1].route[0].y.id == edge.x.id and self.routes[route_2].route[0].y.id == edge.y.id:
                self.routes[route_1].reverse()
                self.routes[route_1].route = self.routes[route_1].route[:-1] + [edge] + self.routes[route_2].route[1:]
                plot = True

            elif self.routes[route_1].route[-1].x.id == edge.x.id and self.routes[route_2].route[-1].x.id == edge.y.id:
                self.routes[route_2].reverse()
                self.routes[route_1].route = self.routes[route_1].route[:-1] + [edge] + self.routes[route_2].route[1:]
                plot = True

            elif self.routes[route_1].route[0].y.id == edge.x.id and self.routes[route_2].route[-1].x.id == edge.y.id:
                self.routes[route_1].route = self.routes[route_2].route[:-1] + [edge] + self.routes[route_1].route[1:]
                plot = True

            else:
                self.routes[route_1].route = self.routes[route_1].route[:-1] + [edge] + self.routes[route_2].route[1:]
                plot = True

            self.routes[route_1].dist = self.routes[route_1].dist - saving + self.routes[route_2].dist
            self.routes[route_1].demand = self.routes[route_1].demand + self.routes[route_2].demand
            del self.routes[route_2]

        if plot and verbose_plot:
            plot_sol(self.routes, self.nodes)

    def get_saving(self, saving_list):

        # Random
        # saving_list.pop(rnd.randint(0, len(saving_list)-1))
        # GRASP
        # saving_list.pop(rnd.randint(0, min([5, len(saving_list)-1])))
        # Greedy
        # saving_list.pop(0)

        return saving_list.pop(rnd.randint(0, min([5, len(saving_list)-1])))

    def algo(self):
        self.routes = self.dummy_solution()
        plot_sol(self.routes, self.nodes)
        saving_list = self.create_saving_list()
        saving_list.sort(key=lambda x: x[2], reverse=True)
        while len(saving_list) > 0:
            s = self.get_saving(saving_list)
            self.merge_routes(edge(self.nodes[s[0]], self.nodes[s[1]]), verbose_plot=True)

    def multistart_algo(self, computing_time):
        start = time.time()
        best_dist = -1

        while time.time() - start < computing_time:
            self.routes = self.dummy_solution_multidepot()
            #plot_sol(self.routes, self.nodes)
            saving_list = self.create_saving_list()
            saving_list.sort(key=lambda x: x[2], reverse=True)
            while len(saving_list) > 0:
                s = self.get_saving(saving_list)
                self.merge_routes(edge(self.nodes[s[0]], self.nodes[s[1]]), s[2])

            if best_dist == -1 or best_dist > sum([i.dist for i in self.routes]):
                best_dist = sum([i.dist for i in self.routes])
                best_route = copy.deepcopy(self.routes)

        plot_sol(best_route, self.nodes, self.n_depots)



