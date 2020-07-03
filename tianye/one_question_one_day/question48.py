# encoding=utf8
"""
剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :滑动窗口
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        d = {}
        head, res_num = 0, 0
        for i in range(len(s)):  # head为滑动窗口的头，i 为滑动窗口的尾部
            if s[i] in d:
                head = max(d[s[i]] + 1, head)  # 有可能出现 d[s[i]] + 1 比 head 小的情况，所以这里需要 max （见测试用例）
            d[s[i]] = i  # 记录某个字符最后出现的位置
            res_num = max(res_num, i - head + 1)
        return res_num


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring('abba')
