# coding:utf8

from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
            dp[i][j][k]
            每笔交易有手续费, 买入算一次交易
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][0] - prices[i] -fee, dp[i - 1][1])
            dp[0][0] = 0
            dp[0][1] = -prices[0] - fee
        '''

        if not prices:
            return 0
        dp_i_0, dp_i_1 = 0, -prices[0] - fee

        for i in range(1, len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(tmp - prices[i] - fee, dp_i_1)

        return dp_i_0
