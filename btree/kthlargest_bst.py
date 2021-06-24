count = 0
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kthlargest(root, k):
    global count
    if root:
        kthlargest(root.right, k)
        count += 1
        if count == k:
            print(root.data)
        kthlargest(root.left, k)

root = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(7)
root.right.right = Node(9)
root.right.left = Node(6)
kthlargest(root, 3)