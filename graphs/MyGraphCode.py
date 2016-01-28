from GraphCode import Graph, Vertex, Edge

class MyGraph(Graph):
    def get_edge(self, v1, v2):
        """Exercise 2.2 #3
        Return an edge if it exists between v1 and v2
        None otherwise
        :param v1:
        :param v2:
        :return: Edge
        """
        try:
            return self[v1][v2]
        except:
            return None

    def remove_edge(self, edge):
        """Exercise 2.2 #4
        Remove all references to the pass edge
        :param edge:
        """
        v1 = edge[0]
        v2 = edge[1]
        del self[v1][v2]
        del self[v2][v1]

    def vertices(self):
        """Exercise 2.2 #5
        Returns a list of the vertices in a graph
        :return: list
        """
        return [vertex for vertex in self]

    def edges(self):
        """Exercise 2.2 #6
        Returns a list of edges from the graph
        :return: Set
        """
        vertices = self.vertices()
        edges = set()
        for v1 in vertices:
            for v2 in vertices:
                try:
                    edges.add(self[v1][v2])
                except:
                    pass
        return edges

    def out_vertices(self, vertex):
        """Exercise 2.2 #7
        Takes a vertex and returns a list of adjacent vertices
        :return: Set
        """
        adjacent_vertices = set()
        for v in self[vertex]:
            adjacent_vertices.add(v)
        return adjacent_vertices

    def out_edges(self, vertex):
        """Exercise 2.2 #8
        Takes a vertex and returns a list of connected edges
        :return: Set
        """
        connected_edges = set()
        for v in self[vertex]:
            connected_edges.add(self[vertex][v])
        return connected_edges

    def add_all_edges(self, *edges):
        """Exercise 2.2 #9
        Add all edges between all pairs of vertices
        """
        vertices = self.vertices()
        for edge in edges:
            for v1 in vertices:
                for v2 in vertices:
                    self[v1][v2] = edge


class MyVertex(Vertex):
    pass


class MyEdge(Edge):
    pass


