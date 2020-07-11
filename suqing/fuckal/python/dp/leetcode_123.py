# coding:utf8
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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

        k = 2
        dp = [[[0 for _ in range(k + 1)]for _ in range(2)] for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][0] = float('-inf')
        dp[0][0][1] = 0
        dp[0][1][1] = -prices[0]
        dp[0][0][2] = 0
        dp[0][1][2] = -prices[0]

        for i in range(1, len(dp)):
            for j in range(1, k + 1):
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j] + prices[i])
                dp[i][1][j] = max(dp[i - 1][0][j - 1] - prices[i], dp[i - 1][1][j])
        
        return max(dp[-1][0][2], dp[-1][0][1], 0)


if __name__ == '__main__':
    obj = Solution()
    prices = [3,3,5,0,0,3,1,4]
    prices = [1,2,3,4,5]
    prices = [1,2,4,2,5,7,2,4,9,0,9]
    res = obj.maxProfit(prices)
    print(res)


