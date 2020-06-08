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

    def reverse_in_groups(self, head, k):
        cnt, prev, cur, next_node = 0, None, head, None
        while cur and cnt < k:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            cnt += 1
        if next_node:
            head.next = self.reverse_in_groups(next_node, k)
        return prev

    #Utility method to print list
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(5)
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.print_list()
    print('After reversing list')
    linked_list.head = linked_list.reverse_in_groups(linked_list.head, 4)
    linked_list.print_list()
