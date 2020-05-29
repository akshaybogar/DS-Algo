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

    def nth_node_from_end(self, n):
        if not self.head:
            return
        slow, fast = self.head, self.head
        while n-1 > 0 and fast:
            fast = fast.next
            n = n - 1
        if not fast:
            return None
        while fast.next:
            slow = slow.next
            fast = fast.next
        print(slow.data)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.nth_node_from_end(5)
