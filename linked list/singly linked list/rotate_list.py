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

    def rotate_list(self, rot_cnt):
        cnt, prev, cur = 0, None, self.head
        rot_cnt = rot_cnt % self.find_length(self.head)
        while cnt < rot_cnt:
            prev = cur
            cur = cur.next
            cnt += 1
        while cur.next:
            cur = cur.next
        cur.next = self.head
        self.head = prev.next
        prev.next = None
        return

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
    print('After rotating list')
    linked_list.rotate_list(6)
    linked_list.print_list()
