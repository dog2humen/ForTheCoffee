# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #return self.maxDepth_v1(root)
        return self.maxDepth_v2(root)
    def maxDepth_v1(self, root: TreeNode) -> int:
        '''
            递归
        '''
        if not root:
            return 0
        return max(self.maxDepth_v1(root.left), self.maxDepth_v1(root.right)) + 1

    def maxDepth_v2(self, root: TreeNode) -> int:
        '''
            bfs
        '''
        queue = [root] if root else []
        res = 0
        while queue:
            for _ in range(len(queue)):
                curNode = queue.pop(0)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res += 1


        return res

