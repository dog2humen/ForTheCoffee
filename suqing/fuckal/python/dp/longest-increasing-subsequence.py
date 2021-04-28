# coding:utf8
"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #return self.lengthOfLIS_v1(nums)
        return self.lengthOfLIS_v2(nums)
    def lengthOfLIS_v1(self, nums: List[int]) -> int:
        """
            dp table
            dp[i]表示nums[...i]的递增子序列的最长长度
            dp[i]的值要遍历[...i - 1]找小于nums[i]的, 即可构造一个递增子序列
        """

        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS_v2(self, nums: List[int]) -> int:
        """
            二分思路, 模拟牌堆分牌
        """
        top = [0 for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            poker = nums[i]
            left, right = 0, res
            while left < right:
                mid = (left + right) // 2
                if top[mid] < poker:
                    left = mid + 1
                elif top[mid] > poker:
                    right = mid
                else:
                    right = mid

            if left == res:
                res += 1
            top[left] = poker
            print(top)
        return res
if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    obj = Solution()
    print(obj.lengthOfLIS(nums))
