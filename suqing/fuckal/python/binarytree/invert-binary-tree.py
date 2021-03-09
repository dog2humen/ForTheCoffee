# coding:utf8
"""
    226. 翻转二叉树
    翻转一棵二叉树。

    示例：
    输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #return self.invertTree_v1(root)
        return self.invertTree_v2(root)
    def invertTree_v1(self, root: TreeNode) -> TreeNode:
        """
            递归:前序遍历
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree_v1(root.left)
        self.invertTree_v1(root.right)
        return root

    def invertTree_v2(self, root: TreeNode) -> TreeNode:
        """
            迭代dfs, 利用栈
        """
        stack = [root] if root else []
        while stack:
            cur = stack.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                stack.append(cur.left)
                stack.append(cur.right)

        return root

