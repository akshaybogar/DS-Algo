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

    def frequency(self, node, key):
        if not node:
            return 0
        elif node.data != key:
            return self.frequency(node.next, key)
        else:
            return 1 + self.frequency(node.next, key)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(1)
    print(linked_list.frequency(linked_list.head, 1))
