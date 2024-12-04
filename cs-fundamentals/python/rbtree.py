"""
Red-black properties:
1. Every node is either red or black
2. The root is black
3. Every leaf (NIL) is black
4. If a node is red, then both its children are black
5. For each node, all simple paths from the node to
   descendant leaves contain the same number of black nodes
"""

class Node:
    def __init__(self, val, is_black):
        self.val = val
        self.is_black = is_black      # True = red, False = black
        self.left = None
        self.right = None
        self.p = None
    
    def __repr__(self):
        return f'Node({self.val})'
    
    def is_leaf(self):
        return self.left is None and self.right is None
    
    def bheight_helper(self, root):
        if root is None:
            return 0
        l_bheight = self.bheight_helper(root.left)
        r_bheight = self.bheight_helper(root.right)
        return max(l_bheight, r_bheight) + int(root.is_black)
    
    def black_height(self):
        b_height = self.bheight_helper(self)
        if self.is_black:
            b_height -= 1
        return b_height
    
class RBTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def black_height(self):
        if self.root is None:
            return 0
        return self.root.black_height()

l1 = Node(17, False)
l1.left = Node(14, True)
l1.right = Node(21, True)
r1 = Node(41, True)
r1.left = Node(30, False)
r1.right = Node(47, True)
root = Node(26, True)
root.left = l1
root.right = r1
print(l1.left.black_height())