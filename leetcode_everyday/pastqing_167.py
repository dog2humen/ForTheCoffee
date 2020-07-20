# coding:utf8
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return self.twoSum_v1(numbers, target)
        #return self.twoSum_v2(numbers, target)
        return self.twoSum_v3(numbers, target)
    def twoSum_v1(self, numbers: List[int], target: int) -> List[int]:
        '''
            回溯 + 剪枝
        '''
        res = []
        self.helper(numbers, target, res, [], 0)
        return res

    def helper(self, numbers, target, res, cur, start):

        # terminated
        if len(cur) == 2 and target == 0:
            res.extend(cur)
            return

        
        for i in range(start, len(numbers)):
            if target < numbers[i]:
                continue
            self.helper(numbers, target - numbers[i], res, cur + [i + 1], i + 1)

    def twoSum_v2(self, numbers: List[int], target: int) -> List[int]:
        '''
            二分
        '''
        for i in range(len(numbers)):
            res = self.binarySearch(numbers, i + 1, len(numbers), target - numbers[i])
            if res is not None:
                return [i + 1, res + 1]
        
        return []
    def binarySearch(self, numbers, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid

        return None

    def twoSum_v3(self, numbers: List[int], target: int) -> List[int]:
        '''
            双指针
        '''
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []




if __name__ == '__main__':
    obj = Solution()
    numbers = [-1, 0]
    target = -1
    res = obj.twoSum(numbers, target) 
    print(res)

