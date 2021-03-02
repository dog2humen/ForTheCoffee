# coding:utf8
"""
    312. 戳气球
    有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
    这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
    求所能获得硬币的最大数量。
    示例 1：
    输入：nums = [3,1,5,8]
    输出：167
    解释：
    nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
    链接：https://leetcode-cn.com/problems/burst-balloons
"""
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return self.maxCoins_v1(nums)

    def maxCoins_v1(self, nums: List[int]) -> int:
        """
            dp table
            定义dp[i][j] = x 表示戳破(i, j)开区间中的所有气球, 可以获得最高分为x
            结果为dp[0][n + 1], n = len(nums)
            转移方程:
                k为最后一个戳破的气球, 则:
                穷举k, i < k < j
                dp[i][j] = dp[i][k] + dp[k][j] + nums[i] * nums[k] + nums[j]
            base case:
                j <= i + 1, dp[i][j] = 0

            因最终结果是dp[0][n + 1], 最右上角, 故从下往上, 从左往右遍历
        """

        size = len(nums)
        dp = [[0] * (size + 2) for _ in range(size + 2)]
        points = [1]
        points.extend(nums)
        points.append(1)

        for i in range(size, -1, -1):
            for j in range(i + 1, size + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], 
                                   dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])

        return dp[0][size + 1]

if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    obj = Solution()
    print(obj.maxCoins(nums))
