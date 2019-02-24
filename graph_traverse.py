class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.predecessor = None


# Breadth - first search algorithm
class BFS(object):
    def bfs(self, start_node):
        queue = []
        queue.append(start_node)
        start_node.visited = True

        # BFS --> queue
        while queue:
            actual_node = queue.pop(0)
            print "%s" % actual_node.name

            for n in actual_node.adjacency_list:
                if not n.visited:
                    n.visited = True
                    queue.append(n)


# Depth - first search algorithm
class DFS(object):
    def dfs(self, node):
        node.visited = True
        print "%s" % node.name

        # Stacks but usually implemented with recursion
        for n in node.adjacency_list:
            if not n.visited:
                self.dfs(n)


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    print "BFS:"
    bfs = BFS()
    bfs.bfs(node1)

    node2_1 = Node("A")
    node2_2 = Node("B")
    node2_3 = Node("C")
    node2_4 = Node("D")
    node2_5 = Node("E")

    node2_1.adjacency_list.append(node2_2)
    node2_1.adjacency_list.append(node2_3)
    node2_2.adjacency_list.append(node2_4)
    node2_4.adjacency_list.append(node2_5)
    print "DFS:"
    dfs = DFS()
    dfs.dfs(node2_1)
