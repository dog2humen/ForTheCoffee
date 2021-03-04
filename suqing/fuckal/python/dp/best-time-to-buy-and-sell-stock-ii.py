# coding:utf8
"""
    122. 买卖股票的最佳时机 II
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1:

    输入: [7,1,5,3,6,4]
    输出: 7
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfit_v1(prices)
    def maxProfit_v1(self, prices: List[int]) -> int:
        """
            dp table
            dp[i][j] = x 表示第i天持有状态为j时的最大利润为x
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
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
    prices = [7, 1, 5, 3, 6, 4]
    obj = Solution()
    print(obj.maxProfit(prices))
