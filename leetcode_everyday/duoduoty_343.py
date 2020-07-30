#encoding=utf8
"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。
返回你可以获得的最大乘积。

示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
"""
class Solution(object):
    """
    1、
    状态：i
    选择：拆分、拆分多次、不拆分
    2、
    dp[i] : 定义 dp，当前正整数 i 可得到的最大乘积

    3、
    状态转移方程： dp[i] = max
                         j * (i - j) 拆一次
                         j * dp[i - j] 拆多次
    4、
    初始状态： dp[0] = dp[1] = 0

    5、
    由于可能的 j 是 从 0 到 i-1，不知道在哪个 j 时得到最大值
    故：两个循环 i， j
    dp[i] = max
            dp[i]
            j * (i - j) 拆一次
            j * dp[i - j] 拆多次
    """
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

