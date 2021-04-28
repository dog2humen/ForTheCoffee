# coding:utf8
"""
    4. 寻找两个正序数组的中位数
    给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

    示例 1：
    输入：nums1 = [1,3], nums2 = [2]
    输出：2.00000
    解释：合并数组 = [1,2,3] ，中位数 2
    链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedianSortedArrays_v1(nums1, nums2)
    def findMedianSortedArrays_v1(self, nums1: List[int], nums2: List[int]) -> float:
        """
            思路
            遍历找中位数
        """
        size1, size2 = len(nums1), len(nums2)
        size = size1 + size2
        pos1, pos2 = 0, 0
        preVal, curVal = None, None

        for _ in range(size // 2 + 1):
            preVal = curVal
            if (pos1 < size1 and (pos2 >= size2 or nums1[pos1] < nums2[pos2])):
                curVal = nums1[pos1]
                pos1 += 1
            else:
                curVal = nums2[pos2]
                pos2 += 1



        if size % 2 == 0:
            return (preVal + curVal) / 2
        else:
            return curVal

    def findMedianSortedArrays_v2(self, nums1: List[int], nums2: List[int]) -> float:
        pass


if __name__ == '__main__':
    nums1, nums2 = [1, 3], [2]
    obj = Solution()
    print(obj.findMedianSortedArrays(nums1, nums2))
