# coding:utf8
"""
1234. 替换子串得到平衡字符串
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。

假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。

给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
请返回待替换子串的最小可能长度。
如果原字符串自身就是一个平衡字符串，则返回 0。

输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。

链接：https://leetcode-cn.com/problems/replace-the-substring-for-balanced-string
"""

class Solution:
    def balancedString(self, s: str) -> int:
        return self.balancedString_v1(s)
    def balancedString_v1(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)


if __name__ == '__main__':
    s = 'QWER'
    obj = Solution()
    print(obj.balancedString(s))

