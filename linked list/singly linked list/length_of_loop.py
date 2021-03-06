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

    def create_loop(self):
        if not self.head:
            return
        # Make sure the the linked list contains atleast 5 elements
        #self.head.next.next.next.next.next = self.head.next
        return

    def detect_loop(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def length_of_loop(self):
        ref = self.detect_loop()
        if not ref:
            return 0
        mov, cnt  = ref.next, 1
        while mov.next != ref:
            cnt += 1
            mov = mov.next
        return cnt

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(5)
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.create_loop()
    print(linked_list.length_of_loop())
