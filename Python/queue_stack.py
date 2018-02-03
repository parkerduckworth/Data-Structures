class Queue:
    def __init__(self, items=[]):
        self.items = items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) < 1:
            print("Empty queue")
            return
        return self.items.pop()

    def peek(self):
        if len(self.items) < 1:
            print("Empty queue")
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print(self):
        if len(self.items) < 1:
            print("Empty queue")
        print([x for x in self.items])


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) < 1:
            print("Empty stack")
            return
        return self.items.pop()

    def peek(self):
        if len(self.items) < 1:
            print("Empty stack")
            return
        return self.items[-1]

    def size(self):
        if len(self.items) < 1:
            print("Empty stack")
            return
        return len(self.items)


"""
Using only queues, stacks, and their instance methods,
mirror() accepts a queue of strings and appends 
the queue's contents to itself in reverse order.

['a', 'b', 'c']
becomes:
['a, 'b', 'c', 'c', 'b', 'a']
"""

def mirror(q1):
    s = Stack()
    size = q1.size()
    q2 = Queue()
    for i in range(size):
        elem = q1.dequeue()
        q2.enqueue(elem)
        q1.enqueue(elem)
    for i in range(size):
        s.push(q1.dequeue())
    while not s.is_empty():
        q1.enqueue(s.pop())
    for i in range(size):
        q1.enqueue(q2.dequeue())
    return q1


"""
Using only queues, stacks, and their instance methods,
reverse_mirror() accepts a queue of strings, reverses it, 
and appends the queue's contents to itself in reverse order.

['a', 'b', 'c']
becomes:
['c', 'b', 'a', 'a', 'b', 'c']
"""

def reverse_mirror(q):
    s = Stack()
    size = q.size()
    for i in range(size):
        elem = q.dequeue()
        s.push(elem)
        q.enqueue(elem)
    while not s.is_empty():
        q.enqueue(s.pop())
    return q


# Tests
q1 = Queue(['a', 'b', 'c'])
q2 = Queue(['a', 'b', 'c'])

mirror(q1).print()         # ['a', 'b', 'c', 'c', 'b', 'a']
reverse_mirror(q2).print() # ['c', 'b', 'a', 'a', 'b', 'c']
