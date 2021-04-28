# coding:utf8
"""
    75. 颜色分类
    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

    示例 1：

    输入：nums = [2,0,2,1,1,0]
    输出：[0,0,1,1,2,2]

    链接：https://leetcode-cn.com/problems/sort-colors
"""


from typing import List
class Solution:

    def sortColors(self, nums: List[int]) -> List[int]:
        #return self.sortColors_v1(nums)
        return self.sortColors_v2(nums)
    def sortColors_v1(self, nums: List[int]) -> List[int]:
        
        pos0 = 0
        pos1 = 0
        for cur in range(len(nums)):
            val = nums[cur]
            nums[cur] = 2
            if val < 2:
                nums[pos1] = 1
                pos1 += 1
            if val == 0:
                nums[pos0] = 0
                pos0 += 1
        return nums

    def sortColors_v2(self, nums: List[int]) -> List[int]:

        p1 = 0
        p2 = len(nums) - 1
        cur = 0
        while cur < len(nums):
            if cur > p2:
                break
            val = nums[cur]
            if val == 0:
                nums[p1], nums[cur] = nums[cur], nums[p1]
                p1 += 1
            elif val == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
                cur -= 1
            cur += 1


        return nums



if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    nums = [2, 0, 1]
    obj = Solution()
    print(obj.sortColors(nums))
