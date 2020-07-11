# coding:utf8
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
            dp[i][j][k]
            dp[i][0][k] = max(dp[i - 1][0][k], dp[i - 1][1][k] + prices[i])
            dp[i][1][k] = max(dp[i - 1][0][k - 1] - prices[i], dp[i - 1][1][k])
            k = 2
            dp[0][0][0] = 0 第一天不买
            dp[0][1][0] = -inf 第一天不可能卖出

            dp[0][0][1] = -inf 不可能发生
            dp[0][1][1] = -prices[0]

            dp[0][0][2] = 0 买1卖1买1卖1
            dp[0][1][2] = -prices[0] 买一次, 卖一次, 再买一次

        '''
        if not prices:
            return 0

        if k > len(prices) // 2:
            return self.maxWithKinf(prices)
        res = 0
        dp = [[[0 for _ in range(k + 1)]for _ in range(2)] for _ in range(len(prices))]

        for i in range(len(dp)):
            for j in range(1, k + 1):
                if i - 1 == 0:
                    dp[i - 1][0][j] = 0
                    dp[i - 1][1][j] = -prices[0]
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j] + prices[i])
                dp[i][1][j] = max(dp[i - 1][0][j - 1] - prices[i], dp[i - 1][1][j])


        for i in range(k + 1):
            res = max(dp[-1][0][i], res)

        return res


    def maxWithKinf(self, prices: List[int]):
        if not prices:
            return 0

        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(tmp - prices[i], dp_i_1)

        return dp_i_0

if __name__ == '__main__':
    obj = Solution()
    k = 2
    prices = [2, 4, 1]
    prices = [2,1,2,0,1]
    res = obj.maxProfit(k, prices)
    print(res)
