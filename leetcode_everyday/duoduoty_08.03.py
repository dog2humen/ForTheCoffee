#encoding=utf8
"""
面试题 08.03. 魔术索引
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。
给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。
若有多个魔术索引，返回索引值最小的一个。

示例1:

 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0
示例2:

 输入：nums = [1, 1, 1]
 输出：1
提示:

nums长度在[1, 1000000]之间
"""
class Solution(object):
    """
    基本思路：
        二分法不仅要比较 mid， 还需要比较 left，条件较复杂，且时间复杂度最差也是 O(n)。故采用顺序遍历的暴力解法。
    优化：
        考虑到单调递增的性质，i < nums[i] 时，在 i 和 nums[i] 之间是不肯能有魔术索引的，所以 i 跳跃到 nums[i] 处
    """
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            if i < nums[i]:
                i = nums[i]
            else:
                i += 1
        return -1


s = Solution()
l = [1, 1, 1]
print s.findMagicIndex(l)
