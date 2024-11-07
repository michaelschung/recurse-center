# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sameTree(self, tree1, tree2):
        # None trees match by definition
        if tree1 is None and tree2 is None:
            return True
        # Only one None tree means no match
        if tree1 is None or tree2 is None:
            return False
        # Full match requires curr, left, and right
        return tree1.val == tree2.val and \
            self.sameTree(tree1.left, tree2.left) and \
            self.sameTree(tree1.right, tree2.right)

    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # Assuming None tree is subtree by definition
        if subRoot is None:
            return True
        # If main tree ran out then it can't contain subtree
        if root is None:
            return False
        
        # Check if these two subtrees match
        if self.sameTree(root, subRoot):
            return True
        
        # Traverse through main tree, check each subtree to see if it matches
        return self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)