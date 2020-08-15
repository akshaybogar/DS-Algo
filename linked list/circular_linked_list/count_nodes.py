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

    def count_nodes(self):
        cnt = 0
        if not self.last:
            return cnt
        cur = self.last.next
        while cur is not self.last:
            cur = cur.next
            cnt += 1
        return cnt + 1

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
    cl2 = CircularLinkedList()
    cl.traverse_list()
    last_node = cl.insert_empty(1)
    for i in range(2,10):
        last_node = cl.add_node_at_end(i)
    cl.traverse_list()
    print('Number of nodes in linked list {}'.format(cl.count_nodes()))
