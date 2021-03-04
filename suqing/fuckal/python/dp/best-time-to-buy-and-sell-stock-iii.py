# coding:utf8
"""
    123. 买卖股票的最佳时机 III
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1:
    输入：prices = [3,3,5,0,0,3,1,4]
    输出：6
    解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
    随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfit_v1(prices)
    def maxProfit_v1(self, prices: List[int]) -> int:
        """
            dp table
            dp[i][k][j] = x 表示第i天, 交易次数为k, 持有股票状态为j的最大利润为x
            其中 j = {0, 1}, 0 <= k <= K
            ans: max(dp[n - 1][k][0])
            每次买入作为一笔交易
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i - 1][k - 1][0] - prices[i], dp[i - 1][k][1])
            base case:
                dp[0][0][0] = 0
                dp[0][1][0] = -inf
                dp[0][0][1] = -inf
                dp[0][1][1] = -prices[0]
        """
        if not prices:
            return 0
        k = 2
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][0] = 0
        dp[0][0][1] = float('-inf')
        dp[0][1][1] = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i], dp[i - 1][j][1])
        return max(dp[-1][1][0], dp[-1][2][0], 0)



if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices = [1, 2, 3, 4, 5]
    obj = Solution()
    print(obj.maxProfit(prices))
