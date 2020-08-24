# coding:utf8

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        #return self.rangeBitwiseAnd_v1(m, n)
        return self.rangeBitwiseAnd_v2(m, n)
    def rangeBitwiseAnd_v1(self, m: int, n: int) -> int:
        """ 暴力 """
        if m == 0 or n == 0:
            return 0

        res, i = n, n - 1
        while i >= m:
            res = res & i
            if res == 0:
                return res
            i -= 1

        return res

    def rangeBitwiseAnd_v2(self, m: int, n: int) -> int:
        """
            26-30
            11010
            11011
            11100
            11101
            11110
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1

        return m << i



if __name__ == '__main__':
    obj = Solution()
    m, n = 5, 7
    res = obj.rangeBitwiseAnd(m, n)
    print(res)
