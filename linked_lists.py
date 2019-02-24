class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # Insert method for linked lists  -> O(1)
    def insert_start(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.next_node = self.head
            self.head = newNode

    def remove(self, data):
        if self.head is None:
            return

        self.size -= 1
        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

    # O(1)
    def size1(self):
        return self.size

    # O(N)
    def size2(self):
        actual_node = self.head
        size = 0
        while actual_node is not None:
            size += 1
            actual_node = actual_node.next_node
        return size

    # O(N)
    def insert_end(self, data):
        self.size += 1
        newNode = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = newNode

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print "%d" % actual_node.data
            actual_node = actual_node.next_node


if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.insert_start(12)
    linked_list.insert_start(122)
    linked_list.insert_start(3)
    linked_list.insert_end(31)

    linked_list.traverse()
    print "SIZE is {}".format(linked_list.size1())

    linked_list.remove(31)
    linked_list.remove(3)
    linked_list.remove(122)
    print "SIZE is {}".format(linked_list.size1())
