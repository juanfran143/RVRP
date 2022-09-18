from classes import *

class algorithm:
    def __init__(self, nodes):
        self.nodes = nodes

    def create_saving_list(self):
        saving_list = []
        for i in range(1, len(self.nodes)):
            for j in range(i+1, len(self.nodes)-1):
                edge_i = edge(self.nodes[i], self.nodes[0])
                edge_j = edge(self.nodes[j], self.nodes[0])
                edge_i_j = edge(self.nodes[i], self.nodes[j])
                saving_list.append((i, j, edge_i.dist+edge_j.dist-edge_i_j.dist))

        return saving_list

    def dummy_solution(self):
        routes = []
        for i in range(1, len(self.nodes)):
            routes.append([edge(self.nodes[i], self.nodes[0]), edge(self.nodes[0], self.nodes[i])])

        return routes

    def algo(self):
        routes = self.dummy_solution()
        saving_list = self.create_saving_list()
        