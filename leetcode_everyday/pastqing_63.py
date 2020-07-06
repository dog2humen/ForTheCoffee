# coding:utf8
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #return self.uniquePathsWithObstacles_v1(obstacleGrid)
        return self.uniquePathsWithObstacles_v2(obstacleGrid)

    def uniquePathsWithObstacles_v1(self, obstacleGrid: List[List[int]]) -> int:
        '''
            搜索, 递归, 自底向上
            ac不过, 超时了
        '''
        if not obstacleGrid:
            return 0
        row_index, col_index = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        return self.helper(obstacleGrid, row_index, col_index)


    def helper(self, obstacleGrid, row_index, col_index):
        # terminated
        if row_index < 0 or col_index < 0:
            return 0

        # current level
        if obstacleGrid[row_index][col_index] == 1:
            return 0
        
        if row_index == 0 and col_index == 0:
            return 1

        return self.helper(obstacleGrid, row_index - 1, col_index) + self.helper(obstacleGrid, row_index, col_index - 1)
        

    def uniquePathsWithObstacles_v2(self, obstacleGrid: List[List[int]]) -> int:
        '''
            dp[i][j]表示从起始位置到obstacleGrid[i, j]位置的路径个数
            自底向上
            状态转移方程:
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] # 从下或者从右转移而来


        '''
        if not obstacleGrid:
            return 0

        row_l, col_l = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * col_l for _ in range(row_l)]
        # 初始状态
        dp[row_l - 1][col_l - 1] = 1 - obstacleGrid[row_l - 1][col_l - 1]


        # 列边界
        for i in range(row_l - 2, -1, -1):
            dp[i][col_l - 1] = dp[i + 1][col_l - 1] * (1 - obstacleGrid[i][col_l - 1])

        
        # 行边界
        for j in range(col_l - 2, -1, -1):
            dp[row_l - 1][j] = dp[row_l - 1][j + 1] * (1 - obstacleGrid[row_l - 1][j])
        

        # 中间部分
        for i in range(row_l - 2, -1, -1):
            for j in range(col_l - 2, -1, -1):
                dp[i][j] = (dp[i + 1][j] + dp[i][j + 1]) * (1 - obstacleGrid[i][j])



        return dp[0][0]



if __name__ == '__main__':
    obj = Solution()
    input = [[0,0,0],[0,1,0],[0,0,0]]
    #input = [[0,0],[1,1],[0,0]]
    res = obj.uniquePathsWithObstacles(input)
    print(res)
