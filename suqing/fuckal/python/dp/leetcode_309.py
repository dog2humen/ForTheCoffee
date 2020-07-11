# coding:utf8
from typing import List
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        '''
            典型dp问题
            状态定义:
                dp[i][k][j] 表示第i天股票的股票状态为j(持有, 不持有), 可以交易k次的最大利润
                j -> (0, 1) 0 => 不持有, 1 => 持有

            状态转移方程:
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                本题中可以交易任意次数, 即k 与k - 1相同, 不需要关注k这个状态
                本题中每次卖后有冷冻期, 则i的状态不能由i - 1转移过来, 要从 i - 2转移过来
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]) i - 1天卖
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            初始化:
                dp[0][0] = 0

        '''
        
        if len(prices) <= 1:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]

        dp[0][0], dp[0][1] = 0, -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][0] - prices[1], dp[0][1]) 

        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[-1][0]

        


if __name__ == '__main__':
    obj = Solution()
    prices = [2, 1, 4]
    res = obj.maxProfit(prices)
    print(res)

