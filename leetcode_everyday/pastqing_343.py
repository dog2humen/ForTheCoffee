# coding:utf8
class Solution:
    def integerBreak(self, n: int) -> int:
        return self.integerBreak_v1(n)
    def integerBreak_v1(self, n: int) -> int:
        '''
            dp
            定义: dp[i]当前正整数i可以拆分后的最大乘积
            选择: 拆一次, 拆分多次, 不拆
            状态转移方程:
                枚举拆分的值j j的值域范围为[1, i]闭区间
                dp[i] = max(
                    dp[i],
                    j * (i - j) 一次
                    j * dp[i - j] 多次
                )

        '''
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]


if __name__ == '__main__':
    obj = Solution()


