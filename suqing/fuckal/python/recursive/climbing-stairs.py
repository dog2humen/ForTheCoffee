# coding:utf8

# https://leetcode-cn.com/problems/climbing-stairs/ 
class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        return self.climbStairs_v1(n)
        #return self.climbStairs_v2(n)

    def climbStairs_v1(self, n: int) -> int:
        '''
            dp[i]表示第i个台阶用的方法数
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[0] = 0
            dp[1] = 1
            dp[2] = 2
        '''
        if n < 2:
            return n
        dp_1, dp_2 = 1, 2
        for i in range(3, n + 1):
            dp_1, dp_2 = dp_2, dp_1 + dp_2
        return dp_2

    def climbStairs_v2(self, n: int) -> int:
        '''
            记忆化递归
            f(n) = f(n - 1) + f(n - 2)
        '''
        if n <= 2:
            return n
        if n - 1 in self.memo:
            res_1 = self.memo.get(n - 1)
        else:
            res_1 = self.climbStairs_v2(n - 1)
            self.memo[n - 1] = res_1

        if n - 2 in self.memo:
            res_2 = self.memo.get(n - 2)
        else:
            res_2 = self.climbStairs_v2(n - 2)
            self.memo[n - 2] = res_2

        return res_1 + res_2

