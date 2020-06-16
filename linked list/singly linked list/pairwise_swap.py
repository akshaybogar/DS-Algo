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

    #Utility method to print list
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def pairwise_swap(self):
        cur = self.head
        while cur and cur.next:
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next
        return

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.push(0)
    linked_list.print_list()
    print('After pairwise swapping')
    linked_list.pairwise_swap()
    linked_list.print_list()
