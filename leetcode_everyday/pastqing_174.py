# coding:utf8
from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        return self.calculateMinimumHP_v1(dungeon)
    def calculateMinimumHP_v1(self, dungeon: List[List[int]]) -> int:
        '''
            dp[i][j] 表示在第[i, j]位置的要用的最低血量
            dp的初始化为(m + 1) * (n + 1)
            推导如下:
            -2  -3  +3             7   5   2  inf 
            -5  -10 +1       ->    6   11  5  inf
            +10 +30 -5             1   1   6  1
                                   inf inf 1  #
            自底向上
            状态转移方程:
                计算, dp[i+1][j] - dungeon[i][j] 与 dp[i][j+1]-dungeon[i][j]
                1.如果两个数中有一个为负数则hp = 1可以存活
                2.如果两个数都是正数, 选最小值
                dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j], 1)

        '''
        if not dungeon:
            return 0
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (cols + 1)  for _ in range(rows + 1)]

        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1

        for i in range(row - 1, -1, -1):
            for j in range(cols - 1, -1 ,-1):
                dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)
        return dp[0][0]

