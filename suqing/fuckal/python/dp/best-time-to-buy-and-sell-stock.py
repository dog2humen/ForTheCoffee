# coding:utf8
"""
    121. 买卖股票的最佳时机
    给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
    你只能选择某一天买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
    设计一个算法来计算你所能获取的最大利润。
    返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
    示例 1：
    输入：[7,1,5,3,6,4]
    输出：5
    解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfit_v1(prices)

    def maxProfit_v1(self, prices: List[int]) -> int:
        """
            dp table
            定义dp[i][j] = x 表示第i天持有状态为j(j = {0, 1})的最大利润为x
            ans: dp[n - 1][0]
            状态转移方程:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(-prices[i], dp[i - 1][1])
            base case:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
        """
        if not prices:
            return 0

        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        
        return dp_i_0

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    obj = Solution()
    print(obj.maxProfit(prices))


