
class node:
    def __init__(self, id, x, y, demand, min_interval, max_interval):
        self.id = id
        self.x = x
        self.y = y
        self.demand = demand
        self.min_interval = min_interval
        self.max_interval = max_interval

    def __str__(self):
        return str(self.id)

class edge:
    def __init__(self, node_x, node_y, velocidad=80):
        self.x = node_x
        self.y = node_y
        self.velocidad = velocidad
        if node_x.id > node_y.id:
            self.dist = ((node_x.x - node_y.x)**2 + (node_x.y - node_y.y)**2)**(1/2)
        else:
            self.dist = (((node_x.x - node_y.x) ** 2 + (node_x.y - node_y.y) ** 2) ** (1 / 2)) * (1.1)
        self.time = self.dist/self.velocidad

    def __str__(self):
        return str(self.x.id)+"-"+str(self.y.id)

class route:
    def __init__(self, edges, demand = 0):
        self.route = edges
        self.dist = sum([i.dist for i in edges])
        self.time = sum([i.time for i in edges])
        self.demand = demand

    def reverse(self):
        edges = []
        for i in range(len(self.route)):
            edges.append(edge(self.route[len(self.route)-i-1].y, self.route[len(self.route)-i-1].x))
        self.route = edges

    def __str__(self):
        t = "0"
        for i in self.route:
            t += "-" + str(i.y.id)

        return t