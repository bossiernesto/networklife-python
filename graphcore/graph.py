from .vertex import Vertex


class Graph(object):

    def __init__(self, dict_graph=None):
        self.vertexes = set()
        if dict_graph:
            self.parse_dict_graph(dict_graph)

    def get_node_from_value(self, value):
        for node in self.vertexes:
            if node.value == value:
                return node
        return None

    def add_vertex_if_not_found(self, value):
        node = self.get_node_from_value(value)
        if not node:
            node = Vertex(value)
            self.vertexes.add(node)
        return node

    def parse_dict_graph(self, dict_graph):
        for vertex, connectors in dict_graph.items():
            self.associate_connectors(vertex, connectors)

    def associate_connectors(self, vertex, connectors):
        raise NotImplementedError

    def add_edge(self, from_value, to_value):
        self.associate_connectors(from_value, [to_value])

    def get_isolated_vertices(self):
        return [vertex for vertex in self.vertexes if vertex.is_isolated()]

    def min_delta(self):
        return min([vertex.degree for vertex in self.vertexes])

    def max_delta(self):
        return max([vertex.degree for vertex in self.vertexes])

    def density(self):
        """ method to calculate the density of a graph """
        V = len(self.vertexes)
        E = sum([len(vertex.get_edges()) for vertex in self.vertexes])
        return 2.0 * E / (V * (V - 1))


class DirectedGraph(Graph):

    def associate_connectors(self, vertex, connectors):
        node = self.add_vertex_if_not_found(vertex)
        for conn in connectors:
            conn_vertex = self.add_vertex_if_not_found(conn)
            node.add_edge(conn_vertex)


class UnDirectedGraph(Graph):

    def associate_connectors(self, vertex, connectors):
        node = self.add_vertex_if_not_found(vertex)
        for conn in connectors:
            conn_vertex = self.add_vertex_if_not_found(conn)
            node.add_edge(conn_vertex)
            conn_vertex.add_edge(node)

    def degree_sequence(self):
        return tuple([vertex.degree for vertex in self.vertexes].sort(reverse=True))
