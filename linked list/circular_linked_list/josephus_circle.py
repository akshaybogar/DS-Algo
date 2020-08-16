class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

def josephus_circle(skip_size, size):
    cl = CircularLinkedList()
    cl.head = Node(1)
    node = cl.head
    for i in range(2, size+1):
        node.next = Node(i)
        node = node.next
    node.next = cl.head
    prev_node, node = cl.head, cl.head
    while node.next is not node:
        cnt = 1
        while cnt < skip_size:
            prev_node = node
            node = node.next
            cnt += 1
        prev_node.next = node.next
        node = prev_node.next
    print('Last man', node.data)

if __name__ == '__main__':
    josephus_circle(3, 5)
