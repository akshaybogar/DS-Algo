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

    def segregate_even_odd(self):
        if not self.head:
            return
        cur = self.head
        while cur and cur.data % 2 == 0:
            cur = cur.next
        if not cur or not cur.next:
            return

        mover = cur.next
        while mover:
            if mover.data % 2 == 0:
                cur.data, mover.data = mover.data, cur.data
                cur = cur.next
            mover = mover.next


    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()


ll = LinkedList()
ll.push(12)
ll.push(14)
ll.push(1)
ll.push(8)
ll.push(4)
ll.push(5)
ll.print_list()
ll.segregate_even_odd()
ll.print_list()