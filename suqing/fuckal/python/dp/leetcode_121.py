# coding:utf8
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
            定义:
                dp[i][j][k] 表示第i天的股票状态为j(持有, 不持有), 可以交易k次的最大利润
                j = 0 不持有, j = 1持有

            状态转移方程:
                买入和卖出作为一次交易, 不能在买入前卖出
                dp[i][0][k] = max(dp[i - 1][0][k], dp[i - 1][1][k] + prices[i])
                dp[i][1][k] = max(dp[i - 1][0][k - 1] - prices[i], dp[i - 1][1][k]) 选择买的时候算做一次交易
                本题中只允许一次交易, k = 1
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1][1] = max(-prices[i], dp[i - 1][1])
            初始化: dp[0][0] = 0, dp[0][1] = -prices[0]
        """
        if not prices:
            return 0

        dp_i_0, dp_i_1 = 0, -prices[0]

        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0
