# coding:utf8
from typing import List
from collections import Counter
"""
    给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
    假设每一种面额的硬币有无限个。 

    示例 1:
    输入: amount = 5, coins = [1, 2, 5]
    输出: 4
    解释: 有四种方式可以凑成总金额:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    链接：https://leetcode-cn.com/problems/coin-change-2
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #return self.change_v1(amount, coins)
        return self.change_v2(amount, coins)

    def change_v1(self, amount: int, coins: List[int]) -> int:
        """
            完全背包
            dp table
            定义: dp[i][j]表示前i个coins 金额为j时的组合数
            第i个用或者不用
            dp[i][j] = dp[i - 1][j - coins[i - 1]] + dp[i - 1][j]
            base case:
                dp[0][j] = 0
                dp[i][0] = 1
	"""

        size = len(coins)
        dp = [[0] * (amount + 1) for _ in range(size + 1)]

        for i in range(size + 1):
            dp[i][0] = 1

        for i in range(1, size + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[size][amount]

    def change_v2(self, amount: int, coins: List[int]) -> int:
        """
            状态压缩
        """
        size = len(coins)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for i in range(size):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j - coins[i]] + dp[j]
        return dp[amount]




if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    obj = Solution()
    print(obj.change(amount, coins))
