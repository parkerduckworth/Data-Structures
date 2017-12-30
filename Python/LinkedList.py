class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)


    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def get_position(self, position):
        curr, curr_pos = self.head, 1
        while curr:
            if curr_pos == position:
                return curr
            else:
                curr = curr.next
                curr_pos += 1
        return None


    def insert(self, data, position):
        new_node = Node(data)
        curr, curr_pos = self.head, 1
        while curr_pos is not (position - 1):
            curr = curr.next
            curr_pos += 1
        new_node.next = curr.next
        curr.next = new_node


    def delete(self, data):
        curr, prev = self.head, None
        if curr.data == data:
            self.head = curr.next
            curr.next = None
        else:
            while curr and curr.value is not data:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            curr.next = None


def iter_reverse(L):
    if not L or not L.next:
        return L
    prev, tail = None, None
    while L:
        tail = L.next
        L.next = prev
        prev = L
        L = tail
    return prev


def recur_reverse(L):
    if not L or not L.next:
        return L
    res = recur_reverse(L.next)
    L.next.next = L
    L.next = None
    return res


def delete_duplicates_unsorted(L):  # for unsorted list
    if not L or not L.next:
        return L
    curr, prev, seen = L, None, []
    while curr:
        if curr.data not in seen:
            tail = curr.next
            prev = curr
            seen.append(curr.data)
            curr = tail
        else:
            tail = curr.next
            prev.next = tail
            curr.next = None
            curr = tail
    return L


def delete_duplicates_sorted(L):  # for sorted list
    if not L or not L.next:
        return L
    curr = L
    while curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return L


def kth_to_last(L, k):
    curr, count = L, 1
    while curr.next:
        curr = curr.next
        count += 1
    curr = L
    for i in range(count - k):
        curr = curr.next
    return curr.data


L = LinkedList(0)
L.add(6)
L.add(6)
L.add(4)
L.add(1)
L.add(3)
L.add(2)

print(kth_to_last(L.head, 3)) # 6

delete_duplicates_unsorted(L.head)

print(kth_to_last(L.head, 3)) # 4
