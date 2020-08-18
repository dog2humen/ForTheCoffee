# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #return self.postorderTraversal_v1(root)
        return self.postorderTraversal_v2(root)
    def postorderTraversal_v1(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
            
    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            self.helper(node.right, res)
            res.append(node.val)

    def postorderTraversal_v2(self, root: TreeNode) -> List[int]:
        """dfs use stack"""
        stack, node, res = [], root, []
        last = None

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                cur = stack[-1]
                if cur.right and last != cur.right:
                    node = cur.right
                else:
                    res.append(cur.val)
                    last = cur
                    stack.pop()
            

        return res
                


    
