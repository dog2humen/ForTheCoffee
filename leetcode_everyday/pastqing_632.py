# coding:utf8
from typing import List
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        return self.smallestRange_v1(nums)
    def smallestRange_v1(self, nums: List[List[int]]) -> List[int]:
        '''
            利用最小堆
            从k个列表中各取一个数, 使得这k个数中的最大值与最小值的差最小
            使用最小堆维护 kk 个指针指向的元素中的最小值，同时维护堆中元素的最大值。初始时，kk 个指针都指向下标 00，最大元素即为所有列表的下标 00 位置的元素中的最大值。每次从堆中取出最小值，根据最大值和最小值计算当前区间，如果当前区间小于最小区间则用当前区间更新最小区间，然后将对应列表的指针右移，将新元素加入堆中，并更新堆中元素的最大值。
            如果一个列表的指针超出该列表的下标范围，则说明该列表中的所有元素都被遍历过，堆中不会再有该列表中的元素，因此退出循环。
        '''



if __name__ == '__main__':
    obj = Solution()
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

