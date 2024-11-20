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
        self.size = 0

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
    
    def __len__(self):
        return self.size
    
    # Handles negative indexes!
    def __getitem__(self, key):
        return self.get(abs(key), key < 0)
    
    def append(self, val):
        self.size += 1
        new_node = Node(val)
        # Empty list
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # Deletes node with given val. Returns True if success, False otherwise
    def delete(self, val):
        # Empty list
        if not self.head:
            return False
        curr = self.head
        while curr is not None:
            if curr.val == val:
                # Head node
                if not curr.prev:
                    self.head = curr.next
                else:
                    curr.prev.next = curr.next
                # Tail node
                if not curr.next:
                    self.tail = curr.prev
                else:
                    curr.next.prev = curr.prev
                self.size -= 1
                return True
            curr = curr.next
        return False
    
    # Returns val at index i, or raises IndexError
    def get(self, i, neg_index):
        curr = self.tail if neg_index else self.head
        print('CURR:', curr)
        count = 1 if neg_index else 0
        while curr is not None:
            if count == i:
                return curr.val
            curr = curr.prev if neg_index else curr.next
            count += 1
        raise IndexError('Index out of bounds')

    # Inserts given val at given index
    def insert(self, i, val):
        pass

dll = DoublyLinkedList()
dll.append(1)
dll.append(5)
dll.append(4)
print(dll[0])
print(dll)
print(len(dll))