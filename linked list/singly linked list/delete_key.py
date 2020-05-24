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

    # Deletes a node from list given key value
    def delete_key(self, key):
        cur, prev = self.head, None
        if not cur:
            return
        # Check if head is the node that needs to be deleted
        if cur.data == key:
            self.head = cur.next
            cur = None
            return
        # Get the previous node of the node to be deleted
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if not cur:
            return
        prev.next = cur.next
        cur = None
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
    print('Deleting 1..')
    linked_list.delete_key(1)
    print('Deleting 5..')
    linked_list.delete_key(5)
    print('Deleting 3..')
    linked_list.delete_key(3)
    linked_list.print_list()
