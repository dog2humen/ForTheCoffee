# coding:utf8

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.topKFrequent_v1(nums, k)
    def topKFrequent_v1(self, nums: List[int], k: int) -> List[int]:
        counter = [(k, v) for k, v in Counter(nums).items()]
        res = heapq.nlargest(k, counter, key = lambda x : x[1])
        return [item[0] for item in res]


if __name__ == '__main__':
    obj = Solution()
    nums = [1,1,1,2,2,3]
    #nums = [-1, -1]
    k = 2
    res = obj.topKFrequent(nums, k)
    print(res)

