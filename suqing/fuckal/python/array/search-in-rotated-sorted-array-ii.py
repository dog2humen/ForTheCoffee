# coding:utf8
"""
    81. 搜索旋转排序数组 II
    已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

    在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

    给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
    链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            print(mid, nums[mid])
            if nums[mid] == target:
                return True

            if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            # 左半边有序
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # 右半边有序
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False

if __name__ == '__main__':
    nums, target = [2, 5, 6, 0, 0, 1, 2], 3
    nums, target = [5, 1, 3], 3
    nums, target = [1, 0, 1, 1, 1], 0
    obj = Solution()
    print(obj.search(nums, target))
