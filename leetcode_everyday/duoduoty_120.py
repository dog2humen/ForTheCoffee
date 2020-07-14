# encoding=utf8
"""
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""
class Solution(object):
    # dp method:
    def minimumTotal_dp(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        m = len(triangle) - 1
        for i in range(m)[::-1]:
            for j in range(i+1):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]

        return triangle[0][0]

    # dfs with memory method
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        memo = [[0] * _ for _ in range(len(triangle)+1)[1:]]
        return self.dfs(triangle, memo, 0, 0)

    def dfs(self, triangle, memo, row, col):
        # 递归终止条件
        if row > len(triangle) - 1:
            return 0
        if memo[row][col] != 0:
            return memo[row][col]

        # 递归过程
        memo[row][col] = triangle[row][col] + \
                         min(self.dfs(triangle, memo, row+1, col), self.dfs(triangle, memo, row+1, col+1))

        return memo[row][col]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    s = Solution()
    print s.minimumTotal(triangle)


