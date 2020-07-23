# coding:utf8
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.minPathSum_v1(grid)
    def minPathSum_v1(self, grid: List[List[int]]) -> int:
        '''
            dp[i][j] 表示到[i, j]位置的最小路径和
            自顶向下:
            状态转移方程:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        '''
        if not grid:
            return 0
        dp = grid
        rows, cols = len(grid), len(grid[0])

        for i in range(1, cols):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]


        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[-1][-1]


if __name__ == '__main__':
    obj = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    res = obj.minPathSum(grid)
    print(res)

