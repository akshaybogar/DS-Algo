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

    def delete_key(self, key):
        if not self.last:
            return
        prev, cur = self.last, self.last.next
        while cur.data != key and cur is not self.last:
            prev = cur
            cur = cur.next
        if cur is not self.last:
            prev.next = cur.next
        else:
            prev.next = cur.next
            self.last = prev
        return

if __name__ == '__main__':
    cl = CircularLinkedList()
    cl.traverse_list()
    last_node = cl.insert_empty(1)
    for i in range(2,6):
        last_node = cl.add_node_at_end(i)
    print('Original list')
    cl.traverse_list()
    cl.delete_key(4)
    cl.traverse_list()
