class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)


def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')


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


def list_to_bst(arr):
    if not len(arr):
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = list_to_bst(arr[ : mid])
    root.right = list_to_bst(arr[mid + 1 : ])
    return root


def find_height(root):
    if not root:
        return -1
    return max(find_height(root.left), find_height(root.left)) + 1


def is_balanced(root):
    if not root:
        return True
    return (abs(find_height(root.left) - find_height(root.right)) <= 1) \
            and is_balanced(root.left) and is_balanced(root.right)    
         

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = list_to_bst(arr)

a = TreeNode(1)
b, c, d = TreeNode(2), TreeNode(3), TreeNode(4)
e, f, g = TreeNode(5), TreeNode(6), TreeNode(7)

root2 = a
a.left, a.right, b.left, c.left, e.left, e.right = b, e, c, d, f, g

print(is_balanced(root))     # True
print(is_balanced(root2))    # False
