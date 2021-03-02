# coding:utf8
"""
    10. 正则表达式匹配
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

     
    示例 1：

    输入：s = "aa" p = "a"
    输出：false
    解释："a" 无法匹配 "aa" 整个字符串。

    示例 2:
    输入：s = "aa" p = "a*"
    输出：true
    解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

    示例 3：
    输入：s = "ab" p = ".*"
    输出：true
    解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

    示例 4：
    输入：s = "aab" p = "c*a*b"
    输出：true
    解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

    链接：https://leetcode-cn.com/problems/regular-expression-matching
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatch_v1(s, p)

    def isMatch_v1(self, s: str, p: str) -> bool:
        
        memo = {}
        def dp(i: int, j: int) -> bool:
            """
                s第i位置, p第j位置是否匹配
            """
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and p[j] in {s[i], '.'}
            res = False
            if j + 2 <= len(p) and p[j + 1] == '*': # 匹配0次或者1次
                memo[(i, j)] = dp(i, j + 2) or first_match and dp(i + 1, j)
            else:
                memo[(i, j)] = first_match and dp(i + 1, j + 1)
            return memo[(i, j)]
        return dp(0, 0)

    def isMatch_v2(self, s: str, p: str) -> bool:
        pass

if __name__ == '__main__':
    s, p = 'ab', '.*'
    s, p = 'aa', 'a'
    obj = Solution()
    print(obj.isMatch(s, p))

