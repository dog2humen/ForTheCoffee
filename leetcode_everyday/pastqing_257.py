# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #return self.binaryTreePaths_v1(root)
        return self.binaryTreePaths_v2(root)
        
    def binaryTreePaths_v1(self, root: TreeNode) -> List[str]:
        res = []
        self.bfs(root, [], res)
        return res

    def dfs(self, node, cur, res):
        
        if node is None:
            return
        if node.left is None and node.right is None:
            cur.append(str(node.val))
            res.append('->'.join(cur))
            return
        
        self.bfs(node.left, cur + [str(node.val)], res)
        self.bfs(node.right, cur + [str(node.val)], res)

    
    def binaryTreePaths_v2(self, root: TreeNode) -> List[str]:
        return self.bfs(root, res)
    def bfs(self, node, res):
        queue = [(node, '')] if node else []
        res = []
        while queue:
            cur, last = queue.pop(0)
            if cur.left is None and cur.right is None:
                res.append(last + str(cur.val))
            if cur.left:
                queue.append((cur.left, last + str(cur.val) + '->'))
            if cur.right:
                queue.append((cur.right, last + str(cur.val) + '->'))
            
        return res
