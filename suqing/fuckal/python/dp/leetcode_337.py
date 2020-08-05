# coding:utf8
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        """
        dp_0, dp_1 = self.helper(root)
        return max(dp_0, dp_1)

    def helper(self, node):
        # terminated
        if node is None:
            return (0, 0)
        
        left_0, left_1 = self.helper(node.left)
        right_0, right_1 = self.helper(node.right)

        
        dp_0 = max(left_0, left_1) + max(right_0, right_1) 
        dp_1 = node.val + left_0 + right_0
        return (dp_i_0, dp_i_1)
