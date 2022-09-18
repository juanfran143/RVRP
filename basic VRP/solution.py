from classes import *

class algorithm:
    def __init__(self, nodes, capacity = 10):
        self.nodes = nodes
        self.routes = []
        self.capacity = capacity

    def create_saving_list(self):
        saving_list = []
        for i in range(1, len(self.nodes)-1):
            for j in range(i+1, len(self.nodes)):
                edge_i = edge(self.nodes[i], self.nodes[0])
                edge_j = edge(self.nodes[j], self.nodes[0])
                edge_i_j = edge(self.nodes[i], self.nodes[j])
                saving_list.append((i, j, edge_i.dist+edge_j.dist-edge_i_j.dist))

        return saving_list

    def dummy_solution(self):
        routes = []
        for i in range(1, len(self.nodes)):
            routes.append(route([edge(self.nodes[0], self.nodes[i]), edge(self.nodes[i], self.nodes[0])],
                                demand = self.nodes[i].demand))

        return routes

    def merge_routes(self, edge):
        route_1 = -1
        route_2 = -1
        for i, r in enumerate(self.routes):
            route = [r.route[0].y.id] + [r.route[-1].x.id]
            if edge.x.id in route:
                route_1 = i
            if edge.y.id in route:
                route_2 = i
            if route_1 != -1 and route_2 != -1:
                break

        if route_1 != route_2 and self.routes[route_1].demand+self.routes[route_2].demand <= self.capacity \
                and route_1 != -1 and route_2 != -1:
            self.routes[route_1].route = self.routes[route_1].route[:-1] + [edge] + self.routes[route_2].route[1:]
            self.routes[route_1].demand = self.routes[route_1].demand + self.routes[route_2].demand
            del self.routes[route_2]

    def algo(self):
        self.routes = self.dummy_solution()
        saving_list = self.create_saving_list()
        while len(saving_list) > 0:
            s = saving_list.pop(0)
            self.merge_routes(edge(self.nodes[s[0]], self.nodes[s[1]]))

        for r in self.routes:
            print(r.__str__())

