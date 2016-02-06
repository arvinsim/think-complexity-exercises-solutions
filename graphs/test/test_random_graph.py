import unittest
from graphs.greenteapress.GraphCode import Graph, Vertex, Edge
from graphs.RandomGraph import RandomGraph

class TestExercises1(unittest.TestCase):
    def test_get_number_of_edges(self):
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        d = Vertex('d')

        rg = RandomGraph()
        rg.add_vertex(a)
        rg.add_vertex(b)
        rg.add_vertex(c)
        rg.add_vertex(d)

        self.assertEqual(rg._get_probable_number_of_edges(0), 0)
        self.assertEqual(rg._get_probable_number_of_edges(0.25), 1)
        self.assertEqual(rg._get_probable_number_of_edges(0.5), 2)
        self.assertEqual(rg._get_probable_number_of_edges(0.75), 3)
        self.assertEqual(rg._get_probable_number_of_edges(1), 4)

    def test_add_random_edges(self):
        probability = 0.5

        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        d = Vertex('d')

        rg = RandomGraph()
        rg.add_vertex(a)
        rg.add_vertex(b)
        rg.add_vertex(c)
        rg.add_vertex(d)

        rg.add_random_edges(probability)

        # TODO: Check if the number of edges is correct

    def test_foobar(self):
        pass

if __name__ == '__main__':
    unittest.main()


