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

    def find_length(self, node):
        if not node:
            return 0
        return 1 + self.find_length(node.next)

    def intersection_point(self, head1, head2):
        cnt = 0
        l1 = self.find_length(head1)
        l2 = self.find_length(head2)
        if l1 >= l2:
            node1 = head1
        else:
            node1 = head2

        while cnt < (l1 - l2):
            node1 = node1.next
            cnt += 1
        while node1 and head2:
            if node1 == head2:
                return node1.data
            node1 = node1.next
            head2 = head2.next
        return -1

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(5)
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list2 = LinkedList()
    linked_list2.push(10)
    linked_list2.head.next = linked_list.head.next
    ll = LinkedList()
    print('Intersection point',
          ll.intersection_point(linked_list.head, linked_list2.head))
