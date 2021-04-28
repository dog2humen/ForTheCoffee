# coding:utf8
"""
    435. 无重叠区间
    给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
    注意:
    可以认为区间的终点总是大于它的起点。
    区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
    示例 1:
    输入: [ [1,2], [2,3], [3,4], [1,3] ]
    输出: 1
    解释: 移除 [1,3] 后，剩下的区间没有重叠。
    链接：https://leetcode-cn.com/problems/non-overlapping-intervals
"""

from typing import List
from functools import cmp_to_key

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return self.eraseOverlapIntervals_v1(intervals)
    def eraseOverlapIntervals_v1(self, intervals: List[List[int]]) -> int:
        """
            1. 子数组的[start, end], 按照end升序排序
            2. 选取end最小的子数组, 即x = arr[0]
            3. 将其他子数组与x比较, 若有重叠, 则从原数组中删除
            4. start < x_end 则有重叠
        """
        if not intervals:
            return 0
        arr = sorted(intervals, key = cmp_to_key(self._sort))
        non_overlap_nums = 1
        _, end = arr[0]
        for item in arr:
            start = item[0]
            if start >= end:
                non_overlap_nums += 1
                end = item[1]
        print(non_overlap_nums)
        return len(intervals) - non_overlap_nums
        

    def _sort(self, first, second):
        return first[1] - second[1]


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    #intervals = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
    #intervals = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
    obj = Solution()
    print(obj.eraseOverlapIntervals(intervals))





