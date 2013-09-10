class Vertex(object):

    def __init__(self, value):
        self.value = value
        self.edges = []
        self.degree = 0

    def add_edge(self, node, weight=None):
        value_tuple = (node,) if not weight else (node, weight)
        self.edges.append(value_tuple)
        self.degree += 1

    def update_weight(self, weight):
        self.value[1] = weight

    def remove_connector(self, node):
        for conn in self.edges:
            if conn[0] == node:
                self.edges.remove(conn)
                self.degree -= 1
                if self.degree < 0:
                    raise Exception

    def get_edges(self):
        return self.edges

    def is_isolated(self):
        return self.degree == 0