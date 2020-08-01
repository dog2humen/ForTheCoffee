# encoding=utf8
"""
632. 最小区间
你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1:
输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释:
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。

注意:
给定的列表可能包含重复元素，所以在这里升序表示 >= 。
1 <= k <= 3500
-105 <= 元素的值 <= 105
对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
"""
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        return self.smallestRange_v1(nums)

    """
    1、取每个数组中的最大值的最小值，作为返回区间的左边界
    2、通过二分，查看左边界应该在每个数组中插入的位置
    3、比较每个数组该位置的值，取最大的
    理想很丰满，现实很骨感，可通过 70+ case，但以下case，均无法通过。
    if nums == [[1,2,3],[1,2,3],[1,2,3]]: return [1,1]
    if nums == [[1,3,5,7,9],[2,4,6,8,10]]: return [1,2]
    if nums == [[1,4,7,10],[2,5,8,11],[3,6,9,12]]: return [1,3]
    """
    def smallestRange_v1(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        left = 10 ** 5
        right = - 10 ** 5

        for list in nums:
            left = min(left, list[-1])

        for list in nums:
            index =self.binary_search(list, left)
            right = max(right, list[index])

        return [left, right]

    def smallestRange_v2(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        left = 10 ** 5
        right = - 10 ** 5

        for list in nums:
            right = max(right, list[0])

        for list in nums:
            index =self.binary_search(list, right)
            left = min(left, list[index])

        return [left, right]

    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left if left < len(arr) else len(arr) - 1

    # heap 
    # todo：不理解，明天看
    def smallestRange_v3(self, nums):
        rangeLeft, rangeRight = -10 ** 9, 10 ** 9
        maxValue = max(vec[0] for vec in nums)
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)

        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))

        return [rangeLeft, rangeRight]


if __name__ == '__main__':
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    s = Solution()
    print s.smallestRange(nums)
