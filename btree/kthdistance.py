class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kthdistance_nodes(root, k):
    if not root:
        return
    if k == 0:
        print(root.data, end=' ')
        return
    else:
        kthdistance_nodes(root.left, k-1)
        kthdistance_nodes(root.right, k-1)

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
kthdistance_nodes(root, 2)