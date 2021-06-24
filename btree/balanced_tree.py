class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if not root:
        return 0
    l = height(root.left)
    r = height(root.right)
    return max(l, r) + 1

def isbalanced(root):
    if not root:
        return True
    lh = height(root.left)
    rh = height(root.right)
    return (abs(lh - rh) <= 1) and isbalanced(root.left) and isbalanced(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)
root.right.right.right = Node(5)
print(height(root))
print(isbalanced(root))