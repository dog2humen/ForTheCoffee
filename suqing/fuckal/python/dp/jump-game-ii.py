# coding:utf8
"""
    45. 跳跃游戏 II
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。

    示例:

    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

    链接：https://leetcode-cn.com/problems/jump-game-ii
"""
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        #return self.jump_v1(nums)
        return self.jump_v2(nums)
    def jump_v1(self, nums: List[int]) -> int:
        """
            dp思路, 自顶向下
        """
        size = len(nums)
        memo = [float('INF') for _ in range(size)]

        def dp(nums: List[int], p: int) -> int:
            """
                从p位置跳到最后的最小次数
            """
            if p >= len(nums) - 1:
                return 0
            if memo[p] != float('INF'):
                return memo[p]

            steps = nums[p]
            for i in range(1, steps + 1):
                sub = dp(nums, p + i)
                memo[p] = min(memo[p], sub + 1)

            return memo[p]

        return dp(nums, 0)

    def jump_v2(self, nums: List[int]) -> int:
        """
            贪心: 每次跳覆盖最大的
        """
        size = len(nums)
        res = 0
        max_range, end = 0, 0 # [i....end]最远位置
        for i in range(size - 1):
            max_range = max(nums[i] + i, max_range)
            if end == i:
                res += 1
                end = max_range

        return res

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    obj = Solution()
    print(obj.jump(nums))
