# coding:utf-8
# 169 https://leetcode-cn.com/problems/majority-element/description/
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        res = filter(lambda item: item[1] > len(nums)/2, c.items())
        return list(res)[0][0]

if __name__ == '__main__':
    obj = Solution()
    nums = [2,2,1,1,1,2,2]
    res = obj.majorityElement(nums)
    print(res)
	
