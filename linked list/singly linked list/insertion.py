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

    # Inserts node after a given node(prev)
    def insert(self, prev, data):
        if not prev:
            return 'Previous node cannot be null'
        node = Node(data)
        node.next = prev.next
        prev.next = node
        return

    #Utility method to print list
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(4) # 4
    linked_list.push(2) # 2->4
    linked_list.push(1) # 1->2->4
    linked_list.insert(linked_list.head.next, 3) # 1->2->3->4
    linked_list.print_list()
