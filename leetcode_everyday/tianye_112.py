# encoding=utf8
"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 得到路径个数
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    # 得到全部路径
    def has_all_path_sum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res_list = []
        tmp_list = []
        return self.recursive_get_all_path(root, sum, tmp_list, res_list)

    def recursive_get_all_path(self, root, sum, tmp_list, res_list):
        if not root:
            return False
        sum -= root.val
        tmp_list.append(root.val)
        if sum == 0 and not root.left and not root.right:
            """
            值得注意的是：
            记录路径时若直接执行 res.append(path) ，
            则是将 path 对象加入了 res ；
            后续 path 改变时， res 中的 path 对象也会随之改变。

            正确做法：
            res.append(list(path)) ，相当于复制了一个 path 并加入到 res
            """
            res_list.append(list(tmp_list))

        self.recursive_get_all_path(root.left, sum, tmp_list, res_list)
        self.recursive_get_all_path(root.right, sum, tmp_list, res_list)
        tmp_list.pop()

        return res_list


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    s = Solution()
    #print s.has_all_path_sum(a, 4)
    a=[1,2,3]
    b = []
    b.append(a)
    b.append(a)
    print b
