# coding:utf8
from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.intersect_v1(nums1, nums2)
	
    def intersect_v1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
            使用hash表
        '''
        size_1, size_2 = len(nums1), len(nums2)
        if size_1 == 0 or size_2 == 0:
            return []

        res = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        if size_1 < size_2:
            res = [num for num in c1 if num in c2 for _ in range(min(c1[num], c2[num]))]
        else:
            res = [num for num in c2 if num in c1 for _ in range(min(c2[num], c1[num]))]


        return res
        


    def intersect_v2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pass

if __name__ == '__main__':
    obj = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res = obj.intersect(nums1, nums2)
    print(res)
