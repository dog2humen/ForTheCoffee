# encoding=utf8

"""
 剑指 Offer 45. 把数组排成最小的数
 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
 输入: [3,30,34,5,9]
 输出: "3033459"
"""

class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs = [str(num) for num in nums]
        return ''.join(self.quick_sort_str_list(strs, 0, len(strs) - 1))

    # 核心思路是快排
    # if str(i) + str(j) < str(j) + str(i), then i should before j
    def quick_sort_str_list(self, str_nums, left, right):
        if left >= right:
            return

        i, j = left, right

        while i < j:
            while str_nums[j] + str_nums[left] >= str_nums[left] + str_nums[j] and i < j:
                j -= 1
            while str_nums[i] + str_nums[left] <= str_nums[left] + str_nums[i] and i < j:
                i += 1
            str_nums[i], str_nums[j] = str_nums[j], str_nums[i]

        str_nums[i], str_nums[left] = str_nums[left], str_nums[i]

        self.quick_sort_str_list(str_nums, left, i - 1)
        self.quick_sort_str_list(str_nums, i + 1, right)

        return str_nums


if __name__ == '__main__':
    s = Solution()
    print s.minNumber([3,30,34,5,9])
