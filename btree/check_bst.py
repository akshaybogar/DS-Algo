class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isbst(root, l, r):
    if not root:
        return True
    if l and root.data > l.data:
        return False
    if r and root.data < r.data:
        return False
    return isbst(root.left, l, root) and isbst(root.right, root, r)


root = newNode(3)
root.left = newNode(2)
root.right = newNode(5)
root.right.left = newNode(1)
root.right.right = newNode(4)
if isbst(root, None, None):
    print('BST')
else:
    print('Not a BST')