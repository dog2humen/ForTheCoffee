# coding:utf8
"""
    回文子串
    给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
    具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
    示例 1：
    输入："abc"
    输出：3
    解释：三个回文子串: "a", "b", "c"
    链接：https://leetcode-cn.com/problems/palindromic-substrings
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
            dp table
            dp[i][j]表示s[i..j]是否是回文子串(True / False)
            if s[i] == s[j], dp[i][j] = dp[i + 1][j - 1]
            base case:
                i == j, dp[i][j] = True
                i > j, dp[i][j] = 0
        """

        size = len(s)
        dp = [[False] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
        res = 0
        for i in range(size - 1 , -1, -1):
            for j in range(i, size):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j]:
                    res += 1
        return res

if __name__ == '__main__':
    s = 'abc'
    obj = Solution()
    print(obj.countSubstrings(s))
