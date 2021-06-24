class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(count_leaves(root))