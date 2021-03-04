# coding:utf8
"""
    63. 不同路径 II
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    输出：2
    解释：
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右
    链接：https://leetcode-cn.com/problems/unique-paths-ii
"""
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #return self.uniquePathsWithObstacles_v1(obstacleGrid)
        return self.uniquePathsWithObstacles_v2(obstacleGrid)

    def uniquePathsWithObstacles_v1(self, obstacleGrid: List[List[int]]) -> int:
        """
            dp table
            定义: dp[i][j] = x 表示从坐标(0, 0) -> (i, j)的路径数为x
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) * (1 - nums[i][j])
            ans: dp[-1][-1]
            base case:
                第一行只能从左侧
                dp[0][j] = dp[0][j - 1] * (1 - nums[i][j])
                第一列只能从上面
                dp[i][0] = dp[i - 1][0] * (1 - num[i][j])

        """
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[1] * n for _ in range(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])

        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) * (1 - obstacleGrid[i][j])

        return dp[-1][-1]

    def uniquePathsWithObstacles_v2(self, obstacleGrid: List[List[int]]) -> int:
        """
            dp func
        """
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        
        def dp(i: int, j: int) -> int:
            
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
            return memo[(i, j)]

        return dp(m - 1, n - 1) 

if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    obstacleGrid = [[1]]
    obj = Solution()
    print(obj.uniquePathsWithObstacles(obstacleGrid))
