# coding:utf8

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minimumTotal_v1(triangle)
        #return self.minimumTotal_v2(triangle)
	
    def minimumTotal_v1(self, triangle: List[List[int]]) -> int:
        '''
            dfs
        '''
        if not triangle:
            return 0
        self.res = None
        self.helper(triangle, 0, 0, 0)
        return self.res
    def helper(self, triangle, level, start, curSum):
        # terminated
        if level > len(triangle) - 1:
            if self.res is None: 
                self.res = curSum
            else:
                self.res = min(self.res, curSum)
            return

        # current level
        for i, val in enumerate(triangle[level][start:start + 2]):
            # 剪枝
            self.helper(triangle, level + 1, start + i, curSum + val)


    def minimumTotal_v2(self, triangle: List[List[int]]) -> int:
        '''
            dp[i][j]表示triangle 第[i, j]位置的最短路径和

            状态转移方程:
                自顶向下
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + triangle[i][j]
                自底向上
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        '''
        if not triangle:
            return 0
        dp = triangle
        rows = len(triangle)
        for i in range(rows - 2, -1, -1):
            for j in range(len(triangle[i]) - 1, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]
	

if __name__ == '__main__':
    obj = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    #triangle = [[-1],[2,3],[1,-1,-3]]
    triangle = [[1],[-5,-2],[3,6,1],[-1,2,4,-3]]
    res = obj.minimumTotal(triangle)
    print(res)
