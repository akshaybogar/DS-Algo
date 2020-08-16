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
        return self.last

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

    def interchange_last_first_nodes(self):
        if not self.last or not self.last.next:
            return
        sec_last = self.last.next
        while sec_last.next is not self.last:
            sec_last = sec_last.next
        if sec_last is self.last.next:
            self.last = self.last.next
            return
        sec_last.next = self.last.next
        self.last.next = self.last.next.next
        sec_last.next.next = self.last
        self.last = sec_last.next
        return

if __name__ == '__main__':
    cl = CircularLinkedList()
    last_node = cl.insert_empty(1)
    for i in range(2, 4):
        last_node = cl.add_node_at_end(i)
    print('Original list')
    cl.traverse_list()
    print('After interchanging first and last nodes')
    cl.interchange_last_first_nodes()
    cl.traverse_list()
