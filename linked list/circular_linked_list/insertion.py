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

    def add_node_at_start(self, data):
        if not self.last:
            return None
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        return self.last

    def add_node_after_node(self, data, item):
        if not self.last:
            return None
        temp = Node(data)
        p = self.last.next
        while p:
            if p.data == item:
                temp.next = p.next
                p.next = temp
                if p == self.last:
                    self.last = temp
                return self.last
            p = p.next
            if p == self.last.next:
                print('Node with data {} not found'.format(item))
                return None

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
    cl.traverse_list()
    last_node = cl.insert_empty(1)
    cl.traverse_list()
    last_node = cl.add_node_at_end(2)
    cl.traverse_list()
    last_node = cl.add_node_at_start(0)
    cl.traverse_list()
    cl.add_node_after_node(3, 2)
    cl.traverse_list()
