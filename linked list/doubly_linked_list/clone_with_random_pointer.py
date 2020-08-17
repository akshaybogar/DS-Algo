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

    def attach_nodes(self):
        if not self.head:
            return
        cur = self.head
        while cur:
            temp = Node(cur.data)
            temp.next = cur.next
            cur.next = temp
            cur = cur.next.next
        return

    def change_random_pointers(self):
        if not self.head:
            return
        cur = self.head
        while cur and cur.next:
            cur.next.prev = cur.prev.next
            cur = cur.next.next
        return

    def change_next_pointers(self):
        if not self.head:
            return
        cur = self.head.next
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        self.head = self.head.next
        return

    def traverse_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        return

if __name__ == '__main__':
    dll = DoublyLinkedList()
    for i in range(4, 0, -1):
        dll.insert_at_beginning(i)
    #Assigning random pointers prev in this case
    dll.head.prev = dll.head.next.next
    dll.head.next.prev = dll.head.next.next.next
    dll.head.next.next.prev = dll.head
    dll.head.next.next.next.prev = dll.head.next.next.next
    # Create nodes
    dll.attach_nodes()
    dll.change_random_pointers()
    dll.change_next_pointers()
    dll.traverse_list()
    cur = dll.head
    while cur:
        print(cur.prev.data, end=' ')
        cur = cur.next
