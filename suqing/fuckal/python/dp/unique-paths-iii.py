# coding:utf8
"""
    980. 不同路径 III
    在二维网格 grid 上，有 4 种类型的方格：
    1 表示起始方格。且只有一个起始方格。
    2 表示结束方格，且只有一个结束方格。
    0 表示我们可以走过的空方格。
    -1 表示我们无法跨越的障碍。
    返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
    每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

    示例 1：
    输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    输出：2
    解释：我们有以下两条路径：
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

    链接：https://leetcode-cn.com/problems/unique-paths-iii
"""
from typing import List
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        return self.uniquePathsIII_v1(grid)

    def uniquePathsIII_v1(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])

        memo = {}
        def dp(i: int, j: int, empty_num: int) -> int:
            """
                返回: 从start点到坐标(i, j)的路径个数
            """

            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == -1 or grid[i][j] == -2:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if grid[i][j] == -1:
                return 0

            if grid[i][j] == 2:
                return 1 if empty_num == 0 else 0

            # mark visited
            old = grid[i][j]
            grid[i][j] = -2
            res = 0
            res +=  dp(i - 1, j, empty_num - 1)
            res +=  dp(i + 1, j, empty_num - 1)
            res +=  dp(i, j - 1, empty_num - 1)
            res +=  dp(i, j + 1, empty_num - 1)

            grid[i][j] = old
            memo[(i, j)] = res
            return memo[(i, j)]

        sx, sy, empty = 0, 0, 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j

        return dp(sx, sy, empty)


if __name__ == '__main__':
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    obj = Solution()
    print(obj.uniquePathsIII(grid))
