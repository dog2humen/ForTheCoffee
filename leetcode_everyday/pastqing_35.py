# coding:utf8
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
            二分找最左
	'''
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid


        return left



		
