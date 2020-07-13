# encoding=utf8
"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
"""
import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        dict = collections.defaultdict(int)
        print dict
        for i in range(len(nums1)):
            dict[nums1[i]] += 1 if nums1[i] in dict else dict[nums1[i]] == 1

        res = []
        for j in range(len(nums2)):
           if nums2[j] in dict and dict[nums2[j]] > 0:
               res.append(nums2[j])
               dict[nums2[j]] -= 1

        return res

