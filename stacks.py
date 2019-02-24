class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # Returns the last value, but the stack structure remains the same
    def peek(self):
        return self.stack[-1]

    def size_stack(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print "Stack size {}".format(stack.size_stack())
    print "Popped {}".format(stack.pop())
    print "Popped {}".format(stack.pop())
    print "Stack size: {}".format(stack.size_stack())
    print "Peeking {}".format(stack.peek())
    print "Stack size {}".format(stack.size_stack())
