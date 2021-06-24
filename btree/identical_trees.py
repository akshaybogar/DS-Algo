class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.data == root2.data and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
  
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if is_identical(root1, root2):
    print('Identical')
else:
    print('Not identical')