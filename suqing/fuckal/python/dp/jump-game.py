# coding:utf8
"""
    55. 跳跃游戏
    给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个下标。

    示例 1：
    输入：nums = [2,3,1,1,4]
    输出：true
    解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

    示例 2：
    输入：nums = [3,2,1,0,4]
    输出：false
    解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

    链接：https://leetcode-cn.com/problems/jump-game
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #return self.canJump_v1(nums)
        return self.canJump_v2(nums)
    def canJump_v1(self, nums: List[int]) -> bool:
        """
            dp table
            定义: dp[i]表示nums[...i] 是否可以跳到i位置(False/True)
            [....i - 1] 能否跳到[...i]
        """

        if not nums:
            return False
        size = len(nums)
        dp = [False for _ in range(size)]
        dp[0] = True
        for i in range(1, size):
            for j in range(i):
                # 之前的j可到达, 并且可以跳到i位置
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break

        return dp[size - 1]

    def canJump_v2(self, nums: List[int]) -> bool:
        """
            贪心
            1.每一步都计算最远能跳到的位置cur_max
            2. 和全局的最大作对比
        """
        res = 0
        size = len(nums)
        for i in range(size - 1):
            res = max(res, nums[i] + i)
            if res <= i:
                return False
        return res >= size - 1

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    obj = Solution()
    print(obj.canJump(nums))
