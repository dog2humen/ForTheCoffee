# coding:utf8
"""
    159. 至多包含两个不同字符的最长子串
    给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。
    输入: "eceba"
    输出: 3
    解释: t 是 "ece"，长度为3。
    https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/

"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        return self.lengthOfLongestSubstringTwoDistinct_v1(s)

    def lengthOfLongestSubstringTwoDistinct_v1(self, s: str) -> int:
        """
            滑动窗口
        """
        from collections import Counter
        left, right, valid = 0, 0, 0
        window = set()
        window = Counter()
        res = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            valid = len([k for k, v in window.items() if v > 0])

            while valid > 2:
                d = s[left]
                left += 1
                window[d] -= 1
                valid = len([k for k, v in window.items() if v > 0])
            res = max(res, right - left)
        
        return res


if __name__ == '__main__':
    s = 'ccaabbb'
    s = 'abaccc'
    obj = Solution()
    print(obj.lengthOfLongestSubstringTwoDistinct(s))
