# coding:utf-8
# https://leetcode-cn.com/problems/invert-binary-tree/description/

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.invertTree_v1(root)
        #return self.invertTree_v2(root)
    def invertTree_v1(self, root: TreeNode) -> TreeNode:
        '''
            翻转二叉树
            子问题: 翻转左子树和右子树
        '''
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree_v1(root.left)
            self.invertTree_v1(root.right)
        return root



    def invertTree_v2(self, root: TreeNode) -> TreeNode:
        '''
            dfs迭代
        '''
        stack = [root] if root else []
        while stack:
            cur = stack.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                stack.append(cur.left)
                stack.append(cur.right)

        return root

