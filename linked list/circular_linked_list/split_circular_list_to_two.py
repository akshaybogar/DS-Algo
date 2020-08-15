class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(node):
        return '%s' % node.data

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insert_empty(self, data):
        if self.last:
            return self.last
        temp = Node(data)
        self.last = temp
        temp.next = self.last
        return self.last

    def add_node_at_end(self, data):
        if not self.last:
            return None
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp

    def split_circular_list_to_two(self):
        if not self.last:
            return None, None
        slow, fast = self.last.next, self.last.next
        if slow == self.last:
            print('Only 1 element present in the list')
            return self.last, None
        while fast.next != self.last.next and fast.next.next != self.last.next:
            slow = slow.next
            fast = fast.next.next
        head, slow_next = self.last.next, slow.next
        slow.next = head
        self.last.next = slow_next
        return slow, self.last

    def traverse_list(self):
        if not self.last:
            print('List empty')
            return

        p = self.last.next
        while p:
            print(p.data, end = ' ')
            p = p.next
            if p == self.last.next:
                break
        print()

if __name__ == '__main__':
    cl = CircularLinkedList()
    last_node = cl.insert_empty(1)
    for i in range(2,5):
        last_node = cl.add_node_at_end(i)
    print('Original list')
    cl.traverse_list()
    l1, l2 = CircularLinkedList(), CircularLinkedList()
    l1.last, l2.last = cl.split_circular_list_to_two()
    l1.traverse_list()
    l2.traverse_list()
