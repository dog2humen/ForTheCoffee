# coding:utf8
# 111 https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #return self.minDepth_v1(root)
        return self.minDepth_v2(root)
    def minDepth_v1(self, root: TreeNode) -> int:
        '''
            dfs 递归
        '''
        if not root:
            return 0
        if not root.left:
            return self.minDepth_v1(root.right) + 1
        if not root.right:
            return self.minDepth_v1(root.left) + 1

        return min(self.minDepth_v1(root.left), self.minDepth_v1(root.right)) + 1

    def minDepth_v2(self, root: TreeNode) -> int:
        '''
            bfs
        '''
        queue = [root] if root else []
        res = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    return res + 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res += 1
        return res
