# coding:utf8
from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        #return self.minArray_v1(numbers)
        return self.minArray_v2(numbers)

    def minArray_v1(self, numbers: List[int]) -> int:
        '''
            暴力
        '''
        cur = 0
        while cur < len(numbers) - 1:
            if numbers[cur] > numbers[cur + 1]:
                return numbers[cur + 1]
            cur += 1

        return numbers[0]

    def minArray_v2(self, numbers: List[int]) -> int:
        '''
            二分
            旋转后,可将数组分割为两部分, 左半排序数组 > 右半排序数组
            考虑又边界元素right, 最小值点右半 < numbers[right], 最小值左半 > numbers[right]
            取mid = left + (right - left) // 2
            if nums[mid] < nums[right] 说明mid在最小值的右半, 最小值点在[i, mid] 区间内
            if nums[mid] > nums[right] 说明mid在最小值的左半, 最小值点在[mid + 1, right]区间内
            if nums[mid] == nums[right] 无法确定, 缩小right
        '''
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
        
        return numbers[left]



if __name__ == '__main__':
    numbers = [3,4,5,1,2]
    obj = Solution()
    res = obj.minArray(numbers)
    print(res)
