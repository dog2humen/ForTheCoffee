# coding:utf8
"""
    480. 滑动窗口中位数
    中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

    例如：

    [2,3,4]，中位数是 3
    [2,3]，中位数是 (2 + 3) / 2 = 2.5
    给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
    链接：https://leetcode-cn.com/problems/sliding-window-median
"""
from typing import List
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        return self.medianSlidingWindow_v1(nums, k)	

    def medianSlidingWindow_v1(self, nums: List[int], k: int) -> List[float]:
        """
            二分查找思路
        """
        import bisect

        median = lambda x : (x[(len(x) - 1) // 2] + x[len(x) // 2]) / 2
        res = []
        first_window = sorted(nums[:k])
        res.append(median(first_window))

        for del_val, ins_val in zip(nums[:-k], nums[k:]):
            first_window.pop(bisect.bisect_left(first_window, del_val))
            bisect.insort_left(first_window, ins_val)
            res.append(median(first_window))

        return res



if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    obj = Solution()
    print(obj.medianSlidingWindow(nums, k))

