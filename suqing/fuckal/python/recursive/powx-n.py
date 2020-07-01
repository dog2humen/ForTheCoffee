# coding:urf-8
# 50 https://leetcode-cn.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
            x的n次幂
            n = 0, f(x) = 1
            n = 1, f(x) = n

            n为偶数, f(n) = f(n//2) * f(n//2)
            n为奇数, f(n) = f(n//2) * f(n//2) * x
        '''
        if n < 0:
            x = 1 / x
            n = -n
    def helper(self, n, x):
        if n == 0:
            return 1.0
        res = self.helper(n//2, x)
        if n & 1 == 1:
            return res * res * x
        else:
            return res * res


