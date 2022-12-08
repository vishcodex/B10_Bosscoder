# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, it is symmetric
        if not root:
            return True
        
        # Check if the left and right subtrees are symmetric
        return self.isSymmetricHelper(root.left, root.right)
        
    def isSymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        # If both subtrees are empty, they are symmetric
        if not left and not right:
            return True
        
        # If one subtree is empty and the other is not, they are not symmetric
        if not left or not right:
            return False
        
        # If the values of the root nodes are not equal, the subtrees are not symmetric
        if left.val != right.val:
            return False
        
        # Recursively check if the left subtree of the left node is symmetric
        # with the right subtree of the right node, and if the right subtree
        # of the left node is symmetric with the left subtree of the right node
        return (self.isSymmetricHelper(left.left, right.right) and
                self.isSymmetricHelper(left.right, right.left))