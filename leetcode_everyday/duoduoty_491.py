# encoding=utf8
"""
491. 递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""
import copy
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.findSubsequences_v1(nums)

    def findSubsequences_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)

        def dfs(start, path):
            if len(path) > 1 and path not in res:
                res.append(copy.copy(path))


            for i in range(start, length):
                if len(path) == 0 or path[-1] <= nums[i]:
                    path.append(nums[i])
                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return res




if __name__ == '__main__':

    s = Solution()
    print s.findSubsequences([4, 6, 7, 7])
    # a = [1]
    # a.append(2)
    # print a
    # a.pop()
    # print a

