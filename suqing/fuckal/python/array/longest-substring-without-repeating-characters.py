# coding:utf8
"""
    3. 无重复字符的最长子串
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.lengthOfLongestSubstring_v1(s)

    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        """
            滑动窗口
        """
        from collections import defaultdict

        left, right = 0, 0
        res = float('-inf')
        window = defaultdict(int)
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            res = max(res, right - left)

        return res



if __name__ == '__main__':
    s = 'abcabcbb'
    obj = Solution()
    print(obj.lengthOfLongestSubstring(s))
