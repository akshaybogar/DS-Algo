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

    # Inserts node after a given node(prev)
    def insert(self, prev, data):
        if not prev:
            return 'Previous node cannot be null'
        node = Node(data)
        node.next = prev.next
        prev.next = node
        return

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

    def delete_duplicates(self):
        if not self.head:
            return
        prev, nxt = self.head, self.head.next
        while nxt:
            if prev.data == nxt.data:
                prev.next = nxt.next
                nxt = None
                nxt = prev.next
            else:
                prev = prev.next
                nxt = nxt.next
        return

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(5)
    linked_list.push(5)
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.push(1)
    print('Initial list')
    linked_list.print_list()
    linked_list.delete_duplicates()
    print('After removing duplicates')
    linked_list.print_list()
