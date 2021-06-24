class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root, ans):
    if not root:
        return 0
    lheight = height(root.left, ans)
    rheight = height(root.right, ans)
    ans[0] = max(ans[0], 1+lheight+rheight)
    return 1 + max(lheight, rheight)

def diameter(root):
    if not root:
        return 0
    ans = [-999999]
    height_tree = height(root, ans)
    print('Height of the tree', height_tree)
    return ans[0]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
print('Diameter', diameter(root))