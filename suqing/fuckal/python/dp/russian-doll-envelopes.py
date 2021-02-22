# coding: utf8

"""
    俄罗斯套娃信封问题
    给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

    请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

    说明:
    不允许旋转信封。
    示例:
    输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出: 3 
    解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
    链接：https://leetcode-cn.com/problems/russian-doll-envelopes
"""
from typing import List
from functools import cmp_to_key
import sys
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        return self.maxEnvelopes_v1(envelopes)

    def maxEnvelopes_v1(self, envelopes: List[List[int]]) -> int:
        """
            dp table
            dp[i]表示以i为结尾的envelopes的递增子序列最长长度
            先对w进行升序排序, 对宽度w相同的对其h降序排序, 之后把所有的h作为数组计算最大升序子序列(LIS)
        """
        if not envelopes:
            return 0
        hs = [item[1] for item in sorted(envelopes, key = cmp_to_key(self._sort_func))]
        dp = [1 for _ in range(len(hs))]
        for i in range(len(dp)):
            for j in range(i):
                if hs[j] < hs[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def _sort_func(self, first, second):
        w_1, h_1 = first
        w_2, h_2 = second
        if w_1 == w_2:
            return h_2 - h_1
        else:
            return w_1 - w_2


        


if __name__ == '__main__':
    envelopes = [[5,4], [6,4], [6,7], [2,3]]
    obj = Solution()
    print(obj.maxEnvelopes(envelopes))
