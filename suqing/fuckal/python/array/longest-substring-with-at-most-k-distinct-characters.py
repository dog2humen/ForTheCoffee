# coding:utf8
"""
    340. 至多包含 K 个不同字符的最长子串
    给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

    示例 1:
    输入: s = "eceba", k = 2
    输出: 3
    解释: 则 T 为 "ece"，所以长度为 3。
    链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        return self.lengthOfLongestSubstringKDistinct_v1(s, k)

    def lengthOfLongestSubstringKDistinct_v1(self, s: str, k: int) -> int:
        """
            滑动窗口
        """
        from collections import Counter

        left, right, valid = 0, 0, 0
        window = Counter()
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            valid = len([k for k, v in window.items() if v > 0])

            while valid > k:
                d = s[left]
                left += 1
                window[d] -= 1
                valid = len([k for k, v in window.items() if v > 0])

            res = max(res, right - left)
        return res

        

if __name__ == '__main__':
    s, k = 'eceba', 2
    obj = Solution()
    print(obj.lengthOfLongestSubstringKDistinct(s, k))
