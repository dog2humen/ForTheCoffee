# coding:utf8
# Definition for a binary tree node.

#class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateTrees_v1(n)
    def generateTrees_v1(self, n: int) -> List[TreeNode]:
        '''
            1... k -1 左子树, k + 1...n 右子树
        '''
        res = []
        if not n:
            return res
        res = self.helper(1, n + 1)
        return res

    def helper(self, start, end):
        
        if start == end:
            return [None, ]
    
        # current level
        res = []
        for i in range(start, end):

            left = self.helper(start, i)
            right = self.helper(i + 1, end)

            for lnode in left:
                for rnode in right:
                    root = TreeNode(i, lnode, rnode)
                    res.append(root)

        return res
