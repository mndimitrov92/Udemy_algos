def arr_reverse(arr):
    '''Reversing and array with an in place solution O(N)'''
    start_index = 0
    end_index = len(arr) - 1

    while end_index > start_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

    return arr


def is_pelindrome(word):
    '''
    Checking if the words is a pelindrome
    ex: radar
    '''
    return word == word[::-1]


def reverse_integers(n):
    '''Reverses the digits in an int'''
    reversed_int = 0
    remainder = 0

    while n > 0:
        remainder = n % 10
        n = n // 10
        reversed_int = reversed_int*10 + remainder

    return reversed_int


def find_duplicates(arr):
    '''
    Finds the duplicates in an array
    Can be used only when the max number in the array
    is less than the length of the array
    '''
    for i in arr:
        if arr[abs(i)] >= 0:
            arr[abs(i)] = - arr[abs(i)]
        else:
            print "Repetition found at %s" % abs(i)


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    a = sorted(word1)
    b = sorted(word2)

    return a == b


def kadane_algo(arr):
    '''Finds the largest sum of a subarray in an array'''
    max_global = arr[0]
    max_current = arr[0]

    for i in range(len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    '''Getting the middle node of a linked list'''

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) time complexity
    def get_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.next_node and \
                fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    # O(1) time complexity
    def insert_start(self, data):
        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove(self, data):
        if self.head is not None:
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

    def size1(self):
        return self.size

    def size2(self):
        actual_node = self.head
        size = 0

        while actual_node is not None:
            size += 1
            actual_node = actual_node.next_node

        return size

    def insert_end(self, data):
        self.size += 1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node
        actual_node.next_node = new_node

    def traverse_list(self):
        actual_node = self.head

        while actual_node is not None:
            print "{}".format(actual_node.data)
            actual_node = actual_node.next_node


class MaxStack(object):
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)

        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.main_stack.pop()
        return self.main_stack.pop()

    def get_max_item(self):
        return self.max_stack.pop()


if __name__ == "__main__":
    # Reversing and array check
    arr = [1, 2, 3, 4, 5]
    print arr_reverse(arr)

    # Pelindrome check
    word = 'radar'
    print is_pelindrome(word)

    # Integer reversal check
    num = 6789
    print reverse_integers(num)

    # Finding duplicates in an array check
    second_arr = [1, 2, 3, 4, 5, 1]
    find_duplicates(second_arr)

    # Anagram check
    print is_anagram('asdd', 'dsad')

    # Finding the largest sum of a subarray
    nums = [1, -2, 3, 4, 5, -8]
    print kadane_algo(nums)

    # Finding the middle node in a linked list
    # And reversing a linked list
    linked_list = LinkedList()

    linked_list.insert_start(12)
    linked_list.insert_start(122)
    linked_list.insert_start(3)
    linked_list.insert_start(31)
    linked_list.insert_start(10)
    linked_list.insert_start(11)
    linked_list.insert_start(26)

    print linked_list.get_middle_node().data
    print "Traversing the list..."
    linked_list.traverse_list()
    print "Reversing the list..."
    linked_list.reverse()
    linked_list.traverse_list()

    # Getting the max element of a stack
    print "Max of Stack"
    max_stack = MaxStack()

    max_stack.push(100)
    max_stack.push(2)
    max_stack.push(99)
    max_stack.push(23)
    max_stack.push(276)
    print max_stack.get_max_item()
