import sys

# Bellman ford shortest path algo implementation


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = sys.maxsize


class Edge(object):
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Algo(object):
    HAS_CYCLE = False

    def calc_shortest_path(self, vertex_list, edge_list, start_vertex):
        start_vertex.min_distance = 0

        for i in range(0, len(vertex_list)-1):
            for edge in edge_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    v.min_distance = new_distance
                    v.predecessor = u

        for edge in edge_list:
            if self.has_cycle(edge):
                print "Negative cycle detected"
                Algo.HAS_CYCLE = True
                return

    def has_cycle(self, edge):
        edge_distance = (edge.start_vertex.min_distance + edge.weight)
        if edge_distance < edge.target_vertex.min_distance:
            return True
        else:
            return False

    def get_shortest_path(self, target_vertex):
        if not Algo.HAS_CYCLE:
            print "Shortest path is with value %s" % target_vertex.min_distance

            node = target_vertex

            while node:
                print "%s" % node.name
                node = node.predecessor
        else:
            print "Negative cycle detected"


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node2.adjacency_list.append(edge6)
    node8.adjacency_list.append(edge7)
    node8.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node5.adjacency_list.append(edge11)
    node6.adjacency_list.append(edge12)
    node6.adjacency_list.append(edge13)
    node3.adjacency_list.append(edge14)
    node3.adjacency_list.append(edge15)
    node4.adjacency_list.append(edge16)

    vertex_list = (node1, node2, node3, node4, node5, node6, node7, node8)
    edge_list = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8,
                 edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16)

    algo = Algo()
    algo.calc_shortest_path(vertex_list, edge_list, node1)
    algo.get_shortest_path(node7)
