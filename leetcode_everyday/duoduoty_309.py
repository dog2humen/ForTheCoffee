# encoding=utf8
class Solution(object):
    """
    121. 买卖股票的最佳时机
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。
    """
    def maxProfit_121(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(len(prices))[1:]:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], - prices[i])
        return dp[-1][0]

    def maxProfit_121_less_cache(self, prices):
        if not prices:
            return 0

        dp_i_0 = 0
        dp_i_1 = - prices[0]
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

    """
    122. 买卖股票的最佳时机 II
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """
    def maxProfit_122(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[-1][0] = 0
        dp[-1][1] = - prices[0]
        for i in range(len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]

    def maxProfit_122_less_cache(self, prices):
        if not prices:
            return 0
        dp_i_0 = 0
        dp_i_1 = - 2**32
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0

    """
    123. 买卖股票的最佳时机 III
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """
    def maxProfit_123(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k_max = 2
        dp = [[[0]*2 for _ in range(3)] for _ in range(len(prices))]

        for i in range(len(prices)):
            for k in range(3)[-1:0:-1]:
                if i - 1 == -1:
                    dp[i-1][k][0] = 0
                    dp[i-1][k][1] = - prices[0]
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return max(dp[-1][1][0],dp[-1][2][0])

    """
    188. 买卖股票的最佳时机 IV
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0 or not prices:
            return 0
        # 存在内存超限问题，问题变为 k 无限制， 即 maxProfit_k_inf
        if k > len(prices) // 2:
            return self.maxProfit_k_inf(prices)
        
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices))]

        for i in range(len(prices)):
            for j in range(k + 1)[-1:0:-1]:
                if i - 1 == -1:
                    dp[i - 1][j][0] = 0
                    dp[i - 1][j][1] = - prices[0]
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        res = 0
        for i in range(k + 1):
            res = max(res, dp[-1][k][0])
        return res

    def maxProfit_k_inf(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp_i_0 = 0
        dp_i_1 = - 2 ** 32
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0

    """
    309. 最佳买卖股票时机含冷冻期
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
        1、你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        2、卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    """
    def maxProfit_309(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <=1:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[-1][0] = 0
        dp[-2][0] = 0
        dp[-1][1] = - 2**32
        for i in range(len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[-1][0]

    """
    714. 买卖股票的最佳时机含手续费
    给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
    你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
    返回获得利润的最大值。
    注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
    """
    def maxProfit_714(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[-1][0] = 0
        dp[-1][1] = - 2**32
        for i in range(len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]



if __name__ == '__main__':
    s = Solution()
    print s.maxProfit_123([3,3,5,0,0,3,1,4])
    print s.maxProfit_123([1,2,3,4,5])
    print s.maxProfit_188(2,[2,4,1])
