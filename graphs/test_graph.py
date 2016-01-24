import unittest
from MyGraphCode import MyGraph, MyVertex, MyEdge

class TestQuestion3(unittest.TestCase):
    def test_return_true(self):
        v1 = MyVertex('v1')
        v2 = MyVertex('v2')
        e = MyEdge(v1, v2)

        g = MyGraph()
        g.add_vertex(v1)
        g.add_vertex(v2)
        g.add_edge(e)

        result = g.get_edge(v1, v2)

        self.assertIsNot(result, None)

    def test_return_none(self):
        v1 = MyVertex('v1')
        v2 = MyVertex('v2')
        v3 = MyVertex('v3')
        e = MyEdge(v1, v3)

        g = MyGraph()
        g.add_vertex(v1)
        g.add_vertex(v2)
        g.add_vertex(v3)
        g.add_edge(e)

        result = g.get_edge(v1, v2)

        self.assertIs(result, None)

class TestQuestion4(unittest.TestCase):
    def test_remove_all_edges(self):
        v1 = MyVertex('v1')
        v2 = MyVertex('v2')
        v3 = MyVertex('v3')
        e1 = MyEdge(v1, v2)
        e2 = MyEdge(v2, v3)

        g = MyGraph()
        g.add_vertex(v1)
        g.add_vertex(v2)
        g.add_vertex(v3)
        g.add_edge(e1)
        g.add_edge(e2)

        g.remove_edge(e1)

        self.assertIs(g.get_edge(v1, v2), None)

if __name__ == '__main__':
    unittest.main()