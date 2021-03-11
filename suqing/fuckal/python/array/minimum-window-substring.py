# coding:utf8
"""
    76. 最小覆盖子串
    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

    注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
    输入：s = "ADOBECODEBANC", t = "ABC"
    输出："BANC"
    链接：https://leetcode-cn.com/problems/minimum-window-substring
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.minWindow_v1(s, t)
    def minWindow_v1(self, s: str, t: str) -> str:
        from collections import Counter
        from collections import defaultdict
        
        needs = Counter(t)
        window = defaultdict(int)
        left, right = 0, 0
        valid = 0
        start, le = 0, float('inf') # 记录最小覆盖子串的起始索引以及长度
        while right < len(s):
            c = s[right]
            right += 1

            # 窗口内数据更新
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1

            print(window, left, right, s[left : right])
            # 判断左侧窗口是否需要收缩
            # 找到一个可行解
            while valid == len(needs):
                # 更新结果
                if right - left < le:
                    start = left
                    le = right - left

                d = s[left]
                left += 1 # 收缩窗口
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1


        return '' if le == float('inf') else s[start : start + le]





if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    obj = Solution()
    print(obj.minWindow(s, t))


