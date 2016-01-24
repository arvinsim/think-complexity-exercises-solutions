from GraphCode import Graph, Vertex, Edge

class MyGraph(Graph):
    def get_edge(self, v1, v2):
        """TODO: #3
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


class MyVertex(Vertex):
    pass


class MyEdge(Edge):
    pass


