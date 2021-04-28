# coding:utf8
"""
    424. 替换后的最长重复字符
    给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次
    在执行上述操作后，找到包含重复字母的最长子串的长度。
    注意：字符串长度 和 k 不会超过 104。

    输入：s = "ABAB", k = 2
    输出：4
    解释：用两个'A'替换为两个'B',反之亦然。

    输入：s = "AABABBA", k = 1
    输出：4
    解释：
    将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
    子串 "BBBB" 有最长重复字母, 答案为 4。


    链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.characterReplacement_v1(s, k)

    def characterReplacement_v1(self, s: str, k: int) -> int:
        """
            滑动窗口
        """
        from collections import Counter

        left, right = 0, 0
        window = Counter()
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            
            # 窗口的串的长度- 窗口中频次最高的数 > k, 缩小窗口
            while right - left - window.most_common(1)[0][1] > k:
                d = s[left]
                left += 1
                window[d] -= 1

            res = max(res, right - left)


        return res



if __name__ == '__main__':
    s = 'ABAB'
    k = 2
    obj = Solution()
    print(obj.characterReplacement(s, k))
