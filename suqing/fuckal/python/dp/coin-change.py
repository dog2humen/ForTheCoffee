# coding:utf8
from typing import List

"""
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
    你可以认为每种硬币的数量是无限的。
    链接：https://leetcode-cn.com/problems/coin-change
    输入：coins = [1, 2, 5], amount = 11
    输出：3 
    解释：11 = 5 + 5 + 1
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #return self.coinChange_v1(coins, amount)
        return self.coinChange_v2(coins, amount)
    
    def coinChange_v1(self, coins: List[int], amount: int) -> int:
        """
            dp
            dp[n] 表示amount = n 的最少的硬币个数
            转态转移方程
            dp[n] = {
                0, n == 0  
                -1 n < 0
                min(dp[amount - n] + 1, dp[n])
            }
        """
        if amount < 0:
            return -1
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i - coin] + 1, dp[i])

        return -1 if dp[amount] == amount + 1 else dp[amount]

    def coinChange_v2(self, coins: List[int], amount: int) -> int:

        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for coin in coins:
                cur = helper(n - coin)
                if cur == -1: continue
                res = min(res, cur + 1)
            
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return helper(amount)
            


if __name__ == '__main__':
    coins, amount = [1, 2, 5], 11
    obj = Solution()
    print(obj.coinChange(coins, amount))
