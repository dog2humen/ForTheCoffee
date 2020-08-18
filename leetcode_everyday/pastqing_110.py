# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #return self.isBalanced_v1(root) != -1
        return self.isBalanced_v2(root)

    def isBalanced_v1(self, root: TreeNode) -> bool:
        """dfs recursive"""
        if root is None:
            return 0

        ha = self.isBalanced_v1(root.left)
        if ha == -1:
            return -1
        hb = self.isBalanced_v1(root.right)
        if hb == -1:
            return -1

        if abs(ha - hb) > 1:
            return -1

        return max(ha, hb) + 1

    def isBalanced_v2(self, root: TreeNode) -> bool:
        """
            dfs use stack 
            postorder
        """

        stack, node, res = [], root, False
        last = None
        # 记录节点的高度
        depths = {}
        while stack or node is not None:
            if node:
                stack.append(node)
                node = node.left
            else:
                cur = stack[-1]
                if cur.right and last != cur.right:
                    node = cur.right
                else:
                    tmp = stack.pop()
                    ha, hb = depths.get(tmp.left, 0), depths.get(tmp.right, 0)
                    if abs(ha - hb) > 1:
                        return False
                    depths[tmp] = max(ha, hb) + 1
                    last = cur

        return True

        


