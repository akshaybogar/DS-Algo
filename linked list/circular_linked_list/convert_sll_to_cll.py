class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def convert_to_circular(self):
        if not self.head:
            return None
        last = self.head
        while last.next:
            last = last.next
        last.next = self.head
        return

    def print_sll(self):
        cur = self.head
        while cur:
            print(cur.data, end = ' ')
            cur = cur.next
        print()

    def print_cll(self):
        if not self.head:
            return
        cur = self.head.next
        print(self.head.data, end=' ')
        while cur is not self.head:
            print(cur.data, end=' ')
            cur = cur.next
        return

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll.print_sll()
    ll.convert_to_circular()
    ll.print_cll()
