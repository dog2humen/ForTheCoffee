# coding:utf8
"""
    395. 至少有 K 个重复字符的最长子串
    给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 
    要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
    输入：s = "aaabb", k = 3
    输出：3
    解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
    https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstring_v1(s, k)

    def longestSubstring_v1(self, s: str, k: int) -> int:
        """
            滑动窗口
        """
        from collections import Counter

        left, right = 0, 0
        res = 0
        window = Counter()
        needs = Counter(s)

        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1

            print(s[left : right], window)
            while len(needs) == len(window):

                flag = any([item >= k for item in window.values()])
                if flag:
                    res = max(res, right - left)
                d = s[left]
                left += 1
                window[d] -= 1

        return res



        

if __name__ == '__main__':
    s, k = 'aaabb', 3
    s, k = 'ababbc', 2 
    obj = Solution()
    print(obj.longestSubstring(s, k))
