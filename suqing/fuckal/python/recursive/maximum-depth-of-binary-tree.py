# coding:utf8
# 104 https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #return self.maxDepth_v1(root)
        #return self.maxDepth_v2(root)
        return self.maxDepth_v3(root)
    def maxDepth_v1(self, root: TreeNode) -> int:
        '''
            dfs 递归
        '''
        if root is None:
            return 0
        leftHeight = self.maxDepth_v1(root.left)
        rightHeight = self.maxDepth_v1(root.right)
        return max(leftHeight, rightHeight) + 1

    def maxDepth_v2(self, root: TreeNode) -> int:
        '''
            dfs 迭代, 层序遍历
        '''
        stack = [root] if root else []
        res = 0
        while stack:
            nextLevel = []
            while stack:
                cur = stack.pop()
                if cur.left:
                    nextLevel.append(cur.left)
                if cur.right:
                    nextLevel.append(cur.right)
            stack = nextLevel
            res += 1
        return res
            

    def maxDepth_v3(self, root: TreeNode) -> int:
        '''
            bfs
        '''
        queue = [root] if root else []
        res = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res += 1
        return res
