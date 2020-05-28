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

    def find_nth_node(self, node, n, cnt=0):
        if not node:
            return None
        elif cnt == n:
            return node
        else:
            return self.find_nth_node(node.next, n, cnt+1)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    node = linked_list.find_nth_node(linked_list.head, 3)
    if node:
        print(node.data)
    else:
        print('Not found')
