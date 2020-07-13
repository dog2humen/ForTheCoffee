# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) <= 0:
            return False

        return self.cursive_create_BST(nums, 0, len(nums)-1)

    def cursive_create_BST(self, nums, left, right):  # 递归参数
        if left > right:  # 定义递归终止条件
            return
        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        # 递归分支
        root.left = self.cursive_create(nums, left, mid-1)
        root.right = self.cursive_create(nums, mid+1, right)
        return root
