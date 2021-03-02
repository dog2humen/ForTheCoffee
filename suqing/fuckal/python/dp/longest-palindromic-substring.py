# coding:utf8
"""
    最长回文子串
    给你一个字符串 s，找到 s 中最长的回文子串。
    示例 1：
    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。
    链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #return self.longestPalindrome_v1(s)
        #return self.longestPalindrome_v2(s)
        return self.longestPalindrome_v3(s)
    def longestPalindrome_v1(self, s: str) -> str:
        """
            已s[i]为中心向两侧扩散去判断是否是回文
            需要处理长度为奇数和偶数的情况
        """
        def helper(s: str, i: int, j: int) -> str:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j]

        res = ''
        for i in range(len(s)):
            s1 = helper(s, i, i) # 以s[i]为中心的
            s2 = helper(s, i, i + 1) # 以s[i]和s[i + 1]为中心的
            res = s1 if len(s1) > len(res) else res
            res = s2 if len(s2) > len(res) else res
        return res
    
    def longestPalindrome_v2(self, s: str) -> str:
        """
            dp table
            定义dp[i][j]为s[i...j]是否是回文串
            dp[i][j] = dp[i - 1][j + 1] == True and s[i] == s[j]
            base case dp[0][0] = True

        """
        res = ''
        size = len(s)
        if size < 2:
            return s
        dp = [[False] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(j):
                print(i, j, s[i], s[j])
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                print(dp[i][j])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i: j + 1]
        
        return res

    def longestPalindrome_v3(self, s: str) -> str:
        size = len(s)
        dp = [[False] * size for _ in range(size)]
        res = ''
        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i: j + 1]
        return res

if __name__ == '__main__':
    s = 'ecabbad'
    s = 'acbed'
    s = 'a'
    obj = Solution()
    print(obj.longestPalindrome(s))

