class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert nodes at the beginning of linked list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def find_length(self, node):
        if not node:
            return 0
        return 1+self.find_length(node.next)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    print(linked_list.find_length(linked_list.head))
