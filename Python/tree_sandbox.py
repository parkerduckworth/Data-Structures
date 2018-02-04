class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


###### Traversal Methods ######
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=' ')
        in_order(root.right)


def pre_order(root):
    if root:
        print(root.data, end=' ')
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=' ')


def level_order(root):
    if not root:
        return
    Q = []
    Q.append(root)
    while Q:
        curr = Q[0]
        print(curr.data, end=' ')
        if curr.left:
            Q.append(curr.left)
        if curr.right:
            Q.append(curr.right)
        Q.pop(0)


###### Find Min/Max Data ######
def find_min_iter(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.data


def find_max_iter(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.data


def find_min_recur(root):
    if not root:
        return None
    elif not root.left:
        return root.data
    return find_min_iter(root.left)


def find_max_recur(root):
    if not root:
        return None
    elif not root.right:
        return root.data
    return find_max_iter(root.right)


###### Convert List to Binary Search Tree ######
def list_to_bst(arr):
    if not len(arr):
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = list_to_bst(arr[ : mid])
    root.right = list_to_bst(arr[mid + 1 : ])
    return root


###### Find Height/Max Depth ######
def find_height(root):
    if not root:
        return -1
    return max(find_height(root.left), find_height(root.left)) + 1


###### Determine Balance ######
def is_balanced(root):
    if not root:
        return True
    return (abs(find_height(root.left) - find_height(root.right)) <= 1) \
            and is_balanced(root.left) and is_balanced(root.right)   


###### Merge Non-Null Nodes ######
def merge_trees(root1, root2):
    if not root1 or not root2:
        return root1 or root2
    else:
        root1.data += root2.data
        root1.left = merge_trees(root1.left, root2.left)
        root1.right = merge_trees(root1.right, root2.right)
    return root1
         

###### Tests ######
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root1 = list_to_bst(arr)

a = TreeNode(1)
b, c, d = TreeNode(2), TreeNode(3), TreeNode(4)
e, f, g = TreeNode(5), TreeNode(6), TreeNode(7)

root2 = a
a.left, a.right, b.left, c.left, e.left, e.right = b, e, c, d, f, g

print(is_balanced(root1))    # True
print(is_balanced(root2))    # False


in_order(root1)
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
in_order(root2)
# 4, 3, 2, 1, 6, 5, 7
in_order(merge_trees(root1, root2))
# 5, 5, 5, 4, 5, 7, 7, 14, 14, 17
