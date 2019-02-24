import heapq


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    def __cmp__(self, other_edge):
        return self.cmp(self.weight, other_edge.weight)

    def __lt__(self, other_edge):
        self_priority = self.weight
        other_priority = other_edge.weight
        return self_priority < other_priority


class PrimsAlgo(object):
    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list
        self.spanning_tree = []
        self.edge_heap = []
        self.full_cost = 0

    def calc_spanning_tree(self, vertex):
        self.unvisited_list.remove(vertex)

        while unvisited_list:
            for edge in vertex.adjacency_list:
                if edge.target_vertex in self.unvisited_list:
                    heapq.heappush(self.edge_heap, edge)

            min_edge = heapq.heappop(self.edge_heap)

            self.spanning_tree.append(min_edge)
            print "Edge added to tree %s %s" % (
                min_edge.start_vertex.name, min_edge.target_vertex.name)
            self.full_cost += min_edge.weight

            vertex = min_edge.target_vertex
            self.unvisited_list.remove(vertex)

    def get_spanning_tree(self):
        return self.spanning_tree


if __name__ == "__main__":
    node1 = Vertex('A')
    node2 = Vertex('B')
    node3 = Vertex('C')

    edge1 = Edge(100, node1, node2)
    edge2 = Edge(100, node2, node1)
    edge3 = Edge(1000, node1, node3)
    edge4 = Edge(1000, node3, node1)
    edge5 = Edge(0.1, node3, node2)
    edge6 = Edge(0.1, node2, node3)

    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge6)
    node3.adjacency_list.append(edge4)
    node3.adjacency_list.append(edge5)

    unvisited_list = []
    unvisited_list.append(node1)
    unvisited_list.append(node2)
    unvisited_list.append(node3)

    algo = PrimsAlgo(unvisited_list)
    algo.calc_spanning_tree(node1)
