# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        val = ''
        val_list = []
        
        if root.val == None:
            return 

        if root.val != None:
            val += str(root.val)
            





print(Solution().sumNumbers([1,2,3]))
        