# coding:utf8
"""
    538. 把二叉搜索树转换为累加树
    给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
    提醒一下，二叉搜索树满足下列约束条件：
    节点的左子树仅包含键 小于 节点键的节点。
    节点的右子树仅包含键 大于 节点键的节点。
    左右子树也必须是二叉搜索树。

    链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        #return self.convertBST_v1(root)
        return self.convertBST_v2(root)

    def convertBST_v1(self, root: TreeNode) -> TreeNode:
        """
            中序遍历, 先右再左
        """
        self.res = 0
        def helper(root: TreeNode):
            if not root:
                return
            helper(root.right)
            self.res += root.val
            root.val = self.res
            helper(root.left)
        helper(root)
        return root

    def convertBST_v2(self, root: TreeNode) -> TreeNode:
        stack = []
        res = 0
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right

            cur = stack.pop()
            res += cur.val
            cur.val = res
            cur = cur.left

        return root

