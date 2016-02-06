import random
from graphs.greenteapress.GraphCode import Graph, Vertex, Edge

class RandomGraph(Graph):
    def __init__(self):
        super(RandomGraph, self).__init__()

    def _get_probable_number_of_edges(self, p):
        """
        Gets probable number of edges that should be distributed
        to vertices given probability p
        :param p: the probability
        :return:
        """
        vertices = [vertex for vertex in self]
        return int(p * len(vertices))

    def _get_possible_vertex_combinations(self):
        """
        Gets the possible vertex pairs that edges can be
        assigned to
        :return:
        """
        adjacency_matrix = set()
        for v1 in self:
            for v2 in self:
                if v1 != v2 \
                    and (v1, v2) not in adjacency_matrix \
                    and (v2, v1) not in adjacency_matrix:
                    adjacency_matrix.add((v1, v2))
        return adjacency_matrix

    def add_random_edges(self, p):
        # Get the number of probable edges
        # based on parameter p
        probable_number_of_edges = self._get_probable_number_of_edges(p)

        # Get the possible edges of the graph
        possible_vertex_combinations = self._get_possible_vertex_combinations()

        # Randomly pick possible edges from the list
        vertex_combinations = random.sample(
            possible_vertex_combinations,
            probable_number_of_edges
        )

        # Set edges
        print(vertex_combinations)
        for vc in vertex_combinations:
            self.add_edge(Edge(vc[0], vc[1]))
        print(self)

