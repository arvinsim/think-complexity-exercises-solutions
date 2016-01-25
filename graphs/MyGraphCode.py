from GraphCode import Graph, Vertex, Edge

class MyGraph(Graph):
    def get_edge(self, v1, v2):
        """#3
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
        """#4
        Remove all references to the pass edge
        :param edge:
        """
        v1 = edge[0]
        v2 = edge[1]
        del self[v1][v2]
        del self[v2][v1]

    def vertices(self):
        """#5
        Returns a list of the vertices in a graph
        :return: list
        """
        return [vertex for vertex in self]

    def edges(self):
        """#6
        Returns a list of edges form the graph
        :return: list
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



class MyVertex(Vertex):
    pass


class MyEdge(Edge):
    pass


