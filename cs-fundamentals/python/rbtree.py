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
    
    def height_helper(self, root):
        if root is None:
            return 0
        l_height = self.height_helper(root.left)
        r_height = self.height_helper(root.right)
        return max(l_height, r_height) + 1

    def height(self):
        return self.height_helper(self.root)

    # Works ONLY if tree is already established with some depth before inserting violation
    def insert_fixup(self, root):
        while not root.p.is_black:
            if root.p == root.p.p.left:
                uncle = root.p.p.right
                if not uncle.is_black:
                    root.p.is_black = True
                    uncle.is_black = True
                    root.p.p.is_black = False
                    root = root.p.p
                elif root == root.p.right:
                    root = root.p
                    self.l_rotate(root)
                else:
                    root.p.is_black = True
                    root.p.p.is_black = False
                    self.r_rotate(root.p.p)
            else:
                uncle = root.p.p.left
                if not uncle.is_black:
                    root.p.is_black = True
                    uncle.is_black = True
                    root.p.p.is_black = False
                    root = root.p.p
                elif root == root.p.left:
                    root = root.p
                    self.r_rotate(root)
                else:
                    root.p.is_black = True
                    root.p.p.is_black = False
                    self.l_rotate(root.p.p)
        self.root.is_black = True


    def insert_helper(self, root, p, node):
        if root is None:
            node.p = p
            return node
        if node.val < root.val:
            root.left = self.insert_helper(root.left, root, node)
        else:
            root.right = self.insert_helper(root.right, root, node)
        return root

    def insert(self, val):
        if self.root is None:
            self.root = Node(val, True)
        else:
            new_node = Node(val, False)
            self.root = self.insert_helper(self.root, None, new_node)
            self.insert_fixup(new_node)

    def l_rotate(self, root):
        r_child = root.right
        root.right = r_child.left
        if r_child.left is not None:
            r_child.left.p = root
        r_child.p = root.p
        if root.p is None:
            self.root = r_child
        elif root == root.p.left:
            root.p.left = r_child
        else:
            root.p.right = r_child
        r_child.left = root
        root.p = r_child

    def r_rotate(self, root):
        l_child = root.left
        root.left = l_child.right
        if l_child.right is not None:
            l_child.right.p = root
        l_child.p = root.p
        if root.p is None:
            self.root = l_child
        elif root == root.p.right:
            root.p.right = l_child
        else:
            root.p.left = l_child
        l_child.right = root
        root.p = l_child

tree = RBTree()
tree.root = Node(11, True, None)
tree.root.left = Node(2, False, tree.root)
tree.root.left.left = Node(1, True, tree.root.left)
tree.root.left.right = Node(7, True, tree.root.left)
tree.root.left.right.left = Node(5, False, tree.root.left.right)
tree.root.left.right.right = Node(8, False, tree.root.left.right)
tree.root.right = Node(14, True, tree.root)
tree.root.right.right = Node(15, False, tree.root.right)
tree.insert(4)
print(tree.verbose())