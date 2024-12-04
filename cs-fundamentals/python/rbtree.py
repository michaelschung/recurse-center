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
    def __init__(self, val, is_black, p=None):
        self.val = val
        self.is_black = is_black      # True = red, False = black
        self.left = None
        self.right = None
        self.p = p
    
    def __repr__(self):
        return f'{self.val}'
    
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

    def repr_helper(self, root, verbose=False):
        if root is None:
            return ''
        l_str = self.repr_helper(root.left, verbose)
        r_str = self.repr_helper(root.right, verbose)
        if verbose:
            c_str = f'Node(val: {root.val}, color: {'black' if root.is_black else 'red'}, parent: {root.p})\n'
        else:
            c_str = f'{root} '
        return l_str + c_str + r_str

    def __repr__(self):
        return self.repr_helper(self.root)
    
    def verbose(self):
        return self.repr_helper(self.root, True)

    def black_height(self):
        if self.root is None:
            return 0
        return self.root.black_height()

    def insert_fixup(self):
        pass

    def insert_helper(self, root, p, val):
        if root is None:
            return Node(val, False, p)
        if val < root.val:
            root.left = self.insert_helper(root.left, root, val)
        else:
            root.right = self.insert_helper(root.right, root, val)
        return root

    def insert(self, val):
        if self.root is None:
            self.root = Node(val, True)
        else:
            self.root = self.insert_helper(self.root, None, val)
        self.insert_fixup()

tree = RBTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(6)
print(tree.verbose())