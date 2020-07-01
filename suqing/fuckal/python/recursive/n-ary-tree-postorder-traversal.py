# coding:utf8
# 590 https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res
    def helper(self, node, res):
        if node is None:
            return 
        for n in node.children:
            self.helper(n, res)
        res.append(node.val)
