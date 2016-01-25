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


class TestQuestion5(unittest.TestCase):
    def test_return_all_vertices(self):
        v1 = MyVertex('v1')
        v2 = MyVertex('v2')
        v3 = MyVertex('v3')

        g = MyGraph()
        g.add_vertex(v1)
        g.add_vertex(v2)

        v = g.vertices()

        self.assertEqual(len(v), 2)
        self.assertTrue(v1 in v)
        self.assertTrue(v2 in v)

class TestQuestion6(unittest.TestCase):
    def test_return_all_edges(self):
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

        es = g.edges()

        self.assertEqual(len(es), 2)
        self.assertTrue(e1 in es)
        self.assertTrue(e2 in es)

class TestQuestion7(unittest.TestCase):
    def test_out_vertices(self):
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

        out_vertices = g.out_vertices(v2)

        self.assertEqual(len(out_vertices), 2)
        self.assertTrue(v1 in out_vertices)
        self.assertTrue(v2 not in out_vertices)
        self.assertTrue(v3 in out_vertices)

class TestQuestion8(unittest.TestCase):
    def test_out_edges(self):
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

        out_edges = g.out_edges(v2)

        self.assertEqual(len(out_edges), 2)
        self.assertTrue(e1 in out_edges)
        self.assertTrue(e2 in out_edges)

class TestQuestion9(unittest.TestCase):
    def test_add_all_edges(self):
        v1 = MyVertex('v1')
        v2 = MyVertex('v2')
        v3 = MyVertex('v3')
        e1 = MyEdge(v1, v2)
        e2 = MyEdge(v2, v3)

        g = MyGraph()
        g.add_vertex(v1)
        g.add_vertex(v2)
        g.add_vertex(v3)

        g.add_all_edges(e1, e2)

        self.assertTrue(len(g.edges()), 2)

if __name__ == '__main__':
    unittest.main()