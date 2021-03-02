# coding:utf8
"""
    分割等和子集
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    注意:
    每个数组中的元素不会超过 100
    数组的大小不会超过 200
    示例 1:
    输入: [1, 5, 11, 5]
    输出: true
    解释: 数组可以分割成 [1, 5, 5] 和 [11].
    链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
"""
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #return self.canPartition_v1(nums)
        return self.canPartition_v2(nums)
    def canPartition_v1(self, nums: List[int]) -> bool:
        """
            背包问题
            转化为容量为sum(nums) // 2的背包, 装nums的物品, 是否能装满
            定义: dp[i][j] 对于前i个物品, 当前容量为j, 是否能装满
            结果: dp[N][sum/2]
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            base case
            dp[i][0] = true
        """
        total = sum(nums)

        # 奇数不可能
        if total % 2 != 0:
            return False
        
        size = len(nums)
        total = total // 2
        dp = [[False] * (total + 1) for _ in range(size + 1)]

        for i in range(size + 1):
            dp[i][0] = True

        for i in range(1, size + 1):
            for j in range(1, total + 1):
                if j - nums[i - 1] < 0: # 背包容量不足
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]

        return dp[size][total]

    def canPartition_v2(self, nums: List[int]) -> bool:
        """
            状态压缩
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        total = total // 2
        size = len(nums)
        dp = [False for _ in range(total + 1)]
        dp[0] = True
        for i in range(size):
            for j in range(total, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j - nums[i]] or dp[j]

        return dp[total]

if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    obj = Solution()
    print(obj.canPartition(nums))

