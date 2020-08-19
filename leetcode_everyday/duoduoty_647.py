# encoding=utf8
"""
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.countSubstrings_v2(s)

    # 暴力法，超时
    def countSubstrings_v1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:return False
        res = 0
        length = len(s)
        for i in range(0, length):
            for j in range(i, length):
                if self.check_v1(s[i:j+1]):
                    res += 1
        return res

    def check_v1(self, s):
        if not s:return False

        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

    # 中心向两边扩展
    # 字符串个数可能是奇数、偶数
    def countSubstrings_v2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return False
        res = 0
        for i in range(0, len(s)):
            res += self.check_v2(s, i, i)
            res += self.check_v2(s, i, i + 1)
        return res

    def check_v2(self, s, i, j):
        num = 0
        while i >=0 and j < len(s) and s[i] == s[j]:
            num += 1
            i -= 1
            j += 1
        return num


if __name__ == '__main__':
    s = Solution()
    print s.countSubstrings('aaa')
