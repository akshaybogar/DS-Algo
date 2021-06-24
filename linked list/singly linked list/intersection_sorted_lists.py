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

    def intersect_sorted_lists(self, h1, h2):
        temp = Node(0)
        res = temp
        while h1 and h2:
            if h1.data == h2.data:
                temp.next = Node(h1.data)
                temp = temp.next
                h1 = h1.next
                h2 = h2.next
            elif h1.data < h2.data:
                h1 = h1.next
            else:
                h2 = h2.next
        return res.next

    def intersect_sorted_lists_rec(self, h1, h2):
        if not h1 or not h2:
            return None
        if h1.data < h2.data:
            return self.intersect_sorted_lists_rec(h1.next, h2)
        if h2.data < h1.data:
            return self.intersect_sorted_lists_rec(h1, h2.next)
        temp = Node(h1.data)
        temp.next = self.intersect_sorted_lists_rec(h1.next, h2.next)
        return temp

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(4)
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    ll2 = LinkedList()
    ll2.push(3)
    ll2.push(2)
    ll3 = LinkedList()
    ll3.head = ll3.intersect_sorted_lists_rec(linked_list.head, ll2.head)
    ll3.print_list()