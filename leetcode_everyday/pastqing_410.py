# coding:utf8
from typing import List
import functools

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #return self.splitArray_v1(nums, m)
        return self.splitArray_v2(nums, m)
    def splitArray_v1(self, nums: List[int], m: int) -> int:
        '''
            递归回溯
        '''
        if not nums:
            return 0
        if m == 1:
            return sum(nums)
        self.res = float('+inf')
        self.helper(nums, m - 1, 0, len(nums), [])
        return self.res
    def helper(self, nums, m, start, end, cur):
        # terminated
        if m == 0 and start < end:
            # 最后一次的选择
            cur += [nums[start: end]]
            tmp_res = max(map(lambda x : self.getSum(tuple(x)), cur))
            self.res = min(self.res, tmp_res)
            return 

        # current level
        # 选一个分隔位置, 总共要选m - 1次
        for i in range(start, end):
            self.helper(nums, m - 1, i + 1, end, cur + [nums[start : i+1]])

    @functools.lru_cache
    def getSum(self, arr):
        return sum(arr)

    def splitArray_v2(self, nums: List[int], m: int) -> int:
        '''
            二分思路:
            分割子数组的和的最大值一定在[max(nums), sum(nums)] 这个区间
            那么要找的答案就在这个区间范围内, 使用二分去搜索这个值, 相当于搜索最左侧的值
            如何搜索:
            
            判断当前的搜索的sum值, 遍历数组, 累计求和, 如果加上nums[i]后, sum值大于搜索的sum值, 说明遍历数组之前的元素可以作为一个分割

        '''
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.checkSplit(nums, mid, m):
                right = mid
            else:
                left = mid + 1

        return left

    def checkSplit(self, nums, chSum, m):
        curSum = 0
        cnt = 1
        for n in nums:
            if curSum + n > chSum:
                cnt += 1
                curSum = n
            else:
                curSum += n
        
        return cnt <= m 

if __name__ == '__main__':
    obj = Solution()
    nums = [7,2,5,10,8]
    #nums = [1,4,4]
    m = 2
    res = obj.splitArray(nums, m)
    print(res)
