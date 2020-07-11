# coding:utf8
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        return self.countSmaller_v1(nums)
    def countSmaller_v1(self, nums: List[int]) -> List[int]:
        '''
            1.利用归并排序, 统计前后分割的两数组
            2.利用索引数组, 定位元素在原数组的位置
        '''
        # 构建下标索引的数组
        indexes = [i for i in range(len(nums))]
        res = [0] * len(nums)
        self.helper(nums, indexes, 0, len(nums) - 1, res)
        return res

    def helper(self, nums, indexes, left, right, res):
        if left < right:
            mid = left + (right - left) // 2
            self.helper(nums, indexes, left, mid, res)
            self.helper(nums, indexes, mid + 1, right, res)
            self.merge(nums, indexes, left, mid, right, res)

    def merge(self, nums, indexes, left, mid, right, res):

        # 前有序数组[left : mid + 1] 
        # 后有序数组[mid + 1: right + 1]
        # indexes 索引数组 [5, 2, 6, 1] -> [0, 1, 2, 3]
        # 排序索引数组即可

        new_indexes = [0] * (right - left + 1) 
        right_count = 0
        i, j, k = left, mid + 1, 0
        while i <= mid and j <= right:
            if nums[indexes[j]] < nums[indexes[i]]:
                new_indexes[k] = indexes[j]
                j += 1
                right_count += 1
            else:
                new_indexes[k] = indexes[i]
                res[indexes[i]] += right_count
                i += 1

            k += 1

        while i <= mid:
            new_indexes[k] = indexes[i]
            res[indexes[i]] += right_count
            i += 1
            k += 1

        while j <= right:
            new_indexes[k] = indexes[j]
            j += 1
            k += 1

        for i in range(0, len(new_indexes)):
            indexes[left + i] = new_indexes[i]

if __name__ == '__main__':
    obj = Solution()
    input = [5,2,6,1]
    #input = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
    print(input)
    res = obj.countSmaller(input)
    print(res)
