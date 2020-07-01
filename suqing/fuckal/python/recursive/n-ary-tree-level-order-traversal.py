# coding:utf8
# 429 https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
            dfs
        '''
        queue = [root] if root else []
        res = []
        while queue:
            
            level = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur:
                    level.append(cur.val)
                for n in cur.children:
                    queue.append(n)
            res.append(level)
        return res


