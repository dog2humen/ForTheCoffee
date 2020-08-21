# encoding=utf8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    111. 二叉树的最小深度
        给定一个二叉树，找出其最小深度。

        最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

        说明: 叶子节点是指没有子节点的节点。

        示例:

        给定二叉树 [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回它的最小深度  2.
    """
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.minDepth_v1(root)

    # dfs
    def minDepth_v1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.right:
            return self.minDepth_v1(root.left) + 1
        if not root.left:
            return self.minDepth_v1(root.right) + 1

        return min(self.minDepth_v1(root.left), self.minDepth_v1(root.right)) + 1

    # bfs
    def minDepth_v2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        import collections
        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0

