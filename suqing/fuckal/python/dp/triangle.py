# coding:utf8
"""
    120. 三角形最小路径和
    给定一个三角形 triangle ，找出自顶向下的最小路径和。

    每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

    示例 1：
    输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    输出：11
    解释：如下面简图所示：
       2
      3 4
     6 5 7
    4 1 8 3
    自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
    示例 2：
    输入：triangle = [[-10]]
    输出：-10
    链接：https://leetcode-cn.com/problems/triangle
"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minimumTotal_v1(triangle)

    def minimumTotal_v1(self, triangle: List[List[int]]) -> int:
        """
            dp table
            定义: dp[i][j] = x 表示坐标为(i, j)位置的最小路径和为x
            dp[i][j] = min(dp[i + 1][j] + nums[i + 1], dp[j + 1])
            ans: 
                dp[0][0]
            base case:
        """
        dp = triangle
        size = len(dp)
        for i in range(size - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    obj = Solution()
    print(obj.minimumTotal(triangle))
