# coding:utf8
"""
    最大子序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例 1：
    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
    链接：https://leetcode-cn.com/problems/maximum-subarray
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #return self.maxSubArray_v1(nums)
        return self.maxSubArray_v2(nums)
    def maxSubArray_v1(self, nums: List[int]) -> int:
        """
            dp table
            dp[i]表示以nums[i]为结尾的最大子数组和
        """
        if not nums:
            return 0
        size = len(nums)
        dp = [float('-INF') for _ in range(size)]
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)

    def maxSubArray_v2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp_0 = nums[0]
        dp_1 = 0
        res = dp_0
        for i in range(1, len(nums)):
            dp_1 = max(nums[i], dp_0 + nums[i])
            dp_0 = dp_1
            res = max(res, dp_1)

        return res



if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    obj = Solution()
    print(obj.maxSubArray(nums))
