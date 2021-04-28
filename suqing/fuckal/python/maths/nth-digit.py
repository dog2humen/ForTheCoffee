# coding:utf8
"""
    400. 第 N 位数字
    在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。
    注意：n 是正数且在 32 位整数范围内（n < 231）。

    示例 1：
    输入：11
    输出：0
    链接：https://leetcode-cn.com/problems/nth-digit
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        return self.findNthDigit_v1(n)
    def findNthDigit_v1(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        while n > count * length:
            n -= count * length
            length += 1
            count *= 10
            start *= 10

        start += (n - 1) // length
        s = str(start)
        res = s[(n - 1) % length]
        return res



if __name__ == '__main__':
    n = 11
    obj = Solution()
    print(obj.findNthDigit(n))
