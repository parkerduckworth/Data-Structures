class Node:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self, head=None):
		self.head = head


	def add(new_node):
		new_node.next = self.head
		self.head = new_node.next


	def get_position(self, position):
		curr, curr_pos = self.head, 1
		while curr:
			if curr_pos == position:
				return curr
			else:
				curr = curr.next
				cur_pos += 1
		return None


	def insert(self, new_node, position):
		curr, curr_pos = self.head, 1
		while curr_pos is not (position - 1):
			curr = curr.next
			curr_pos += 1
		new_node.next = curr.next
		curr.next = new_node


	def delete(self, data):
		curr, prev = self.head, None
		if curr.data = data:
			self.head = curr.next
			curr.next = None
		else:
			while curr and curr.value is not value:
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
