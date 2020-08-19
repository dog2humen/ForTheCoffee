# coding:utf8
class Solution:
    def countSubstrings(self, s: str) -> int:
        #return self.countSubstrings_v1(s)
        return self.countSubstrings_v2(s)
    def countSubstrings_v1(self, s: str) -> int:
        """暴力循环 """
        if not s:
            return 0
        res = 0
        size = len(s)
        for i in range(size):
            for j in range(i, size):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    res += 1



        return res

    def countSubstrings_v2(self, s: str) -> int:
        """
            dp: s[0..i]是回文, 添加一个 i + 1是否是回文
            定义: dp[i][j]表示子串s[i..j]是否回文
            状态转移方程:
                中心扩散
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
            初始化:
                dp[i][j] = True if i == j
                
        """
        res = 0
        size = len(s)
        dp = [[False] * size for _ in range(size)]
        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j]:
                    res += 1
        return res



if __name__ == '__main__':
    obj = Solution()
    s = 'aaa'
    res = obj.countSubstrings(s)
    print(res)
