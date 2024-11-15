class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.val)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        result = '['
        curr = self.head
        while curr is not None:
            result += str(curr)
            if curr.next is not None:
                result += ', '
            curr = curr.next
        result += ']'
        return result
    
    def append(self, val):
        new_node = Node(val)
        # Empty list
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

dll = DoublyLinkedList()
dll.append(1)
dll.append(5)
print(dll)