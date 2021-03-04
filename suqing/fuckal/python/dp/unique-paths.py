# coding:utf8
"""
    62. 不同路径
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
    问总共有多少条不同的路径？
    示例 2：
    输入：m = 3, n = 2
    输出：3
    解释：
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向下

    链接：https://leetcode-cn.com/problems/unique-paths
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePaths_v1(m, n)

    def uniquePaths_v1(self, m: int, n: int) -> int:
        """
            dp table
            定义dp[i][j] = x 表示坐标(0,0) -> (i, j)下的路径数为x
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            ans: dp[-1][-1]
            base case:
                第一行只能从左侧来
                dp[0][j] = dp[0][j - 1] = 1
                第一列只能从上面来
                dp[i][0] = dp[i - 1][0] = 1

        """

        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    m, n = 3, 2
    obj = Solution()
    print(obj.uniquePaths(m, n))
