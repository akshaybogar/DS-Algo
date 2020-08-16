class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

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

    def traverse_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()
        return

    def delete_node(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        cur = self.head
        while cur and cur.data != key:
            cur = cur.next
        if cur:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            cur = None
        return

if __name__ == '__main__':
    dll = DoublyLinkedList()
    for i in range(6):
        dll.insert_at_end(i)
    print('Original list')
    dll.traverse_list()
    print('After deleting', 0)
    dll.delete_node(0)
    dll.traverse_list()
