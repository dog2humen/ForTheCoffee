# coding:utf8
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [n for n in range(1, 10)]
        res = []
        self.helper(nums, n, k, 0, [], res)
        return res

    def helper(self, nums, target, k, start, cur, res):

        if len(cur) == k and target == 0:
            res.append(cur[:])
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if target - nums[i] < 0:
                break
            self.helper(nums, target - nums[i], k, i + 1, cur + [nums[i]], res)


if __name__ == '__main__':
    obj = Solution()
    k, n = 3, 7
    res = obj.combinationSum3(k, n)
    print(res)

