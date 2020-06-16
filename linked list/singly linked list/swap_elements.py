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

    def swap_elements(self, x, y):
        if not self.head:
            return
        curx, prevx, cury, prevy = self.head, None, self.head, None
        while curx and curx.data != x:
            prevx = curx
            curx = curx.next

        while cury and cury.data != y:
            prevy = cury
            cury = cury.next

        if not curx:
            print('x not found')
            return

        if not cury:
            print('y not found')
            return

        if not prevx:
            self.head = cury
        else:
            prevx.next = cury

        if not prevy:
            self.head = curx
        else:
            prevy.next = curx

        temp = curx.next
        curx.next = cury.next
        cury.next = temp
        return

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.print_list()
    print('After swapping')
    linked_list.swap_elements(1,4)
    linked_list.print_list()
