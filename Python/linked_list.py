class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data



class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
        return True

    def remove(self, data):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node
                self.size -= 1
                return True         # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False          # data not found

    def find(self, data):
        this_node = self.head
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None

    def print_list(self):
        this_node = self.head
        L = []
        while this_node:
            L.append(this_node.get_data())
            this_node = this_node.get_next()
        print(L)