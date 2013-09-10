from unittest import TestCase
from graphcore.graph import DirectedGraph, UnDirectedGraph
from test.test_resource import graph


class DirectedGraphTest(TestCase):

    def setUp(self):
        self.graph = DirectedGraph(graph)

    def test_len_graph(self):
        self.assertEqual(6, len(self.graph.vertexes))

    def test_degree_e(self):
        self.assertEqual(1, self.graph.get_node_from_value('e').degree)

    def test_degree_c(self):
        self.assertEqual(4, self.graph.get_node_from_value('c').degree)

    def test_isolated_node(self):
        isolated = self.graph.get_isolated_vertices()
        self.assertEqual(1, len(isolated))
        self.assertEqual('f', isolated[0].value)

    def test_connect_isolate_node(self):
        self.graph.add_edge("f", "a")
        isolated = self.graph.get_isolated_vertices()
        self.assertEqual(0, len(isolated))
        self.assertEqual(1, self.graph.get_node_from_value('f').degree)


class UndirectedGraphTest(TestCase):

    def setUp(self):
        self.graph = UnDirectedGraph(graph)

    def test_len_graph(self):
        self.assertEqual(6, len(self.graph.vertexes))

    def test_degree_e(self):
        self.assertEqual(2, self.graph.get_node_from_value('e').degree)

    def test_degree_c(self):
        self.assertEqual(8, self.graph.get_node_from_value('c').degree)

    def test_isolated_node(self):
        isolated = self.graph.get_isolated_vertices()
        self.assertEqual(1, len(isolated))
        self.assertEqual('f', isolated[0].value)

    def test_connect_isolate_node(self):
        self.graph.add_edge("e", "f")
        isolated = self.graph.get_isolated_vertices()
        self.assertEqual(0, len(isolated))
        self.assertEqual(1, self.graph.get_node_from_value('f').degree)
        self.assertEqual(3, self.graph.get_node_from_value('e').degree)