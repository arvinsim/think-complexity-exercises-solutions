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
        :return:
        """
        v1 = edge[0]
        v2 = edge[1]
        del self[v1][v2]
        del self[v2][v1]


class MyVertex(Vertex):
    pass


class MyEdge(Edge):
    pass


