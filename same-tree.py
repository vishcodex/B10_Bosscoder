# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty, they are the same
        if not p and not q:
            return True
        
        # If one tree is empty and the other is not, they are not the same
        if not p or not q:
            return False
        
        # If the values of the root nodes are not equal, the trees are not the same
        if p.val != q.val:
            return False
        
        # Recursively check if the left subtree of p is the same as the left subtree of q
        # and if the right subtree of p is the same as the right subtree of q
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        