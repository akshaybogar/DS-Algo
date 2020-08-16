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

    def traverse_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()
        return

    def reverse_list(self):
        if not self.head:
            return
        cur, temp = self.head, None
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev
        return

if __name__ == '__main__':
    dll = DoublyLinkedList()
    for i in range(5, -1, -1):
        dll.insert_at_beginning(i)
    print('Original list')
    dll.traverse_list()
    print('Reversed list')
    dll.reverse_list()
    dll.traverse_list()
