
class node:
    def __init__(self, id, x, y, demand):
        self.id = id
        self.x = x
        self.y = y
        self.depot = None
        self.demand = demand

    def __str__(self):
        return str(self.id)

class edge:
    def __init__(self, node_x, node_y):
        self.x = node_x
        self.y = node_y
        self.dist = ((node_x.x - node_y.x)**2 + (node_x.y - node_y.y)**2)**(1/2)

    def __str__(self):
        return str(self.x.id)+"-"+str(self.y.id)

class route:
    def __init__(self, edges, demand = 0):
        self.route = edges
        self.dist = sum([i.dist for i in edges])
        self.demand = demand

    def reverse(self):
        edges = []
        for i in range(len(self.route)):
            edges.append(edge(self.route[len(self.route)-i-1].y, self.route[len(self.route)-i-1].x))
        self.route = edges
    def __str__(self):
        t = str(self.route[0].x.id)
        for i in self.route:
            t += "-" + str(i.y.id)

        return t