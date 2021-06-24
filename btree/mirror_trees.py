class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_mirror(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.data==root2.data and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)

root1 = Node(1)
root2 = Node(1)
  
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
  
root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(7)
root2.right.right = Node(4)

if is_mirror(root1, root2):
    print('Mirror trees')
else:
    print('Not mirrors')