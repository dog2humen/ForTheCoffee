# encoding=utf8
"""
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        DP三要素：1、状态定义；2、状态转移；3、初始条件。
        """
        if not obstacleGrid:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * col for _ in range(row)]

        i = 0
        while i < row and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1

        j = 0
        while j < col and obstacleGrid[0][j] == 0:
            dp[0][j] = 1
            j += 1

        for i in range(row)[1:]:
            for j in range(col)[1:]:
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row-1][col-1]

a = [[0,0]]
s = Solution()
print s.uniquePathsWithObstacles(a)

