# coding:utf8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        return self.flatten_v1(root)
    def flatten_v1(self, root: TreeNode) -> None:
        '''
            递归
            后序遍历, 头插法构造链表
        '''
        self.root = None
        self.helper(root)

    def helper(self, node):
        if node:
            self.helper(node.right)
            self.helper(node.left)

            node.right = self.root
            node.left = None
            self.root = node

