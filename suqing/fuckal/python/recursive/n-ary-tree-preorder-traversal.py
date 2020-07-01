# coding:utf8
# 589 https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res
    def helper(self, node, res):
        if node is None:
            return
        res.append(node.val)
        for n in node.children:
            self.helper(n, res)

