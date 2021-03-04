# coding:utf8
"""
    188. 买卖股票的最佳时机 IV
    给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    示例 1：
    输入：k = 2, prices = [2,4,1]
    输出：2
    解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.maxProfit_v1(k, prices)

    def maxProfit_v1(self, k: int, prices: List[int]) -> int:
        """
            dp table
            定义dp[i][k][j] = x 表示第i天交易k次是否持有股票状态下的最大利润
            j = 1 -> 持有, j = 0 不持有
            一次交易由买入和卖出构成, 至少需要两天, k应该小于n/2, 如果超过, 相当于k = inf
            ans:
                max(dp[n - 1][k][0])
            转移方程:
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
            base case:
                
        """
        if k > len(prices) // 2:
            return self.maxWithKinf(prices)

        res = 0
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices))]
        
        for i in range(len(prices)):
            for j in range(1, k + 1):
                if i - 1 == 0:
                    dp[i - 1][j][0] = 0
                    dp[i - 1][j][1] = -prices[0]
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i], dp[i - 1][j][1])

        for i in range(k + 1):
            res = max(res, dp[-1][i][0])

        return res

        

    def maxWithKinf(self, prices: List[int]):
        """
            dp table
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            ans: dp[i - 1][0]
            base case:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
                
        """

        if not prices:
            return 0
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(tmp - prices[i], dp_i_1)

        return dp_i_0


if __name__ == '__main__':
    k = 2
    prices = [2, 4, 1]
    obj = Solution()
    print(obj.maxProfit(k, prices))
