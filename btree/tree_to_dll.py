class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def convert_to_dll(self, root):
        if not root:
            return
        self.convert_to_dll(root.left)
        if not self.head:
            self.head = root
        else:
            root.left = self.tail
            self.tail.right = root
        self.tail = root
        self.convert_to_dll(root.right)

    def print_list(self, node):
        while node:
            print(node.data, end=' ')
            node = node.right

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
        
dll = DLL()
dll.convert_to_dll(root)
dll.print_list(dll.head)