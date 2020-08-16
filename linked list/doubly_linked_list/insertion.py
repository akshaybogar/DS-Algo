class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        return

    def insert_at_end(self, data):
        temp = Node(data)
        if not self.head:
            self.head = temp
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = temp
        temp.prev = last
        return

    def insert_after_node(self, prev, data):
        if not self.head or not prev:
            return
        temp = Node(data)
        temp.next = prev.next
        prev.next = temp
        temp.prev = prev
        if temp.next:
            temp.next.prev = temp
        return

    def insert_before_node(self, next_node, data):
        if not self.head or not next_node:
            return
        temp = Node(data)
        temp.prev = next_node.prev
        next_node.prev = temp
        temp.next = next_node
        if temp.prev:
            temp.prev.next = temp
        else:
            self.head = temp
        return

    def traverse_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        return

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning(1)
    dll.insert_at_end(4)
    dll.insert_after_node(dll.head, 2)
    dll.insert_before_node(dll.head, 5)
    dll.traverse_list()
